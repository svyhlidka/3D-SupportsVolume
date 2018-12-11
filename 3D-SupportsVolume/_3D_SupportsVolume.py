from PyQt5.QtWidgets import * #QWidget, QApplication, QFrame, QMessageBox, QLabel, QDesktopWidget,  QMainWindow, QDialog
import sys, random
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, pyqtSlot
from PyQt5.QtGui import *
import winsound         # for sound  
import time             # for sleep
#app = QApplication(sys.argv)


class Triangle():
    def __init__(self, row, facet, vertex1, vertex2, vertex3):
        self.row = row
        self.facet = facet
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3



class MyReader():
    
   
    def load_file(self,path):
       # all = [line for line in open(path)]
       # print(all)
        all_triangles = {}
        file = open(path,"r")
        i = 1
        j = 0
    #    d=[float(x) for x in (t.strip().split(" "))]
        lines = []
        for line in file:
            if "vertex" in str(line): 
 #               lines.append(((str(i) + line.replace("vertex","")).strip().split(' ')))
                lines.append([float(x) for x in ((str(i) + line.replace("vertex","")).strip().split(' '))])
            if "endfacet" in str(line): i +=1
        file.close
        maxX = 0.0
        minX = 10000000.0
        maxY = 0.0
        minY = 10000000.0
        maxZ = 0.0
        minZ = 10000000.0
        triangles = []

        file = open(path,"r")
        line=file.readline()
        while True:
            if "facet normal" in line:
                tline = []
                tline.append([float(x) for x in (line.replace("facet normal","")).strip().split(' ')]) # facet normal
                line=file.readline()  # outer loop
                for i in range(0,3):
                    line=file.readline()
                    tline.append([float(x) for x in (line.replace("vertex","")).strip().split(' ')]) # vertex
 #               print(tline)
                triangles.append(tline)
            line = file.readline()
            if not line: break
        file.close()


        for item in lines: 
            if item[1] > maxX: maxX = item[1]
            if item[2] > maxY: maxY = item[2]
            if item[3] > maxZ: maxZ = item[3]
            if item[1] < maxX: minX = item[1]
            if item[2] < maxY: minY = item[2]
            if item[3] < maxZ: minZ = item[3]

        print(minX, minY, minZ, "  >   ", maxX, maxY, maxZ)


        maxX = 0.0
        minX = 10000000.0
        maxY = 0.0
        minY = 10000000.0
        maxZ = 0.0
        minZ = 10000000.0

        for item in triangles: 
            for i in range(1,4):
              if item[i][0] > maxX: maxX = item[i][0]
              if item[i][1] > maxY: maxY = item[i][1]
              if item[i][2] > maxZ: maxZ = item[i][2]
              if item[i][0] < maxX: minX = item[i][0]
              if item[i][1] < maxY: minY = item[i][1]
              if item[i][2] < maxZ: minZ = item[i][2]
        print(minX, minY, minZ, "  >   ", maxX, maxY, maxZ)

        dict = {}
        i_list = []
        x=0
        for item in lines:
#            [0] = i;  [1] = x; [2] = y; [3] = z
#            dict{(x,y):(i,z)}
            if not (item[1],item[2]) in dict and float(item[3]) > minZ: dict.update({(item[1],item[2]):(item[0],item[3])})
            if     (item[1],item[2]) in dict and item[3] > dict[(item[1],item[2])][1]: dict[(item[1],item[2])]=(item[0],item[3])
        for item in dict: i_list.append(int(dict[item][0]))
            

        final = []
        x=0

        ##############  tady test trojuhelniku #########################
#        for item in triangles:
#            vertex i = 1,2,3   [i][0] = x; [i][1] = y; [i][2] = z
#            normal i = 0

 #           if not (item[1],item[2]) in dict and float(item[3]) > minZ: dict.update({(item[1],item[2]):(item[0],item[3])})
  #          if     (item[1],item[2]) in dict and item[3] > dict[(item[1],item[2])][1]: dict[(item[1],item[2])]=(item[0],item[3])
#        final.append(item) or remove(item)  ????
            

#        print(i_list)
        file_r = open(path,"r")
        file_w = open("C:/3D/Petr/TESTN.txt","w")
#        file_z = open("C:/3D/Petr/TESTz.txt","w")
#        file_w.write("solid")
        i = 1

        for line in file_r:
#            print(i,line)
#            print(line.strip().split(' '))
            if i in (i_list):
#               file_z.write(str(i)+'\n')
               file_w.write(line)
            if "endfacet" in line: i += 1
        if not "endsolid" in line: file.write_w("endsolid")
        file_w.close()
        file_r.close()
#        file_z.close()
        print(i,len(i_list))
        print(minX, minY, minZ, "  >   ", maxX, maxY, maxZ)
        for i in range(1,10):
            print(triangles[i])

class Reader2():
    
    def save_file(self, path, block):
        file_w = open(path,"w")
        file_w.write("solid")
        file_w.write("\n")
        for item in block:
            str = "facet normal " + "{:.8f}".format(item[0][0]) + " " +"{:.8f}".format(item[0][1]) + " " + "{:.8f}".format(item[0][2]) + "\n"
            file_w.write(str)
            file_w.write("outer loop")
            file_w.write("\n")
            str = "vertex " + "{:.8f}".format(item[1][0]) + " " +"{:.8f}".format(item[1][1]) + " " + "{:.8f}".format(item[1][2]) + "\n"
            file_w.write(str)
            str = "vertex " + "{:.8f}".format(item[2][0]) + " " +"{:.8f}".format(item[2][1]) + " " + "{:.8f}".format(item[2][2]) + "\n"
            file_w.write(str)
            str = "vertex " + "{:.8f}".format(item[3][0]) + " " +"{:.8f}".format(item[3][1]) + " " + "{:.8f}".format(item[3][2]) + "\n"
            file_w.write(str)
            file_w.write("end loop")
            file_w.write("\n")
            file_w.write("endfacet")
            file_w.write("\n")
            file_w.write("endsolid")
            file_w.write("\n")
        file_w.close()


    def load_file(self,path):
       # all = [line for line in open(path)]
       # print(all)
        all_triangles = {}
        file = open(path,"r")
        i = 1
        j = 0
        xx = 0
    #    d=[float(x) for x in (t.strip().split(" "))]
        lines = []
        triangles = []
        maxX = 0.0
        minX = 10000000.0
        maxY = 0.0
        minY = 10000000.0
        maxZ = 0.0
        minZ = 10000000.0


        file = open(path,"r")
        line=file.readline()
        while True:
            if "facet normal" in line:
                tline = []
                tline.append([float(x) for x in (line.replace("facet normal","")).strip().split(' ')]) # facet normal
                line=file.readline()  # outer loop
                for i in range(1,4):
                    line=file.readline() # reading vertex
                    tline.append([float(x) for x in (line.replace("vertex","")).strip().split(' ')]) 
                    if tline[i][0] > maxX: maxX = tline[i][0]
                    if tline[i][1] > maxY: maxY = tline[i][1]
                    if tline[i][2] > maxZ: maxZ = tline[i][2]
                    if tline[i][0] < maxX: minX = tline[i][0]
                    if tline[i][1] < maxY: minY = tline[i][1]
                    if tline[i][2] < maxZ: minZ = tline[i][2]
                if tline[0][2] > 0.001:
  #                 print(tline)
  #                 print(tline[0][2])
                   triangles.append(tline)
                   xx += 1
            line = file.readline()
            if not line: break
        file.close()
        print("total:", xx)
        print(minX, minY, minZ, "  >   ", maxX, maxY, maxZ)
        return triangles



x = Reader2()
block = x.load_file(r"C:/3D/Petr/TEST.stl")
x.save_file("C:/3D/Petr/XXX.stl", block)