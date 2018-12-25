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
                for i in range(1,4):
                    line=file.readline() # reading vertex
                    tline.append([float(x) for x in (line.replace("vertex","")).strip().split(' ')]) 
                    if tline[i][0] > self.maxX: self.maxX = tline[i][0]
                    if tline[i][1] > self.maxY: self.maxY = tline[i][1]
                    if tline[i][2] > self.maxZ: self.maxZ = tline[i][2]
                    if tline[i][0] < self.minX: self.minX = tline[i][0]
                    if tline[i][1] < self.minY: self.minY = tline[i][1]
                    if tline[i][2] < self.minZ: self.minZ = tline[i][2]
                    # triangle min-max
                    if not tline[i][2] in z:
                        # [z] : minX, minY, maxX,maxY
                        z[tline[i][2]] = (tline[i][0],tline[i][1],tline[i][0],tline[i][1])
                    else:
                        if tline[i][0] < z[tline[i][2]][0] : z[tline[i][2]] = (tline[i][0],z[tline[i][2]][1],z[tline[i][2]][2],z[tline[i][2]][3]) # minX
                        if tline[i][1] < z[tline[i][2]][1] : z[tline[i][2]] = (z[tline[i][2]][0],tline[i][1],z[tline[i][2]][2],z[tline[i][2]][3]) # maxX
                        if tline[i][0] > z[tline[i][2]][2] : z[tline[i][2]] = (z[tline[i][2]][0],z[tline[i][2]][1],tline[i][0],z[tline[i][2]][3]) # minX
                        if tline[i][1] > z[tline[i][2]][3] : z[tline[i][2]] = (z[tline[i][2]][0],z[tline[i][2]][1],z[tline[i][2]][2],tline[i][1]) # maxX
                    if tline[i][0] > tmaxX: tmaxX = tline[i][0]
                    if tline[i][1] > tmaxY: tmaxY = tline[i][1]
                    if tline[i][0] < tminX: tminX = tline[i][0]
                    if tline[i][1] < tminY: tminY = tline[i][1]
                avgZ=(tline[1][2]+tline[2][2]+tline[3][2])/3
            line = file.readline()
            if not line: break
        file.close()
        for item in z:
            print(item,z[item])
        return self.triangles

r2 = Reader()
block = r2.load_file(r"C:/3D/Petr/XXXdict.stl")