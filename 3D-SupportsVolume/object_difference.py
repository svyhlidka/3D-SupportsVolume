
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



    def save_file(self, path, block):
        print(block)
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
    
    def load_file(self,path):
        all_triangles = {}
        file = open(path,"r")
        i = 1
        j = 0
        xx = 0
        lines = []
        self.triangles = [] # = {}
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
                self.triangles.append(tline)
            line = file.readline()
            if not line: break
        file.close()
        return self.triangles

    def compare(self,t1,t2):
        for item in t2:
            if item in t1: t1.remove(item)
        return t1

r2 = Reader()
block = r2.compare(r2.load_file(r"C:/3D/Petr/TEST.stl"),r2.load_file(r"C:/3D/Petr/XXXdict01.stl"))  #Support_count_test_ASCII.stl") #TEST.stl

r2.save_file("C:/3D/Petr/XXXdiffCube1.stl", block)
