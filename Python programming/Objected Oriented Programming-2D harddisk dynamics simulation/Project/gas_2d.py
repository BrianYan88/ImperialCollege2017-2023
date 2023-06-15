#Object-oriented implementation of a hard-disks molecular dynamics simulations
from itertools import combinations
#import numpy as np
class Vector():
    '''2D vectors'''

    def __init__(self, i1,i2):
        '''Initialise vectors with x and y coordinates'''
        self.x = i1
        self.y = i2

    def __add__(self,other):
        '''Use + sign to implement vector addition'''
        return (Vector(self.x+other.x,self.y+other.y))

    def __sub__(self,other):
        '''Use - sign to implement vector "subtraction"'''
        return (Vector(self.x-other.x,self.y-other.y))

    def __mul__(self,number):
        '''Use * sign to multiply a vector by a scaler on the left'''
        return Vector(self.x*number,self.y*number)

    def __rmul__(self,number):
        '''Use * sign to multiply a vector by a scaler on the right'''
        return Vector(self.x*number,self.y*number)

    def __truediv__(self,number):
        '''Use / to multiply a vector by the inverse of a number'''
        return Vector(self.x/number,self.y/number)

    def __repr__(self):
        '''Represent a vector by a string of 2 coordinates separated by a space'''
        return '{x} {y}'.format(x=self.x, y=self.y)

    def copy(self):
        '''Create a new object which is a copy of the current.'''
        return Vector(self.x,self.y)

    def dot(self,other):
        '''Calculate the dot product between two 2D vectors'''
        return self.x*other.x + self.y*other.y

    def norm(self):
        '''Calculate the norm of the 2D vector'''
        return (self.x**2+self.y**2)**0.5
    
#    def angle(self, vector1):
        #return np.arccos(self.dot(vector1)/(self.norm()*vector1.norm()))

class Simulation():
    def __init__(self, particles, box_length, dt):
        self.particles=particles
        self.box_length=box_length
        self.dt=dt
        self.trajectory = []
        self.trajectory = self.trajectory + [self.record_state()]
        total_area = 0
        for i in self.particles:
            total_area = total_area + 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230825334468503526193118817101000313783875288658753320838142061717766914730359825349042875546873115956286388235378759375195778185778053217122680661300192787661119590921642019893809525 * i.radius**2
        self.density=total_area / (box_length**2)
        
    def step(self):
        for a, b in combinations (self.particles, 2):
                self.apply_particle_collision(a, b)
        for i in self.particles:
            self.apply_box_collisions(i)
            i.position = i.position + i.velocity() * self.dt 
        self.trajectory = self.trajectory + [self.record_state()]
        
    def apply_particle_collision(self, particle1, particle2):
        if particle1.overlap(particle2):
            collision_axis = ( particle2.position - particle1.position ) / ( ( particle2.position - particle1.position ).norm() )
            momentum_caxis1 = collision_axis * particle1.momentum.dot(collision_axis)
            momentum_oaxis1 = particle1.momentum - momentum_caxis1
            momentum_caxis2 = collision_axis * particle2.momentum.dot(collision_axis)
            momentum_oaxis2 = particle2.momentum - momentum_caxis2
            if ( momentum_caxis2 - momentum_caxis1 ).dot(collision_axis) < 0 :
                particle1.momentum = ( (particle1.mass - particle2.mass) * momentum_caxis1 + 2 * particle1.mass * momentum_caxis2 ) / ( particle1.mass + particle2.mass ) + momentum_oaxis1
                particle2.momentum = ( (particle1.mass - particle2.mass) * momentum_caxis2 + 2 * particle1.mass * momentum_caxis1 ) / ( particle1.mass + particle2.mass ) + momentum_oaxis2
            
    def apply_box_collisions(self, particle ):
        if ( particle.position.x < particle.radius and particle.momentum.x < 0 ) or ( self.box_length - particle.position.x < particle.radius and particle.momentum.x > 0) :
            particle.momentum.x = particle.momentum.x * (-1)
        if ( particle.position.y < particle.radius and particle.momentum.y < 0 ) or ( self.box_length - particle.position.y < particle.radius and particle.momentum.y > 0) :
            particle.momentum.y = particle.momentum.y * (-1)
            
    def record_state(self):
        state = []
        for i in self.particles:
            state = state + [i.copy()]
        return state

class Particle():
    def __init__(self, position, momentum, radius, mass):
        self.position = position
        self.momentum = momentum
        self.radius = radius
        self.mass = mass
        
    def velocity(self):
        'returns velocity of particle'
        velocity = self.momentum / self.mass
        return velocity

    def copy(self):
        'returns copy of particle class'
        return Particle (self.position, self.momentum, self.radius, self.mass )
    
    def overlap(self, other_particle):
        return (self.position - other_particle.position).norm() <= other_particle.radius + self.radius

def init_randomsqrlongsim ( N, box_length):
    init_random = []
    from numpy.random import random
    for p in range(0,N):
        pos_x = random() * box_length
        pos_y = random() * box_length
        pos = Vector(pos_x,pos_y)
        mom_x = random() - 0.5
        mom_y = random() - 0.5
        mom=Vector(mom_x,mom_y)
        init_random.append(Particle(pos, mom, 1, 1))
    return init_random