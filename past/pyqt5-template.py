#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QMainWindow,
                             QStatusBar, QFileDialog, QColorDialog, QFontDialog, QLabel, QFontComboBox, QComboBox, QSpinBox,QToolBar)


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fontLabel1 = QLabel()
        self.fontLabel2 = QLabel()
        self.fontComboBox = QFontComboBox()
        self.sizeSpinBox = QSpinBox()
        self.fontToolBar = QToolBar()

        self.filename = None
        self.fCurFileName = None


        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = TextEditor()
    sys.exit(app.exec_())
