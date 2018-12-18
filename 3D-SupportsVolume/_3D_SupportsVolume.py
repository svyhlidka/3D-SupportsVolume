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



class MyReader():
    
    def __init__(self):
        self.maxX = 0.0
        self.minX = 10000000.0
        self.maxY = 0.0
        self.minY = 10000000.0
        self.maxZ = 0.0
        self.minZ = 10000000.0

   
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



        for item in triangles: 
            for i in range(1,4):
              if item[i][0] > self.maxX: self.maxX = item[i][0]
              if item[i][1] > self.maxY: self.maxY = item[i][1]
              if item[i][2] > self.maxZ: self.maxZ = item[i][2]
              if item[i][0] < self.maxX: self.minX = item[i][0]
              if item[i][1] < self.maxY: self.minY = item[i][1]
              if item[i][2] < self.maxZ: self.minZ = item[i][2]
 
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
    
    
    def __init__(self):
        self.maxX = 0.0
        self.minX = 10000000.0
        self.maxY = 0.0
        self.minY = 10000000.0
        self.maxZ = 0.0
        self.minZ = 10000000.0
        self.triangles = []
        self.new_d = {}


    def save_filedictx(self, path, block):
        file_w = open(path,"w")
        file_w.write("solid")
        file_w.write("\n")
        for item in block:
            # item - index
            # block[item] - value
            str = "facet normal " + "{:.8f}".format(block[item][0]) + " " +"{:.8f}".format(block[item][1]) + " " + "{:.8f}".format(block[item][2]) + "\n"
            file_w.write(str)
            file_w.write("outer loop")
            file_w.write("\n")
            str = "vertex " + "{:.8f}".format(item[1][0][0]) + " " +"{:.8f}".format(item[1][0][1]) + " " + "{:.8f}".format(item[1][0][2]) + "\n"
            file_w.write(str)
            str = "vertex " + "{:.8f}".format(item[1][1][0]) + " " +"{:.8f}".format(item[1][1][1]) + " " + "{:.8f}".format(item[1][1][2]) + "\n"
            file_w.write(str)
            str = "vertex " + "{:.8f}".format(item[1][2][0]) + " " +"{:.8f}".format(item[1][2][1]) + " " + "{:.8f}".format(item[1][2][2]) + "\n"
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
        file_w.write("solid")
        file_w.write("\n")
        for item in block:
            # item - index
            # block[item] - value
            str = "facet normal " + "{:.8f}".format(block[item][0][0]) + " " +"{:.8f}".format(block[item][0][1]) + " " + "{:.8f}".format(block[item][0][2]) + "\n"
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
        file_w.write("solid")
        file_w.write("\n")
        # {vertex:x,y,z:facet, s, p}
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
            file_w.write("endloop")
            file_w.write("\n")
            file_w.write("endfacet")
            file_w.write("\n")
        file_w.write("endsolid")
        file_w.write("\n")
        file_w.close()
    
    def triangle_area(self, x, y, z):
        #x,y,z tuple x(0,1), y(0,1), z(0,1)
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
       # all = [line for line in open(path)]
       # print(all)
        all_triangles = {}
        file = open(path,"r")
        i = 1
        j = 0
        xx = 0
    #    d=[float(x) for x in (t.strip().split(" "))]
        lines = []


        self.triangles = [] # = {}
        self.trianglesd = {}
        self.trianglesdx = {}
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
                    if tline[i][0] > self.maxX: self.maxX = tline[i][0]
                    if tline[i][1] > self.maxY: self.maxY = tline[i][1]
                    if tline[i][2] > self.maxZ: self.maxZ = tline[i][2]
                    if tline[i][0] < self.maxX: self.minX = tline[i][0]
                    if tline[i][1] < self.maxY: self.minY = tline[i][1]
                    if tline[i][2] < self.maxZ: self.minZ = tline[i][2]
                avgZ=(tline[1][2]+tline[2][2]+tline[3][2])/3
                if tline[0][2] > 0.001:
                    s = self.triangle_area((tline[1][0],tline[1][1]),(tline[2][0],tline[2][1]),(tline[3][0],tline[3][1]))
                    tline.append(s)
                    self.triangles.append(tline)
#                    self.trianglesd[((tline[1][0],tline[1][1],tline[1][2]),(tline[2][0],tline[2][1],tline[2][2]),(tline[3][0],tline[3][1],tline[3][2]))]=((tline[0][0],tline[0][1],tline[0][2]),s,avgZ)
#vertex 0,1,2  factor 3
                    self.trianglesd[avgZ, ((tline[1][0],tline[1][1],tline[1][2]),(tline[2][0],tline[2][1],tline[2][2]),(tline[3][0],tline[3][1],tline[3][2]))] = (tline[0][0],tline[0][1],tline[0][2])
                    xx += 1
            line = file.readline()
            if not line: break
        file.close()
        print("total:", xx)
        print("min > max", self.minX, self.minY, self.minZ, "  >   ", self.maxX, self.maxY, self.maxZ)
        self.trianglesdx = collections.OrderedDict(sorted(r2.trianglesd.items(),reverse=True))
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
 #           print(item)
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
 #           print("zz:",zz,item)
            if self.PointInTriangle1((x,y,z),item[0],item[1],item[2],0.1):
                # keep average z, looking for max Z
                zzz = (item[0][2]+item[1][2]+item[2][2])/3
 #               if (item[0][2]==3.6946) or (zzz==3.6946): print(zzz,"vs.",item[0][2])
                if zzz > zz:
                    if len(maxZtri) > 0: new_d.pop(maxZtri, None) #!!!!!!!!!!
                    zz = zzz
                    maxZtri = item
                else:
                   if len(maxZtri) > 0 and zzz < zz: new_d.pop(item, None)

    def find_triangledx(self,x,y,z):
        for item in self.trianglesdx:
            if self.PointInTriangle1((x,y,z),item[1][0],item[1][1],item[1][2],0.1):
                # find the first
                self.new_d[item] = self.trianglesdx[item]
                return




r2 = Reader2()
block = r2.load_file(r"C:/3D/Petr/Support_count_test_ASCII.stl")  #Support_count_test_ASCII.stl") #TEST.stl
r2.save_file("C:/3D/Petr/XXX.stl", block)
#print(r2.triangle_area((2,1,1),(6,1,1),(4,3,1)))
#print(r2.edge_test([(1,5,1),(5,4,1),(4,1,1)],10))

a = (1,5,1)
b = (5,4,1)
c = (4,1,1)
p = (4.8, 4,1)

print("je tam:", r2.PointInTriangle1(p, a,b,c, 0.1))
i = 0
startx = int(r2.minX/0.1)  # bylo 0.1
endx   = int(r2.maxX/0.1)
starty = int(r2.minY/0.1)
endy   = int(r2.maxY/0.1)
print(startx,endx,starty,endy)
print("triangles:", len(r2.trianglesdx), len(r2.triangles))

#orderedD = collections.OrderedDict(sorted(r2.trianglesd.items(),reverse=True))
#print("start0:",time.asctime( time.localtime(time.time()) ))
#print("triangles:", len(orderedD))
#i = 0
#for item in orderedD:
 #   print(item, orderedD[item])
 #   print(item, orderedD[item][0][0],orderedD[item][0][1],orderedD[item][0][2])
 #   i += 1
 #   if i > 1000: break

print("start:",time.asctime( time.localtime(time.time()) ))

j = 0
for xx in range(startx, endx, 1):
    for yy in range(starty,endy,1):
      r2.find_triangledx(xx,yy,0)
      i += 1


print("i:",i)
print("triangles:", len(r2.new_d))
print("end:",time.asctime( time.localtime(time.time()) ))
r2.save_file("C:/3D/Petr/XXXred.stl", r2.triangles)
r2.save_filedictx("C:/3D/Petr/XXXdict.stl", r2.new_d)

