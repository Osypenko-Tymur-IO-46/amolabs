import sys
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from alg import function, newton, find_intervals
 
 
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(900, 500)
        self.build_ui()
 
    def build_ui(self):
        layout = QHBoxLayout(self)

        ctrl = QVBoxLayout()
        ctrl.setAlignment(Qt.AlignTop)
        ctrl.setSpacing(8)
 
        ctrl.addWidget(QLabel("Значення A:"))
        self.a_entry = QLineEdit()
        ctrl.addWidget(self.a_entry)
 
        ctrl.addWidget(QLabel("Значення B:"))
        self.b_entry = QLineEdit()
        ctrl.addWidget(self.b_entry)
 
        ctrl.addWidget(QLabel("Точність ε:"))
        self.e_entry = QLineEdit("0.0001")
        ctrl.addWidget(self.e_entry)
 
        btn = QPushButton("Обчислити")
        btn.clicked.connect(self.calculate)
        ctrl.addWidget(btn)
 
        self.result_label = QLabel("")
        self.result_label.setWordWrap(True)
        ctrl.addWidget(self.result_label)
 
        self.fig = Figure(figsize=(6, 5))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
 
        layout.addLayout(ctrl, stretch=1)
        layout.addWidget(self.canvas, stretch=2)
 
        self.draw_graph()
 
    def draw_graph(self, root=None):
        self.ax.cla()
        x_vals = np.linspace(-2, 3, 500)
        y_vals = [function(x) for x in x_vals]
 
        self.ax.plot(x_vals, y_vals, color="blue", label="f(x) = x³ + 10x − 9")
        self.ax.axhline(0, color="black", linewidth=0.8)
        self.ax.axvline(0, color="black", linewidth=0.8)
 
        if root is not None:
            self.ax.plot(root, 0, marker="o", color="red",  label=f"Корінь: {root:.6f}")
 
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.grid(True, alpha=0.5)
        self.ax.legend()
        self.fig.tight_layout()
        self.canvas.draw()
 
    def calculate(self):
        a_text = self.a_entry.text().strip()
        b_text = self.b_entry.text().strip()
        e_text = self.e_entry.text().strip()
 
        try:
            e = float(e_text)
        except ValueError:
            return
 
        if bool(a_text) != bool(b_text):
            return
 
        if a_text and b_text:
            try:
                a, b = float(a_text), float(b_text)
            except ValueError:
                return
        else:
            intervals = find_intervals()
            if not intervals:
                return
            a, b = intervals[0]
 
        if function(a) * function(b) >= 0:
            return
 
        root, steps = newton(a, b, e)
        self.result_label.setText(f"Корінь: {root:.8f}\nКроків: {steps}")
        self.draw_graph(root)
 
 
def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
 
 
if __name__ == "__main__":
    main()
