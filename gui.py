from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import  QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

_WIDTH = 640
_HEIGTH = 480

class Canvas(QtWidgets.QLabel):
    
    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(_WIDTH, _HEIGTH)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CNC")
        self.main_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        drawing_space = Canvas()
        
        self.right_layout.addWidget(drawing_space)
        self.input_area = QTextEdit()
        self.send_button = QPushButton("Send")


        self.left_layout.addWidget(self.text_area)
        self.left_layout.addWidget(self.input_area)
        self.left_layout.addWidget(self.send_button)

        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)
        self.setLayout(self.main_layout)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(100, 100, 400, 400)
    window.showMaximized()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()