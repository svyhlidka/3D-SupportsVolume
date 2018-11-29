from PyQt5.QtWidgets import * #QWidget, QApplication, QFrame, QMessageBox, QLabel, QDesktopWidget,  QMainWindow, QDialog
import sys, random
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, pyqtSlot
from PyQt5.QtGui import *
import winsound         # for sound  
import time             # for sleep
#app = QApplication(sys.argv)


class MyReader():
    
   
    def load_file(self,path):
        lines = [line.replace("vertex","").strip().split(' ') for line in open(path) if "vertex" in line]
        lines1 = []
        lines1 = [[float(line[0]), float(line[1]), float(line[2])] for line in lines]
        for i in range(10):
            print(lines1[i])
        dict = {}
        for item in lines1:
            if not (item[0],item[1]) in dict: dict.update({(item[0],item[1]):item[2]})
            if (item[0],item[1]) in dict and item[2] > dict[(item[0],item[1])]: dict[(item[0],item[1])]=item[2]
        #dict1 = {{(item[0],item[1]):item[2]} for item in lines1}
        #dict1={{(item[0],item[1]):item[2]} if not (item[0],item[1]) in dict else dict[(item[0],item[1])]=item[2] for item in lines1 }
        print(len(lines1),len(dict)) #,len(dict1))

x = MyReader()
x.load_file(r"C:/3D/Petr/Cube_for_support_ASCII.stl")