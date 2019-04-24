# -*- coding: utf-8 -*-
# done: 可以选择轮廓或线的颜色、线性、填充色等
# DONE: 可以打开并浏览图片文件
from pathlib import Path

import sys
from PyQt5.QtWidgets import (
    QFileDialog,
    QSpinBox,
    QColorDialog,
    QGridLayout,
    QPushButton,
    QFrame,
    QComboBox,
    QLabel,
    QApplication,
    QWidget,
    QMainWindow,
    QAction,
    qApp,
    QHBoxLayout,
)
from PyQt5.QtGui import QPainter, QPixmap, QPen, QBrush, QIcon, QPalette
from PyQt5.QtCore import Qt, QPoint

import logging

from PIL import Image

from enum import IntEnum

# tag: import here

logging.basicConfig(level=logging.DEBUG)

logging.debug("this is a debug message")

cwd = Path.cwd()
resourcesDir = cwd / "resources"
iconsDir = resourcesDir / "icons"

MinimunHeight = 400
MinimunWidth = 400

DefaultPenColor = Qt.red
DefaultBrushColor = Qt.red
DefaultPenSize = 10
DefaultBrushStyle = Qt.NoBrush

# enum of shape


class shape(IntEnum):
    Point = 0
    Line = 1
    Rectangle = 2
    Ellipse = 3


class PaintArea(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.shape = shape.Point
        self.pen = QPen(DefaultPenColor, DefaultPenSize)
        self.brush = QBrush(DefaultBrushColor, DefaultBrushStyle)
        self.fillrule = Qt.OddEvenFill

        self.lastPoint = QPoint(-10, -10)
        self.endPoint = QPoint(-10, -10)

        self.drawItems = []
        self.pix = QPixmap(self.width(), self.height())
        self.pix.fill(Qt.white)

        # 有什么用?
        # self.setPalette(QPalette(Qt.white))
        # self.setAutoFillBackground(True)
        # TODO: width,Height or reverse?
        self.setMinimumSize(MinimunWidth, MinimunHeight)

    def initPoint(self):
        self.lastPoint = QPoint(-10, -10)
        self.endPoint = QPoint(-10, -10)

    def setShape(self, shape):
        self.shape = shape
        self.initPoint()
        self.update()

    def setPen(self, pen):
        self.pen = pen
        self.initPoint()
        self.update()

    def setBrush(self, brush):
        self.brush = brush
        self.initPoint()
        self.update()

    def setFilRule(self, fillrule):
        self.fillrule = fillrule
        self.initPoint()
        self.update()

    def paintEvent(self, e):
        # 到 pixmap 的painter
        qp = QPainter(self.pix)
        qp.setPen(self.pen)
        qp.setBrush(self.brush)

        logging.debug((self.shape, self.shape == shape.Line))

        if self.shape == shape.Point:
            # 根据鼠标指针前后两个位置绘制直线
            qp.drawLine(self.lastPoint, self.endPoint)
            # 让前一个坐标值等于后一个坐标值，
            # 这样就能实现画出连续的线
            self.lastPoint = self.endPoint

            # 到屏幕上的painter
            painter = QPainter(self)
            # 绘制画布到窗口指定位置处
            painter.drawPixmap(0, 0, self.pix)

            return None

        elif self.shape == shape.Line:
            if self.lastPoint and self.endPoint:
                qp.drawLine(self.lastPoint, self.endPoint)
        elif self.shape == shape.Rectangle:
            if self.lastPoint and self.endPoint:
                qp.drawRect(
                    self.lastPoint.x(),
                    self.lastPoint.y(),
                    self.endPoint.x() - self.lastPoint.x(),
                    self.endPoint.y() - self.lastPoint.y(),
                )
        elif self.shape == shape.Ellipse:
            if self.lastPoint and self.endPoint:
                qp.drawEllipse(
                    self.lastPoint.x(),
                    self.lastPoint.y(),
                    self.endPoint.x() - self.lastPoint.x(),
                    self.endPoint.y() - self.lastPoint.y(),
                )
        # 到屏幕上的painter
        painter = QPainter(self)
        # 绘制画布到窗口指定位置处
        painter.drawPixmap(0, 0, self.pix)

        self.initPoint()

    def mousePressEvent(self, event):
        # 鼠标左键按下
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint

    def mouseMoveEvent(self, event):
        # 鼠标左键按下的同时移动鼠标
        if event.buttons() and Qt.LeftButton and self.shape == shape.Point:
            self.endPoint = event.pos()
            # 进行重新绘制
            self.update()

    def mouseReleaseEvent(self, event):
        # 鼠标左键释放
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # 进行重新绘制
            self.update()


class MainWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.paintArea = PaintArea()

        # 4
        self.shapeLabel = QLabel("形状: ")
        comboxItems = [
            ["Point", shape.Point],
            ["Line", shape.Line],
            ["Rectangle", shape.Rectangle],
            ["Ellipse", shape.Ellipse],
        ]
        self.shapeComboBox = QComboBox()
        for comboxItem in comboxItems:
            self.shapeComboBox.addItem(*comboxItem)
        # 连接
        self.shapeComboBox.activated.connect(self.paintArea.setShape)

        self.penColorLabel = QLabel("画笔颜色: ")
        self.penColorFrame = QFrame()
        self.penColorFrame.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.penColorFrame.setAutoFillBackground(True)
        self.penColorFrame.setPalette(QPalette(DefaultPenColor))
        self.penColorBtn = QPushButton("更改")
        self.penColorBtn.clicked.connect(self.setPenColor)

        self.penWidthLabel = QLabel("画笔宽度: ")
        self.penWidthSpinBox = QSpinBox()
        self.penWidthSpinBox.setRange(0, 20)
        self.penWidthSpinBox.setValue(DefaultPenSize)
        self.penWidthSpinBox.valueChanged.connect(self.setPenWidth)

        self.penStyleLabel = QLabel("画笔风格: ")
        self.penStyleComboBox = QComboBox()

        # TODO: functionlize
        styleItems = [
            ["SolidLine", int(Qt.SolidLine)],
            ["DashLine", int(Qt.DashLine)],
            ["DotLine", int(Qt.DotLine)],
            ["DashDotLine", int(Qt.DashDotLine)],
            ["DashDotDotLine", int(Qt.DashDotDotLine)],
            ["CustomDashLine", int(Qt.CustomDashLine)],
        ]
        for styleItem in styleItems:
            self.penStyleComboBox.addItem(*styleItem)

        self.penStyleComboBox.activated.connect(self.setPenStyle)

        self.penCapLabel = QLabel("画笔顶帽: ")
        self.penJoinLabel = QLabel("画笔连接点:  ")
        self.fillRuleLavel = QLabel("填充模式: ")
        self.fillRuleComboBox = QComboBox()
        self.fillRuleComboBox.addItem("Odd Even", Qt.OddEvenFill)
        self.fillRuleComboBox.addItem("Winding", Qt.WindingFill)
        self.fillRuleComboBox.activated.connect(self.setFillRule)

        self.brushColorLabel = QLabel("画刷颜色: ")
        self.brushColorFrame = QFrame()
        self.brushColorFrame.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.brushColorFrame.setAutoFillBackground(True)
        self.brushColorFrame.setPalette(QPalette(DefaultPenColor))
        self.brushColorBtn = QPushButton("更改")
        self.brushColorBtn.clicked.connect(self.setBrushColor)

        self.brushStyleLabel = QLabel("画刷风格: ")
        self.brushStyleComboBox = QComboBox()

        brushStyleItems = [
            ["NoBrush", int(Qt.NoBrush)],
            ["SolidPattern", int(Qt.SolidPattern)],
            ["Dense1Pattern", int(Qt.Dense1Pattern)],
            ["Dense2Pattern", int(Qt.Dense2Pattern)],
            ["Dense3Pattern", int(Qt.Dense3Pattern)],
            ["Dense4Pattern", int(Qt.Dense4Pattern)],
            ["Dense5Pattern", int(Qt.Dense5Pattern)],
            ["Dense6Pattern", int(Qt.Dense6Pattern)],
            ["Dense7Pattern", int(Qt.Dense7Pattern)],
            ["HorPattern", int(Qt.HorPattern)],
            ["VerPattern", int(Qt.VerPattern)],
            ["CrossPattern", int(Qt.CrossPattern)],
            ["BDiagPattern", int(Qt.BDiagPattern)],
            ["FDiagPattern", int(Qt.FDiagPattern)],
            ["DiagCrossPattern", int(Qt.DiagCrossPattern)],
            ["LinearGradientPattern", int(Qt.LinearGradientPattern)],
            ["ConicalGradientPattern", int(Qt.ConicalGradientPattern)],
            ["RadialGradientPattern", int(Qt.RadialGradientPattern)],
            ["TexturePattern", int(Qt.TexturePattern)]
        ]
        for styleItem in brushStyleItems:
            self.brushStyleComboBox.addItem(*styleItem)

        self.brushStyleComboBox.activated.connect(self.setBrushStyle)

        self.selectPicBtn = QPushButton("选择图片")
        self.selectPicBtn.clicked.connect(self.openPic)

        # tag: create and set widgets
        self.cleanBtn = QPushButton("清屏")
        self.cleanBtn.clicked.connect(self.cleanAll)
        # 3

        # 2

        # left area gen
        self.rightLayout = QGridLayout()
        rightWidgets = [
            [self.shapeLabel, self.shapeComboBox],
            [self.penColorLabel, self.penColorFrame, self.penColorBtn],
            [self.penWidthLabel, self.penWidthSpinBox],
            [self.fillRuleLavel, self.fillRuleComboBox],
            [self.penStyleLabel, self.penStyleComboBox],
            [self.brushColorLabel, self.brushColorFrame, self.brushColorBtn],
            [self.brushStyleLabel, self.brushStyleComboBox],
            [self.cleanBtn],
            [self.selectPicBtn],
        ]
        # tag: add and show widgets
        for r in range(len(rightWidgets)):
            for c in range(len(rightWidgets[r])):
                self.rightLayout.addWidget(rightWidgets[r][c], r, c)
        # 1
        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.addWidget(self.paintArea)
        self.mainLayout.addLayout(self.rightLayout)

        #
        self.mainLayout.setStretchFactor(self.paintArea, 1)
        self.mainLayout.setStretchFactor(self.rightLayout, 0)

    def setPenColor(self):

        tmpColor = QColorDialog.getColor()
        self.penColorFrame.setPalette(QPalette(tmpColor))
        self.paintArea.initPoint()
        self.paintArea.pen.setColor(tmpColor)  # use this

    def setPenWidth(self, value):
        tmpWidth = value
        self.paintArea.initPoint()

        self.paintArea.pen.setWidth(tmpWidth)

    def setFillRule(self, value):
        rule = Qt.FillRule(
            int(
                self.fillRuleComboBox.itemData(
                    self.fillRuleComboBox.currentIndex(), Qt.UserRole)))
        self.paintArea.setFilRule(rule)

    def setPenStyle(self, value):
        style = Qt.PenStyle(
            int(self.penStyleComboBox.itemData(value, Qt.UserRole)))
        self.paintArea.initPoint()
        self.paintArea.pen.setStyle(style)

    def openPic(self):
        name = QFileDialog.getOpenFileName(self, "打开", "/", "*")

        self.paintArea.pix = QPixmap(name[0])

    def setBrushColor(self):
        """setBrushColor
        """
        tmpColor = QColorDialog.getColor()
        self.brushColorFrame.setPalette(QPalette(tmpColor))
        self.paintArea.initPoint()
        self.paintArea.brush.setColor(tmpColor)  # use this

    def setBrushStyle(self, value):
        """setBrushStyle
        """
        style = Qt.BrushStyle(
            int(self.brushStyleComboBox.itemData(value, Qt.UserRole)))
        self.paintArea.initPoint()
        self.paintArea.brush = QBrush(style)

    # tag: next func
    def cleanAll(self):
        """should i do this?
        """
        self.paintArea.pix.fill(Qt.white)
        self.paintArea.initPoint()
        self.paintArea.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWidget()
    form.show()
    sys.exit(app.exec_())
