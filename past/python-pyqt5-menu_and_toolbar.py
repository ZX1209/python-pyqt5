#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a menubar. The
menubar has one menu with an exit action.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: January 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication,QMenu
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initMenu({'a','b','c','d'})
        self.initUI()

    def genMenu(self,menus):
        for menu in menus:
            yield QMenu(menu,self)

        

    
    def initMenu(self,menus):
        # if isinstance(menus,str):
        #     return QMenu(menus,self)
        # else:
        #     for menu in menus:
        #         self.initMenu(menu)
        firstMenu = self.menuBar()
        for menu in menus:
            if isinstance(menu,str):
                firstMenu.addMenu(menu)
            else:




    def initUI(self):

        self.setGeometry(300, 300, 1200, 600)
        self.setWindowTitle('anki-like')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())