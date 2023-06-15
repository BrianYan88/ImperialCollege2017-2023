import numpy as np
def parse_line(x):
    y=x.split()
    a=np.array(y[1:4])
    b=[float(a[0])]+[float(a[1])]+[float(a[2])]
    c=np.array(b)
    z=[y[0]]+[c]
    return z
def load_structure(xyz):
    a=[]
    b=[]
    for lines in xyz:
        a=a+[lines]
    a=a[2:]
    for lines in a:
        lines1=lines.split()
        b=b+[parse_line(lines)]
    return b
def equivalent_atoms(x,y):
    a=False
    b=np.linalg.norm(x[1]-y[1])
    if abs(b)<0.01 and x[0]==y[0]:
        a=True
    return a
def equivalent_structures(x,y):
    a=True
    b=0
    c=0
    d=False
    while a==True and b<len(x):
        while c<len(x) and d==False:
            d=equivalent_atoms(x[b],y[c])
            c=c+1
            if d==True:
                c=0
            elif d==False and c==len(x):
                a=False
        b=b+1
        d=False
    return a
def coordinate_transformation(array,list1):
    a=[]
    for x in list1:
         a=a+[[x[0],np.dot(array,x[1])]]
    return a
def principle_axis(list1):
    n=6
    b=False
    while n>1 and b==False:
        a=coordinate_transformation(np.array([[np.cos(2*np.pi/n),-1*np.sin(2*np.pi/n),0],[np.sin(2*np.pi/n),np.cos(2*np.pi/n),0],[0,0,1]]),list1)
        b=equivalent_structures(a,list1)
        if b==False:
            n=n-1
    return n

sigmavxz=np.array([[1,0,0],[0,-1,0],[0,0,1]])
sigmavyz=np.array([[-1,0,0],[0,1,0],[0,0,1]])
sigmahxy=np.array([[1,0,0],[0,1,0],[0,0,-1]])
i=np.array([[1,0,0],[0,1,0],[0,0,1]])
sigmavxztest=False
sigmavyztest=False
sigmahxytest=False
itest=False
file=input("XYZ file?")
with open(file,'r') as xyz:
    a=load_structure(xyz)
n=principle_axis(a)
sigmavxztest=equivalent_structures(a,coordinate_transformation(sigmavxz,a))
sigmavyztest=equivalent_structures(a,coordinate_transformation(sigmavyz,a))
sigmahxytest=equivalent_structures(a,coordinate_transformation(sigmahxy,a))
itest=equivalent_structures(a,coordinate_transformation(i,a))
if n==1:
    if sigmavyztest==True or sigmavxztest==True or sigmahxytest==True:
        print("-> Cs")
    elif itest==True:
        print("-> Ci")
    else:
        print("C1")
if n>1:
    if sigmahxytest==True:
        print("-> C"+str(n)+"h")
    elif sigmavxztest==True or sigmavyztest==True:
        print("-> C"+str(n)+"v")
    else:
        print("-> C"+str(n))
