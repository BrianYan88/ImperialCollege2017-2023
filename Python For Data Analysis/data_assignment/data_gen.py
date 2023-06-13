#Auxiliary scrip for the Python for Data Analysis assignment
#Contains a function to generate a file with data for fitting

import numpy
import numpy.random

def get_data(CID):
    "Receive a CID number and generate a file with noisy linear data."
    x=numpy.linspace(1,4,10)
    numpy.random.seed(CID)
    n=numpy.random.normal(size=(len(x)))
    a=3
    b=2
    d=numpy.column_stack((x,(a*x+b)+n))
    numpy.savetxt('data_'+str(CID)+'.dat',d)
