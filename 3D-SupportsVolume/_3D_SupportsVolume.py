from PyQt5.QtWidgets import * #QWidget, QApplication, QFrame, QMessageBox, QLabel, QDesktopWidget,  QMainWindow, QDialog
import sys, random
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, pyqtSlot
from PyQt5.QtGui import *
import winsound         # for sound  
import time             # for sleep
#app = QApplication(sys.argv)


class MyReader():

    def load_file(self,path):
        self.file = open(path)
        i = 0
        for line in self.file:
            print(line)
            i += 1
            if i > 20: break

x = MyReader()
x.load_file(r"C:/3D/Petr/Cube_for_support_ASCII.stl")