import sys
import numpy as np
import pandas as pd
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
            self.week_count_student()

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
        ax = self.fig.add_subplot(111) #1X1그리드에 첫번째 subplot
        ax.set_ylim(0, 10)  #y축의 최대,최솟값 설정
        rects=ax.bar(row, column, label="student")

        ax.set_xlabel("date")

        ax.set_title("Student")
        ax.legend()

        self.canvas.draw()
        for i, rect in enumerate(rects):
            ax.text(rect.get_x() + rect.get_width() / 2.0, 1.05 * rect.get_height(), str(column[i]) ,
                    ha='center')

    def week_count_student(self):  # 주별 그래프
        df = pd.read_csv(open("today_student.txt", "rb"), delimiter='\t')
        df.columns = ['date', 'cnt']

        df['datetime'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y-%m-%d'))
        df.set_index(df['datetime'], inplace=True)
        df = df.drop('datetime', 1)

        weekly_df = df['cnt'].resample('W-Fri').sum().fillna(0)
        print(weekly_df) #그 주의 금요일 날짜와 총합이 나옴
        print(weekly_df.values) #주별 합계들이 나옴

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        rects = ax.bar(weekly_df.index, weekly_df.values, label="student")
        ax.set_xlabel("week")
        ax.set_title("Student")
        ax.legend()

        self.canvas.draw()
        for i, rect in enumerate(rects):
            ax.text(rect.get_x() + rect.get_width() / 2.0, 1.05 * rect.get_height(), str(weekly_df.values[i]),
                    ha='center')

    def center(self): #화면 가운데에 띄우기 위해서
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.center()
    window.show()
    app.exec_()