import time             # for sleep
import collections

class Reader():
    
    def __init__(self):
        self.maxX      = 0.0
        self.minX      = 10000000.0
        self.maxY      = 0.0
        self.minY      = 10000000.0
        self.maxZ      = 0.0
        self.minZ      = 10000000.0
        self.triangles = []
        self.new_d     = {}
        self.total_ops = 0
        self.vol       = 0.0
        self.deltaX    = 0.01
        self.deltaY    = 0.01


    def save_filedict(self, path, block):
        file_w = open(path,"w")
        file_w.write("solid ")
        file_w.write("\n")
        for item in block:
            str = "facet normal " + "{:.6f}".format(block[item][0]) + " " +"{:.6f}".format(block[item][1]) + " " + "{:.6f}".format(block[item][2]) + "\n"
            file_w.write(str)
            file_w.write("outer loop")
            file_w.write("\n")
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
        file_w.write("endsolid ")
        file_w.write("\n")
        file_w.close()

  
    def triangle_area(self, x, y, z):
        #x,y,z tuple x(0,1), y(1,1), z(2,1)
        a=((x[0]-y[0])**2+(x[1]-y[1])**2)**.5
        b=((y[0]-z[0])**2+(y[1]-z[1])**2)**.5
        c=((x[0]-z[0])**2+(x[1]-z[1])**2)**.5
        s =(a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**.5


    def load_file(self,path):
        file = open(path,"r")
        xx = 0
        lines = []
        self.triangles = [] # = {}
        self.trianglesd = {}
        self.trianglesdx = {}
        file = open(path,"r")
        avgZ = 0.0
        for line in file.readlines():
            items = line.split() 
            if len(items) > 0:
                if items[0] == 'facet':
                    tline = []
                    tmaxX = -99999999.0
                    tmaxY = -99999999.0
                    tminX = 99999999.0
                    tminY = 99999999.0
                    for i in range(2,5): items[i]=float(items[i])
                    tline.append((items[2], items[3], items[4]))
                if items[0] == 'vertex':
                    for i in range(1,4): items[i]=float(items[i])
                    tline.append((items[1], items[2], items[3]))
                    if items[1] > self.maxX: self.maxX = items[1]
                    if items[2] > self.maxY: self.maxY = items[2]
                    if items[3] > self.maxZ: self.maxZ = items[3]
                    if items[1] < self.minX: self.minX = items[1]
                    if items[2] < self.minY: self.minY = items[2]
                    if items[3] < self.minZ: self.minZ = items[3]
                    # triangle min-max
                    if items[1] > tmaxX: tmaxX = items[1]
                    if items[2] > tmaxY: tmaxY = items[2]
                    if items[1] < tminX: tminX = items[1]
                    if items[2] < tminY: tminY = items[2]
                    avgZ=avgZ+items[3] 
                if items[0] == 'endloop':
                    avgZ = avgZ / 3
                    self.triangles.append(tline)
                    self.trianglesd[avgZ, (tminX, tmaxX, tminY, tmaxY),\
                        ((tline[1][0],tline[1][1],tline[1][2]),\
                        (tline[2][0],tline[2][1],tline[2][2]),\
                        (tline[3][0],tline[3][1],tline[3][2]))] = ((tline[0][0],tline[0][1],tline[0][2]))
                    xx += 1
                    avgZ = 0.0
        file.close()
        tri = {}
        for item in self.trianglesd:
            tri[item[0]-self.minZ,((item[1][0]-self.minX),(item[1][1]-self.minY),(item[1][2]-self.minX),(item[1][3]-self.minY)),\
                (((item[2][0][0]-self.minX),(item[2][0][1]-self.minY),(item[2][0][2]-self.minZ)),\
                 ((item[2][1][0]-self.minX),(item[2][1][1]-self.minY),(item[2][1][2]-self.minZ)),\
                 ((item[2][2][0]-self.minX),(item[2][2][1]-self.minY),(item[2][2][2]-self.minZ))\
                 )] = ((self.trianglesd[item][0],self.trianglesd[item][1],self.trianglesd[item][2]))
        self.maxX -= self.minX
        self.minX = 0
        self.maxY -= self.minY
        self.minY = 0
        self.maxZ -= self.minZ
        self.minZ = 0
        self.trianglesd = {}
        self.trianglesdx = collections.OrderedDict(sorted(tri.items(),reverse=False))
        print(self.minX,self.maxX,self.minY,self.maxY)
#        r2.save_filedict("C:/3D/Petr/XXXdictMoved.stl", self.trianglesdx)
        return self.triangles

    def PointInTriangle(self, p, a,b,c, delta):
        A  = self.triangle_area(a, b, c)
        A1 = self.triangle_area(p, b, c)
        A2 = self.triangle_area(a, p, c)
        A3 = self.triangle_area(a, b, p)
        return (abs(A-A1-A2-A3) < delta)

    def find_triangle(self,x,y,z,deltaX,deltaY):
        in_body = False
        h = 0.0
        for item in self.trianglesdx:
            self.total_ops += 1
            if x > item[1][0] and x < item[1][1] and y > item[1][2] and y < item[1][3]:
                if self.PointInTriangle((x,y,z),item[2][0],item[2][1],item[2][2],0.1):
                    if in_body: 
                        h = item[0]
                    else:
                        self.vol += ((item[0]-h)*deltaX*deltaY)
                        if item[0] > 0: self.new_d[item] = self.trianglesdx[item]
                    in_body = not in_body

    def getVolume(self):
        startx = int(self.minX/self.deltaX)  
        endx   = int(self.maxX/self.deltaX)
        starty = int(self.minY/self.deltaY)
        endy   = int(self.maxY/self.deltaY)
        print("X",self.minX,self.maxX,self.minY,self.maxY,self.deltaX,self.deltaY)
        print(startx,starty,endx,endy)
        for xx in range(startx, endx, 1):
            for yy in range(starty,endy,1):
                self.find_triangle(xx*self.deltaX,yy*self.deltaY,0,self.deltaX,self.deltaY)
        return self.vol
                    
r2 = Reader()
#block = r2.load_file(r"C:/3D/Petr/TEST.stl")  #Support_count_test_ASCII.stl") #TEST.stl
block = r2.load_file(r"C:/3D/Petr/Support_count_test_ASCII.stl")  #Support_count_test_ASCII.stl") #TEST.stl
print("start:",time.asctime( time.localtime(time.time()) ))
print(" volume:",r2.getVolume())
#r2.save_filedict("C:/3D/Petr/XXXdict.stl", r2.new_d)
print("end:",time.asctime( time.localtime(time.time()) ))
print("total ops:",r2.total_ops)

