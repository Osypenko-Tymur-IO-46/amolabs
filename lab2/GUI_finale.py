from PyQt5.QtWidgets import * 
import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtCore import Qt
import alg
import filegen
import random
import time

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("PyQtGraph")
        #self.setGeometry(100, 100, 600, 500)
        self.UiComponents()
    
    def UiComponents(self):

        widget = QWidget()

        submit = QPushButton("Застосувати")
        clear = QPushButton("Очистити графіки")
        import_btn = QPushButton("Імпортувати з файлу")
        generate = QPushButton("Згенерувати 10 файлів")
        analyse_btn = QPushButton("Запустити аналіз")


        submit.clicked.connect(self.set_vals)
        clear.clicked.connect(self.graph_reset)
        import_btn.clicked.connect(self.import_from_file)
        generate.clicked.connect(self.generate_files)
        analyse_btn.clicked.connect(self.run_analysis)

        self.ask_y = QLineEdit()
        self.ask_y.setMaximumWidth(200)

        self.result = QLabel("Введіть масив")
        self.result.setWordWrap(True)
        self.result.setMaximumWidth(200)  # match the QLineEdit width

        self.uPlot = pg.PlotWidget(title="Кількість операцій від довжини масиву")
        self.uPlot.setLabel("left",   "Операції")
        self.uPlot.setLabel("bottom", "Довжина масиву")
        self.uPlot.addLegend()
 
        self.operation_line = self.uPlot.plot([], [], pen=pg.mkPen("#00d4ff", width=2), name="Фактична кількість операцій")
        self.theoretical_line = self.uPlot.plot([], [], pen=pg.mkPen("#ff8c00", width=2, style=Qt.DashLine), name="Теоретична кількість операцій")

        self.sPlot = pg.PlotWidget(title="Час виконання від довжини масиву")
        self.sPlot.setLabel("left",   "Час")
        self.sPlot.setLabel("bottom", "Довжина масиву")
 
        self.time_line = self.sPlot.plot([], [], pen=pg.mkPen("#39ff14", width=2))


        layout = QGridLayout()
        widget.setLayout(layout)

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.uPlot)
        splitter.addWidget(self.sPlot)
        splitter.setSizes([500, 500])

        layout.addWidget(self.ask_y, 0, 0)
        layout.addWidget(submit, 1, 0)
        layout.addWidget(clear, 2, 0)
        layout.addWidget(import_btn, 3, 0)
        layout.addWidget(generate, 4, 0)
        layout.addWidget(analyse_btn,   5, 0)
        layout.addWidget(self.result, 6, 0)
        layout.addWidget(splitter, 0, 1, 7, 1)
        
        
        self.setCentralWidget(widget)

    def run_analysis(self):
        sizes = list(range(1000, 6000, 1000))
        avg_steps = []
        avg_times = []
    
        for n in sizes:
            step_total = 0
            time_total = 0.0
            for i in range(5):
                data = [random.randint(-10000, 10000) for j in range(n)]
                t = time.perf_counter()
                steps = alg.sort(data)
                time_total += time.perf_counter() - t
                step_total += steps
            avg_steps.append(step_total / 5)
            avg_times.append(time_total / 5)
    
        theoretical_value = [n ** 2 for n in sizes]
        scale = avg_steps[-1] / theoretical_value[-1]
        theoretical_scaled = [v * scale for v in theoretical_value]
    
        self.operation_line.setData(sizes, avg_steps)
        self.theoretical_line.setData(sizes, theoretical_scaled)
        self.time_line.setData(sizes, avg_times)

        
    def set_vals(self):
        y = list(map(int, self.ask_y.text().split()))
        alg.sort(y)
        self.result.setText(' '.join(str(v) for v in y))


    def generate_files(self):
            filegen.generate()


    def graph_reset(self):
        self.operation_line.setData([], [])
        self.theoretical_line.setData([], [])
        self.time_line.setData([], [])
        self.ask_y.clear()
        self.result.setText("Введіть масив")


    def import_from_file(self):
        file_path, j = QFileDialog.getOpenFileName(self, "Open file", "", "Text Files (*.txt);;All Files (*)")
        if not file_path:
            return

        try:
            with open(file_path, 'r') as f:
                content = f.read()
            numbers = list(map(int, content.split()))
            self.ask_y.setText(' '.join(str(n) for n in numbers))
            self.set_vals()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not read file:\n{e}")

    def graph_reset(self):
        self.operation_line.setData([], [])
        self.theoretical_line.setData([], [])
        self.time_line.setData([], [])
        self.ask_y.clear()
        self.result.setText("Введіть масив")


def main():
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()