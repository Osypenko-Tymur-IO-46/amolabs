import math
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from aitken import aitken
from error import get_error_table, get_error_curve
 
def eval_func(x):
    return math.sin(x)

nodes_x = [i * (2*math.pi) / (10 - 1) for i in range(10)]
nodes_y = [eval_func(xi) for xi in nodes_x] 

def get_nodes(n):
    return nodes_x[:n], nodes_y[:n]

def separator():
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        return line

class Window1(QWidget):
 
    A = 0.0
    B = 2 * math.pi
 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sin(x)")
        self.resize(1100, 700)
        self.build_ui()
        self.refresh()
 
    def build_ui(self):
        root = QHBoxLayout(self)

        ctrl = QVBoxLayout()
        ctrl.setAlignment(Qt.AlignTop)
        ctrl.setSpacing(8)
 
        ctrl.addWidget(QLabel("Кількість точок:"))
        self.n_combo = QComboBox()
        self.n_combo.addItems([str(i) for i in range(2, 11)])
        self.n_combo.currentIndexChanged.connect(self.refresh)
        ctrl.addWidget(self.n_combo)
 
        ctrl.addWidget(QLabel("Значення x:"))
        self.x_entry = QLineEdit(f"{math.pi:.6f}")
        self.x_entry.setMaximumWidth(160)
        ctrl.addWidget(self.x_entry)
 
        calc_btn = QPushButton("Обчислити таблицю")
        calc_btn.clicked.connect(self.show_table)
        ctrl.addWidget(calc_btn)
 
        ctrl.addWidget(separator())
 
        ctrl.addWidget(QLabel("Таблиця похибок:"))
        self.table_text = QTextEdit()
        self.table_text.setReadOnly(True)
        self.table_text.setMinimumWidth(300)
        f = QFont("Courier")
        f.setPointSize(9)
        self.table_text.setFont(f)
        ctrl.addWidget(self.table_text)
 
        plots = QVBoxLayout()

        self.fig1, self.ax1 = plt.subplots(figsize=(6, 3.2))
        self.canvas1 = FigureCanvas(self.fig1)
        plots.addWidget(self.canvas1)
 
        self.fig2, self.ax2 = plt.subplots(figsize=(6, 3.2))
        self.canvas2 = FigureCanvas(self.fig2)
        plots.addWidget(self.canvas2)
 
        root.addLayout(ctrl, stretch=1)
        root.addLayout(plots, stretch=2)
 
    def refresh(self):
        n = int(self.n_combo.currentText())
        x_nodes, y_nodes = get_nodes(n)
 
        X = np.linspace(self.A, self.B, 501)
        Y_exact  = [eval_func(x) for x in X]
        Y_interp = [aitken(x_nodes, y_nodes, x) for x in X]
        Y_err    = get_error_curve(eval_func, x_nodes, y_nodes, X)
 
        self.ax1.cla()
        self.ax1.plot(X, Y_exact,  label="sin(x)",        color="#00d4ff", linewidth=2)
        self.ax1.plot(X, Y_interp, label="Інтерполяція",  color="#ff8c00", linewidth=2, linestyle="--")
        self.ax1.scatter(x_nodes, y_nodes, color="black", zorder=5, s=40, label="Вузли")
        self.ax1.set_title("Графік інтерполяції")
        self.ax1.set_xlabel("x")
        self.ax1.set_ylabel("y")
        self.ax1.legend()
        self.ax1.grid(True)
        self.fig1.tight_layout()
        self.canvas1.draw()
 
        self.ax2.cla()
        self.ax2.plot(X, Y_err, color="#39ff14", linewidth=2)
        self.ax2.set_title("Абсолютна похибка |f(x) – P(x)|")
        self.ax2.set_xlabel("x")
        self.ax2.set_ylabel("Похибка")
        self.ax2.grid(True)
        self.fig2.tight_layout()
        self.canvas2.draw()
 
        self.show_table()
 
    def show_table(self):
        try:
            x = float(self.x_entry.text())
        except ValueError:
            self.table_text.setPlainText("Помилка: введіть коректне число")
            return
 
        n = int(self.n_combo.currentText())
        x_nodes, y_nodes = get_nodes(n)
        exact, table = get_error_table(eval_func, x_nodes, y_nodes, x)
 
        lines = ["Таблиця похибок для sin(x)", f"Точне значення f({x:.6f}) = {exact:.10f}", "", f"{'k':<4}{'P_k(x)':<22}{'Абс. похибка':<18}{'Відн. похибка %':<18}", "-" * 65]
        for k, approx, abs_err, rel_err in table:
            lines.append(f"{k:<4}{approx:<22.10f}{abs_err:<18.2e}{rel_err * 100:<18.2e}")
 
        self.table_text.setPlainText("\n".join(lines))

