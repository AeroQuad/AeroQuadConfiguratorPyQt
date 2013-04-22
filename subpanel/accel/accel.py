'''
Created on 22 apr. 2013

@author: Erik
'''

from PyQt4 import QtCore, QtGui
from subpanel.subPanel import SubPanel
from subpanel.accel.accelWindow import Ui_Form


class accel(QtGui.QWidget, SubPanel):


    def __init__(self):
        QtGui.QWidget.__init__(self)
        SubPanel.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        pictureScene = QtGui.QGraphicsScene()
        pictureBackground = QtGui.QPixmap("./resources/calfront.png")
        pictureItem = QtGui.QGraphicsPixmapItem(pictureBackground)
        pictureScene.addItem(pictureItem)
        self.ui.picture.setScene(pictureScene)
        