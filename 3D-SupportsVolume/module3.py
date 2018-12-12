from numpy import *
a = array([1,0,0])  
b = array([0,1,0])  
print(cross(a,b))

def cross_product(u,v):  
    dim = len(u)
    s = []
    for i in range(dim):
        if i == 0:
            j,k = 1,2
            s.append(u[j]*v[k] - u[k]*v[j])
        elif i == 1:
            j,k = 2,0
            s.append(u[j]*v[k] - u[k]*v[j])
        else:
            j,k = 0,1
            s.append(u[j]*v[k] - u[k]*v[j])
    return s
print(cross_product(a,b))


def sign(p1, p2, p3):
  return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


def PointInAABB(pt, c1, c2):
  return c2[0] <= pt[0] <= c1[0] and \
         c2[1] <= pt[1] <= c1[1]

def PointInTriangle(pt, v1, v2, v3):
  b1 = sign(pt, v1, v2) <= 0
  b2 = sign(pt, v2, v3) <= 0
  b3 = sign(pt, v3, v1) <= 0

  return ((b1 == b2) and (b2 == b3)) and \
         PointInAABB(pt, map(max, v1, v2, v3), map(min, v1, v2, v3))

def SameSide(p1,p2, a,b):
    cp1 = cross_product(b-a, p1-a)
    cp2 = cross_product(b-a, p2-a)
    if DotProduct(cp1, cp2) >= 0: return True
    else: return False

def PointInTriangle(p, a,b,c):
    if SameSide(p,a, b,c) and SameSide(p,b, a,c)\
        and SameSide(p,c, a,b): return True
    else: return False

#print(PointInTriangle((4,3,1), (1,5,1), (5,4,1),(4,1,1)))


def triangle_area(x, y, z):
        #x,y,z tuple x(0,1), y(0,1), z(0,1)
        a=((x[0]-y[0])**2+(x[1]-y[1])**2)**.5
        b=((y[0]-z[0])**2+(y[1]-z[1])**2)**.5
        c=((x[0]-z[0])**2+(x[1]-z[1])**2)**.5
        s =(a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**.5
print("kiriki ###############")

a = (1,5,1)
b = (5,4,1)
c = (4,1,1)
p = (4.8, 4,1)

def PointInTriangle1(p, a,b,c, delta):
    A  = triangle_area(a, b, c)
    A1 = triangle_area(p, b, c)
    A2 = triangle_area(a, p, c)
    A3 = triangle_area(a, b, p)
    return (abs(A-A1-A2-A3) < delta)
print("je tam:", PointInTriangle1(p, a,b,c, 0.01))
