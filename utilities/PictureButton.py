'''
Created on Mar 4, 2013

@author: Ted Carancho
'''

from PyQt4 import QtGui, QtCore

class PictureButton(QtGui.QLabel):
    ''' This class creates a clickable picture button.
    '''
    def __init__(self, parent):
        QtGui.QLabel.__init__(self, parent)
    
    def mouseReleaseEvent(self, event):
        self.emit(QtCore.SIGNAL('clicked()'))