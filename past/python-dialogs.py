#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we reimplement an 
event handler. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication,QPushButton,QDialog,QGridLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        
        layout = QGridLayout()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')


        tmp1 = QPushButton(self)
        tmp1.setText("tmp1")

        tmp2 = QPushButton(self)
        tmp2.setText("tmp2")

        tmp3 = QPushButton(self)
        tmp3.setText("tmp3")

        layout.addWidget(tmp1,0,0,1,2)

        self.show()


    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())