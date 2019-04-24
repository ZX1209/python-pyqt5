from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog,QColorDialog,QApplication,QTextEdit,QFontDialog,QDialog,QWidget,QPushButton,QMainWindow
from PyQt5.QtPrintSupport import QPageSetupDialog,QPrintDialog,QPrinter
from PyQt5.QtGui import QIcon
import sys

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.te=QTextEdit(self)
        self.setCentralWidget(self.te)
        self.setGeometry(0,0,400,400)
        self.statusBar().showMessage('Ready')


if __name__ == "__main__":
    ap=QApplication(sys.argv)
    example=TextEditor()
    example.show()
    sys.exit(ap.exec_())
