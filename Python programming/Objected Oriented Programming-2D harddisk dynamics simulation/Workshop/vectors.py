class Vector:
    'Implements 3D vectors and their behaviour'

    def __init__(self, i1,i2,i3):
         '''Initializes new vector objects by setting the values
            of their of their 3 components'''
         self.x = i1
         self.y = i2
         self.z = i3

    def scale(self,a):
         'Mutiplies the vector by a scalar a'
         self.x=self.x*a
         self.y=self.y*a
         self.z=self.z*a 
    
    def dot(self,a):
        'Dot product between 2 vectors'
        return self.x * a.x + self.y * a.y + self.z * a.z	

    def norm(self):
        'Returns the vector norm -- length '
        return ( self.x**2 + self.y**2 + self.z**2 ) ** 0.5

    def __add__(self,a):
        'combines vector self and a, updating vector self.'
        return Vector ( self.x+a.x , self.y+a.y , self.z+a.z )

    def copy(self):
        'generates a copy of vector self'
        return Vector( self.x , self.y , self.z )

    def __repr__(self):
        'returns string with values of components'
        a = str(self.x) + str(' ') + str(self.y) + str(' ') + str(self.z)
        return a