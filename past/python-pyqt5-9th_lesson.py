import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class QsplitterMain(QSplitter):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        listWs = QListWidget(self)

        listWs.insertItem(0,"1")
        listWs.insertItem(1,"2")
        listWs.insertItem(2,"3")

        content = Content()
        self.addWidget(content)

        listWs.currentRowChanged.connect(content.sw.setCurrentIndex)


        self.setMinimumSize(self.minimumSize())
        self.setMaximumSize(self.maximumSize())

        self.setWindowTitle('修改用户资料')
        self.show()


class PlaceWidget(QWidget):

    def __init__(self,PlaceHolderName="default"):
        super().__init__()
        tmp = QLabel(PlaceHolderName,self)
        self.setStyleSheet("color:white;background-color:black;background:yellow;border-color:red;")


class Content(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.sw = QStackedWidget(self)

        self.sw.setFrameStyle(QFrame.Panel|QFrame.Raised)

        a = PlaceWidget("a")
        b = PlaceWidget("b")
        c = PlaceWidget("c")

        self.sw.addWidget(a);
        self.sw.addWidget(b);
        self.sw.addWidget(c);

        AmendBtn = QPushButton("修改")

        CloseBtn = QPushButton("关闭")

        btnLayout = QHBoxLayout()

        btnLayout.addStretch(1)

        btnLayout.addWidget(AmendBtn)
        
        btnLayout.addWidget(CloseBtn)

        rLayout = QVBoxLayout(self)

        rLayout.setSpacing(6)
        rLayout.addWidget(self.sw)
        rLayout.addLayout(btnLayout)
        



if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet("QStackedWidget{background-color:yellow;}")
    # font = QFont("yahei",12) # 字体名?



    ex = QsplitterMain()
    sys.exit(app.exec_())