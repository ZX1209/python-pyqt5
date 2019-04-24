#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we draw text in Russian Cylliric.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class PlaceWidget(QWidget):

    def __init__(self,PlaceHolderName="default"):
        super().__init__()
        tmp = QLabel(PlaceHolderName,self)
        # self.setStyleSheet("color:white;background-color:black;background:yellow;border-color:red;")
        self.show()

class PaintArea(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        b = PlaceWidget()
        c = PaintWidget()
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(b)
        hbox.addWidget(c)
        self.setLayout(hbox)

        self.setWindowTitle('Drawing text')
        self.show()



class PaintWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.text = "something\nlike this"

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("drawing")
        self.show()

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()


    def drawText(self, event, qp):

        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = PaintWidget()
    sys.exit(app.exec_())