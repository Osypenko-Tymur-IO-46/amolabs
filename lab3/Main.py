import sys
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

from window1 import Window1 
from window2 import Window2

 
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Меню")
        self.setFixedSize(200, 100)
        self.win1 = None
        self.win2 = None
        self.UiComponents()
 
    def UiComponents(self):
        widget = QWidget()

        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignCenter)
 
        btn_sin = QPushButton("sin(x)")
        btn_sin.clicked.connect(self.open_window1)
        layout.addWidget(btn_sin)
 
        btn_var = QPushButton("1/(1+e^(-x))")
        btn_var.clicked.connect(self.open_window2)
        layout.addWidget(btn_var)
 
        self.setCentralWidget(widget)
 
    def open_window1(self):
        if self.win1 is None or not self.win1.isVisible():
            self.win1 = Window1()
        self.win1.show()

 
    def open_window2(self):
        if self.win2 is None or not self.win2.isVisible():
            self.win2 = Window2()
        self.win2.show()
 
 
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 
 
if __name__ == "__main__":
    main()
