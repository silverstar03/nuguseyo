import sys

from PySide2 import QtGui
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel

# from Pyside2 import QtCore

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(800, 500)
    w.setWindowTitle("시작화면")

    title = QLabel("누구세요", w)
    title.move(250, 70)
    title.resize(400, 100)
    title.setFont(QtGui.QFont('나눔바른고딕', 60))
    # 폰트 사이즈, 폰트 지정

    startBtn = QPushButton('시작', w)
    startBtn.move(320, 250)
    startBtn.resize(150, 50)
    # 시작 버튼 누르면 이름 입력 받기

    managerBtn = QPushButton('그래프 보기', w)
    managerBtn.move(320, 350)
    managerBtn.resize(150, 50)
    # 장기간 단기간?

    w.show()

    sys.exit(app.exec_())