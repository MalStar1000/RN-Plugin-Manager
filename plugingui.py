# A window test.

import os
import struct
import sys
import traceback
import zipfile
global self

from PyQt5 import QtCore, QtGui, QtWidgets, uic
Qt = QtCore.Qt

class Window(QtWidgets.QMainWindow):
    """Main Window"""
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, None)
        super(Window, self).__init__(parent)
        uic.loadUi('pluginguithing.ui', self)
        self.gameButton.setChecked(True)

        self.convert.clicked.connect(self.button_click)

    def button_click(self):
        # shost is a QString object
        shost = self.inputFolder.text()
        def zip(path, zip):
            for root, dirs, files in os.walk(folderdir):
                for file in files:
                    zip.write(os.path.join(root, file))
        self.gameButton.toggled.connect(self.gameClick)
        self.transButton.toggled.connect(self.transClick)
        self.themeButton.toggled.connect(self.themeClick)
        print(shost)
    def gameClick(self):
        self.type = "game"
    def transClick(self):
        self.type = "trans"
    def themeClick(self):
        self.type = "theme"

if __name__ == '__main__':
    if type == "game":
        zipf = zipfile.ZipFile(os.path.basename(folderdir[:-1]) + '.rngame', 'w')
        zipdir = ('tmp/', zipf)
        zipf.close()
    elif type == "trans":
        zipf = zipfile.ZipFile(os.path.basename(folderdir[:-1]) + '.rntrans', 'w')
        zipdir = ('tmp/', zipf)
        zipf.close()
    elif type == "theme":
        zipf = zipfile.ZipFile(os.path.basename(folderdir[:-1]) + '.rntheme', 'w')
        zipdir = ('tmp/', zipf)
        zipf.close()
    else:
        uic.loadUi('pluginguithing.ui', self)
    global app, window
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())






