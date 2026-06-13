import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from gauss import gauss_algorithm
 
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.build_ui()
 
    def build_ui(self):
        layout = QVBoxLayout(self)
 
        layout.addWidget(QLabel("Введіть коефіцієнти матриці:"))
 
        grid = QGridLayout()
        self.coef = []
        self.free = []
 
        for i in range(4):
            row = []
            for j in range(4):
                e = QLineEdit()
                e.setFixedWidth(55)
                e.setAlignment(Qt.AlignCenter)
                grid.addWidget(e, i, j)
                row.append(e)
            self.coef.append(row)
 
            grid.addWidget(QLabel("="), i, 4)
 
            b = QLineEdit()
            b.setFixedWidth(55)
            b.setAlignment(Qt.AlignCenter)
            grid.addWidget(b, i, 5)
            self.free.append(b)
 
        layout.addLayout(grid)
 
        btn = QPushButton("Обрахувати")
        btn.clicked.connect(self.calculate)
        layout.addWidget(btn)
 
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)
 
    def calculate(self):
        try:
            A = [[float(self.coef[i][j].text()) for j in range(4)] for i in range(4)]
            B = [float(self.free[i].text()) for i in range(4)]
        except ValueError:
            return
 
        x = gauss_algorithm(A, B)
        if x is None:
            self.result_label.setText("Матриця вироджена")
        else:
            self.result_label.setText("\n".join(f"x{i+1} = {v:.4f}" for i, v in enumerate(x)))
 
def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
