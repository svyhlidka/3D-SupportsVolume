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

    def triangle_area(self, x, y, z):
        #x,y,z tuple x(0,1), y(1,1), z(2,1)
        a=((x[0]-y[0])**2+(x[1]-y[1])**2)**.5
        b=((y[0]-z[0])**2+(y[1]-z[1])**2)**.5
        c=((x[0]-z[0])**2+(x[1]-z[1])**2)**.5
        s =(a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**.5

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
        z = {}
        file = open(path,"r")
        line=file.readline()
        self.deltaX = 999999999.0
        self.deltaY = 999999999.0
        self.deltaZ = 999999999.0
        while True:
            if "facet normal" in line:
                tline = []
                tmaxX = -99999999.0
                tmaxY = -99999999.0
                tminX = 99999999.0
                tminY = 99999999.0
                tline.append([float(x) for x in (line.replace("facet normal","")).strip().split(' ')]) # facet normal
                line=file.readline()  # outer loop
                n=0
                for i in range(1,4):
                    line=file.readline() # reading vertex
                    tline.append([float(x) for x in (line.replace("vertex","")).strip().split(' ')]) 
                    # triangle min-max
                    if not tline[i][2] in z:
                        # [z] : minX, minY, maxX, maxY,#tri
                        z[tline[i][2]] = (tline[i][0],tline[i][1],tline[i][0],tline[i][1],0)
                    else:
                        n=z[tline[i][2]][4]+1
                        if tline[i][0] < z[tline[i][2]][0] : z[tline[i][2]] = (tline[i][0],z[tline[i][2]][1],z[tline[i][2]][2],z[tline[i][2]][3],n) # minX
                        if tline[i][1] < z[tline[i][2]][1] : z[tline[i][2]] = (z[tline[i][2]][0],tline[i][1],z[tline[i][2]][2],z[tline[i][2]][3],n) # maxX
                        if tline[i][0] > z[tline[i][2]][2] : z[tline[i][2]] = (z[tline[i][2]][0],z[tline[i][2]][1],tline[i][0],z[tline[i][2]][3],n) # minX
                        if tline[i][1] > z[tline[i][2]][3] : z[tline[i][2]] = (z[tline[i][2]][0],z[tline[i][2]][1],z[tline[i][2]][2],tline[i][1],n) # maxX
            line = file.readline()
            if not line: break
        file.close()
        for item in z:
            print(item,z[item])
        return self.triangles

r2 = Reader()
block = r2.load_file(r"C:/3D/Petr/XXXdict.stl")
#print("##############################################################")
#block = r2.load_file(r"C:/3D/Petr/Support_count_test_ASCII.stl")
volume = 0.0
for item in r2.new_d:
    volume += item[0]*r2.new_d[item][1]
print("find tri", i,"total ops:",r2.total_ops)
print("volume:",volume, r2.vol)