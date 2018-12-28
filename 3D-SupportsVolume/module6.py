import sys, random
import time             # for sleep
import collections
#app = QApplication(sys.argv)


class Triangle():
    def __init__(self, row, facet, vertex1, vertex2, vertex3):
        self.row = row
        self.facet = facet
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3

class Reader():
    
    
    def __init__(self):
        self.maxX = 0.0
        self.minX = 10000000.0
        self.maxY = 0.0
        self.minY = 10000000.0
        self.maxZ = 0.0
        self.minZ = 10000000.0
        self.triangles = []
        self.new_d = {}
        self.total_ops = 0
        self.vol = 0.0


    def save_filedictx(self, path, block):
        file_w = open(path,"w")
        file_w.write("solid ")
        file_w.write("\n")
        for item in block:
#            print("#####################3")
 #           print(item)
  #          print(block[item])
   #         print(block[item][0][1])
    #        print(block[item][1][0][1])
            # item - index
            # block[item] - value
#            str = "facet normal " + "{:.6f}".format(block[item][0][0]) + " " +"{:.6f}".format(block[item][0][1]) + " " + "{:.6f}".format(block[item][0][2]) + "\n"
            str = "facet normal " + "{:.6f}".format(block[item][0][0]) + " " +"{:.6f}".format(block[item][0][1]) + " " + "{:.6f}".format(block[item][0][2]) + "\n"
            file_w.write(str)
            file_w.write("outer loop")
            file_w.write("\n")
#            str = "vertex " + "{:.8f}".format(block[item][1][0][0]) + " " +"{:.8f}".format(block[item][1][0][1]) + " " + "{:.8f}".format(block[item][1][0][2]) + "\n"
#            file_w.write(str)
#            str = "vertex " + "{:.8f}".format(block[item][1][1][0]) + " " +"{:.8f}".format(block[item][1][1][1]) + " " + "{:.8f}".format(block[item][1][1][2]) + "\n"
#            file_w.write(str)
#            str = "vertex " + "{:.8f}".format(block[item][1][2][0]) + " " +"{:.8f}".format(block[item][1][2][1]) + " " + "{:.8f}".format(block[item][1][2][2]) + "\n"
#
            str = "vertex " + "{:.8f}".format(item[2][0][0]) + " " +"{:.8f}".format(item[2][0][1]) + " " + "{:.8f}".format(item[2][0][2]) + "\n"
            file_w.write(str)
            str = "vertex " + "{:.8f}".format(item[2][1][0]) + " " +"{:.8f}".format(item[2][1][1]) + " " + "{:.8f}".format(item[2][1][2]) + "\n"
            file_w.write(str)
            str = "vertex " + "{:.8f}".format(item[2][2][0]) + " " +"{:.8f}".format(item[2][2][1]) + " " + "{:.8f}".format(item[2][2][2]) + "\n"

            file_w.write(str)
            file_w.write("endloop")
            file_w.write("\n")
            file_w.write("endfacet")
            file_w.write("\n")
        file_w.write("endsolid")
        file_w.write("\n")
        file_w.close()

    def save_filedict(self, path, block):
        file_w = open(path,"w")
        file_w.write("solid ")
        file_w.write("\n")
        for item in block:
            # item - index
            # block[item] - value
            str = "facet normal " + "{:.6f}".format(block[item][0][0]) + " " +"{:.6f}".format(block[item][0][1]) + " " + "{:.6f}".format(block[item][0][2]) + "\n"
            file_w.write(str)
            file_w.write("outer loop")
            file_w.write("\n")
            str = "vertex " + "{:.8f}".format(item[0][0]) + " " +"{:.8f}".format(item[0][1]) + " " + "{:.8f}".format(item[0][2]) + "\n"
            file_w.write(str)
            str = "vertex " + "{:.8f}".format(item[1][0]) + " " +"{:.8f}".format(item[1][1]) + " " + "{:.8f}".format(item[1][2]) + "\n"
            file_w.write(str)
            str = "vertex " + "{:.8f}".format(item[2][0]) + " " +"{:.8f}".format(item[2][1]) + " " + "{:.8f}".format(item[2][2]) + "\n"
            file_w.write(str)
            file_w.write("endloop")
            file_w.write("\n")
            file_w.write("endfacet")
            file_w.write("\n")
        file_w.write("endsolid")
        file_w.write("\n")
        file_w.close()

    def save_file(self, path, block):
        file_w = open(path,"w")
        file_w.write("solid ")
        file_w.write("\n")
        # {vertex:x,y,z:facet, s, p}
        for item in block:
            str = "facet normal " + "{:.6f}".format(item[0][0]) + " " +"{:.6f}".format(item[0][1]) + " " + "{:.6f}".format(item[0][2]) + "\n"
            file_w.write(str)
            file_w.write("outer loop")
            file_w.write("\n")
            str = "vertex " + "{:.8f}".format(item[1][0]) + " " +"{:.8f}".format(item[1][1]) + " " + "{:.8f}".format(item[1][2]) + "\n"
            file_w.write(str)
            str = "vertex " + "{:.8f}".format(item[2][0]) + " " +"{:.8f}".format(item[2][1]) + " " + "{:.8f}".format(item[2][2]) + "\n"
            file_w.write(str)
            str = "vertex " + "{:.8f}".format(item[3][0]) + " " +"{:.8f}".format(item[3][1]) + " " + "{:.8f}".format(item[3][2]) + "\n"
            file_w.write(str)
            file_w.write("endloop")
            file_w.write("\n")
            file_w.write("endfacet")
            file_w.write("\n")
        file_w.write("endsolid")
        file_w.write("\n")
        file_w.close()
    
    def triangle_area(self, x, y, z):
        #x,y,z tuple x(0,1), y(1,1), z(2,1)
        a=((x[0]-y[0])**2+(x[1]-y[1])**2)**.5
        b=((y[0]-z[0])**2+(y[1]-z[1])**2)**.5
        c=((x[0]-z[0])**2+(x[1]-z[1])**2)**.5
        s =(a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**.5

    def check_above(self):
        pass
        return False

    def edge_test(self,item,factor):
        #item triple tuple - triangle coordinates [(x1,y1,z1), (x2,y2,z2), (x3,y3,z3)]
        for i in range(0,3):
            if i == 2: j = 1
            else: j = i+1
            deltax = (item[j][0]-item[i][0])/factor
            deltay = (item[j][1]-item[i][1])/factor
            x = item[i][0]
            y = item[i][1]
            x1 = item[j][0]
            y1 = item[j][1]
            for r in range(0,factor):
                x += deltax
                y += deltay                
           # if self.check_above:
              #  pass
              #  break
              #  print(x,y)

           


    def load_file(self,path):
        file = open(path,"r")
        xx = 0
        lines = []
        self.triangles = [] # = {}
        self.trianglesd = {}
        self.trianglesdx = {}
        file = open(path,"r")
        self.deltaX = 999999999.0
        self.deltaY = 999999999.0
        self.deltaZ = 999999999.0
        avgZ = 0.0
        for line in file.readlines():
            parts = line.split() 
            if len(parts) > 0:
                if parts[0] == 'facet':
                    tline = []
                    tmaxX = -99999999.0
                    tmaxY = -99999999.0
                    tminX = 99999999.0
                    tminY = 99999999.0
                    for i in range(2,5): parts[i]=float(parts[i])
                    tline.append((parts[2], parts[3], parts[4]))
                if parts[0] == 'vertex':
                    for i in range(1,4): parts[i]=float(parts[i])
                    tline.append((parts[1], parts[2], parts[3]))
                    if parts[1] > self.maxX: self.maxX = parts[1]
                    if parts[2] > self.maxY: self.maxY = parts[2]
                    if parts[3] > self.maxZ: self.maxZ = parts[3]
                    if parts[1] < self.minX: self.minX = parts[1]
                    if parts[2] < self.minY: self.minY = parts[2]
                    if parts[3] < self.minZ: self.minZ = parts[3]
                    # triangle min-max
                    if parts[1] > tmaxX: tmaxX = parts[1]
                    if parts[2] > tmaxY: tmaxY = parts[2]
                    if parts[1] < tminX: tminX = parts[1]
                    if parts[2] < tminY: tminY = parts[2]
                    avgZ=avgZ+parts[3] 
                if parts[0] == 'endloop':
                    avgZ = avgZ / 3
                    self.triangles.append(tline)
#vertex 0,1,2  factor 3
                    self.trianglesd[avgZ, (tminX, tmaxX, tminY, tmaxY),((tline[1][0],tline[1][1],tline[1][2]),(tline[2][0],tline[2][1],tline[2][2]),(tline[3][0],tline[3][1],tline[3][2]))] = ((tline[0][0],tline[0][1],tline[0][2]))
                    xx += 1
                    avgZ = 0.0
        file.close()
        print("total:", xx)
        print("min > max", self.minX, self.minY, self.minZ, "  >   ", self.maxX, self.maxY, self.maxZ)
        self.trianglesdx = collections.OrderedDict(sorted(r2.trianglesd.items(),reverse=False))
        return self.triangles

    def PointInTriangle1(self, p, a,b,c, delta):
        A  = self.triangle_area(a, b, c)
        A1 = self.triangle_area(p, b, c)
        A2 = self.triangle_area(a, p, c)
        A3 = self.triangle_area(a, b, p)
        return (abs(A-A1-A2-A3) < delta)

    def find_triangle(self,x,y,z):
        maxZtri = [] # item with max Z
        zz = -999999999.99
        for item in self.triangles:
            if self.PointInTriangle1((x,y,z),item[1],item[2],item[3],0.01):
                # keep average z, looking for max Z
                zzz = (item[1][2]+item[2][2]+item[3][2])/3
                if zzz > zz:
                   zz = zzz
                   if len(maxZtri) > 0: self.triangles.remove(maxZtri)
                   maxZtri = item

    def find_triangled(self,x,y,z):
        new_d = self.trianglesd.copy()
        maxZtri = () # item with max Z
        zz = -999999999.99
        for item in self.trianglesd:
            if self.PointInTriangle1((x,y,z),item[0],item[1],item[2],0.001):
                # keep average z, looking for max Z
                zzz = (item[0][2]+item[1][2]+item[2][2])/3
                if zzz > zz:
                    if len(maxZtri) > 0: new_d.pop(maxZtri, None) #!!!!!!!!!!
                    zz = zzz
                    maxZtri = item
                    
                else:
                   if len(maxZtri) > 0 and zzz < zz: new_d.pop(item, None)

    def find_triangledx(self,x,y,z):
        for item in self.trianglesdx:
            self.total_ops += 1
            if self.PointInTriangle1((x,y,z),item[2][0],item[2][1],item[2][2],0.1):
                self.new_d[item] = self.trianglesdx[item]
                self.vol = self.vol + (0.01*(item[2][0][2]+item[2][1][2]+item[2][2][2])/3)
                return

r2 = Reader()
block = r2.load_file(r"C:/3D/Petr/Support_count_test_ASCII.stl")  #Support_count_test_ASCII.stl") #TEST.stl
#r2.save_file("C:/3D/Petr/XXX.stl", block)
dx = 0.01 #r2.deltaX*0.9
dy = 0.01 #r2.deltaY*0.9
startx = int(r2.minX/dx)  # bylo 0.1
endx   = int(r2.maxX/dx)
starty = int(r2.minY/dy)
endy   = int(r2.maxY/dy)
#startx = int(r2.minX/(r2.deltaX*0.9))  # bylo 0.1
#endx   = int(r2.maxX/(r2.deltaX*0.9))
#starty = int(r2.minY/(r2.deltaY*0.9))
#endy   = int(r2.maxY/(r2.deltaY*0.9))
print("min-max X,Y",r2.minX,r2.maxX,r2.minY,r2.maxY)
print("delta x,y:", r2.deltaX, r2.deltaY)
print("start-end x,y",startx,endx,starty,endy)
print("triangles:", len(r2.trianglesdx), len(r2.triangles))
i = 0
print("start:",time.asctime( time.localtime(time.time()) ))
j = 0
#for item in block: print(item)
#for item in r2.trianglesd:
#   print(item,r2.trianglesd[item])
for item in r2.trianglesdx:
    print(item,r2.trianglesdx[item])
#file_lg = open("C:/3D/Petr/log.txt","w")
for xx in range(startx, endx, 1):
 #   print(endx-xx, time.asctime( time.localtime(time.time()) ))
    for yy in range(starty,endy,1):
#        r2.find_triangledx(xx*dx,yy*dy,0)
        i += 1

# for xx in range(startx, endx, 1):
#    for yy in range(starty,endy,1):
#      r2.find_triangledx(xx,yy,0)
#      i += 1
#file_lg.write("\n")
#file_lg.close()
print("i:",i)
print("triangles:", len(r2.new_d))
print("end:",time.asctime( time.localtime(time.time()) ))
r2.save_file("C:/3D/Petr/XXXred.stl", r2.triangles)
r2.save_filedictx("C:/3D/Petr/XXXdict.stl", r2.new_d)
volume = 0.0
for item in r2.new_d:
    volume += item[0]*r2.new_d[item][1]
print("find tri", i,"total ops:",r2.total_ops)
print("volume:",volume, r2.vol)
i = 0
vv=0.0
for item in r2.new_d:
     print(i,item,r2.new_d[item])
     vv = vv + (item[0]*r2.new_d[item][1])
     print (vv,item[0],r2.new_d[item][1])
     i += 1
print("volume:", vv)


