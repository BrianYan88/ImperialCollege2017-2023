class Molecule:
	'utilizes the xyz file for various analysis of molecules'

	def __init__(self , a , b , c):
		'''Initializes new molecule identity'''
		self.symbols = a
		self.positions = b
		self.charge = c

	def bond(self , a , b):
		'gives bond vector between 2 atoms'
		c=self.positions[a].copy()
		c.scale(-1)
		return self.positions[b] + c

	def bond_length(self , a , b):
		'returns length between 2 atoms'
		return self.bond(a,b).norm()

	def bond_angle(self, a , b, c ):
		'returns bond angles in radians'
		import numpy as np
		bond1 = self.bond( a , b )
		bond2 = self.bond( a , c )
		f = np.arccos( bond1.dot(bond2) / ( self.bond_length(a,c) * self.bond_length(a,b) ) )
		return f

	def bond_angle_deg(self , a , b , c):
		'returns bond angles in degrees'
		import numpy as np
		return self.bond_angle(a , b , c)*180/(np.pi)

	def dipole(self):
		'returns dipole moment vector'
		from vectors import Vector
		a = Vector(0 , 0 , 0)
		for i in range(len(self.symbols)):
			c = self.positions[i]
			c.scale(self.charge[i])
			a = a + c
		return [a.x,a.y,a.z]
			