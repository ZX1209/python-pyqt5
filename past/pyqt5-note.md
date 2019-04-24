# status bar
```py
self.statusBar().showMessage('Ready')

exitAct.setStatusTip('Exit application')
```

# toolbar
```py
    def genToolBar(self,Actions):
        self.toolbar = self.addToolBar('autoGenToolBar')
        for Action in Actions:
            self.toolbar.addAction(self.genAction(*Action))



    def genAction(self,iconPath,iconTitle,connectedFunc=None,shortCut=None):
        tmpAct =  QAction(QIcon(iconPath),iconTitle,self)

        if shortCut: tmpAct.setShortcut(shortCut)
        if connectedFunc: tmpAct.triggered.connect(connectedFunc)

        return tmpAct
    #...
        # init toolbor
        Actions = [
            [str(iconsDir / 'rect.png'),'rect'],
            [str(iconsDir / 'brush.png'),'brush'],
            [str(iconsDir / 'circle.png'),'circle'],
            [str(iconsDir / 'line.png'),'line'],
            [str(iconsDir / 'pencil.png'),'pencil'],
            [str(iconsDir / 'picture.png'),'picture'],
            [str(iconsDir / 'font.png'),'font'],
        ]
        self.genToolBar(Actions)
```


# left click meau
```py
    def contextMenuEvent(self, event):

           cmenu = QMenu(self)

           newAct = cmenu.addAction("New")
           opnAct = cmenu.addAction("Open")
           quitAct = cmenu.addAction("Quit")
           action = cmenu.exec_(self.mapToGlobal(event.pos()))

           if action == quitAct:
               qApp.quit()
```



# meau
toplevel:  menubar = self.menuBar()
nextlevel : fileMenu = menubar.addMenu('File')
lastlevel :         fileMenu.addAction(newAct) or fileMenu.addMenu(impMenu)
```py
```


# layout
```py

self.mainLayout = QHBoxLayout(self)

self.mainLayout.setStretchFactor(self.paintArea,1)
```


# slot and signal
```py
sld.valueChanged.connect(lcd.display)

```