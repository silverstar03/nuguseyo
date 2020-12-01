import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import subprocess

class start(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.title = QLabel("누구세요", self)
        self.title.move(250, 100)
        self.title.resize(400, 100)
        self.title.setFont(QtGui.QFont('나눔바른고딕', 60))
        # 폰트 사이즈, 폰트 지정

        self.startBtn = QPushButton('시작', self)
        self.startBtn.move(320, 260)
        self.startBtn.resize(150, 50)
        self.startBtn.clicked.connect(self.startBtn_clicked)

        self.graphBtn = QPushButton('그래프 보기', self)
        self.graphBtn.move(320, 320)
        self.graphBtn.resize(150, 50)
        self.graphBtn.clicked.connect(self.graphBtn_clicked)

        self.setWindowTitle("시작화면")
        self.resize(800, 500)
        self.show()

    def startBtn_clicked(self):
        subprocess.call("StudentUI.py", shell=True)

    def graphBtn_clicked(self):
        subprocess.call("Graph.py", shell=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = start()

    sys.exit(app.exec_())