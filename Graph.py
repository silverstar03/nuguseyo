import sys
import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setLayout(self.layout)
        self.setGeometry(200, 200, 800, 600)

    def initUI(self):
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        cb = QComboBox()
        cb.addItem('일별')
        cb.addItem('주별')
        cb.activated[str].connect(self.onComboBoxChanged)
        layout.addWidget(cb)
        self.layout = layout
        self.onComboBoxChanged(cb.currentText())

    def onComboBoxChanged(self, text):
        if text == '일별':
            self.day_count_student()
        elif text == '주별':
            self.doGraph2()

    def day_count_student(self):  # 일별 그래프
        with open('today_student.txt', 'r', encoding='utf8') as f:
            data = f.readlines()

        row = []
        column = []
        for line in data:
            li = line.split('\t')
            row.append(li[0])
            column.append(int(li[1]))

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_ylim(0, 10)
        rects=ax.bar(row, column, label="student")

        ax.set_xlabel("date")

        ax.set_title("Student")
        ax.legend()

        self.canvas.draw()
        for i, rect in enumerate(rects):
            ax.text(rect.get_x() + rect.get_width() / 2.0, 1.05 * rect.get_height(), str(column[i]) ,
                    ha='center')


    def doGraph2(self):  # 주별 그래프
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()