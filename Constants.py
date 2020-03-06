'''
Little method to define all of the constants and observables needed in the simulation
'''
from qutip import *
from math import *
import numpy as np


pi 				= 3.14159265358979323
#Define all of the frequecnies we will need
omega1 			= 4
omega2 			= 4.5
omega3 			= 7
omega4 			= 17

omegad1			= omega1
omegad2 		= omega2 
omegad12		= omega1+omega2
omegad12d		= omega1-omega2

dim			 	= 2
g 				= 0.5
EJ 				= 0.05
U 				= 0.1

Id 				= qeye(dim)
I 				= tensor(qeye(dim),qeye(dim),qeye(dim),qeye(dim))

#Define qutip operators to use

a 				= destroy(dim)

q1 				= tensor(a,qeye(dim),qeye(dim),qeye(dim))
q2 				= tensor(qeye(dim),a,qeye(dim),qeye(dim))
q3 				= tensor(qeye(dim),qeye(dim),a,qeye(dim))
q4 				= tensor(qeye(dim),qeye(dim),qeye(dim),a)

one 			= basis(dim,1)
zero 			= basis(dim,0)

zero_transformed = sqrt(2)*(zero + (0 + 1j)*one)
one_transformed = sqrt(2) *(zero - (0 + 1j)*one)

#operators to measure
sx1 			= tensor(jmat(1,'x'),Id,Id,Id)
sx2 			= tensor(Id,jmat(1,'x'),Id,Id)
sx4 			= tensor(Id,Id,Id,jmat(1,'x'))

sy1 			= tensor(jmat(1,'y'),Id,Id,Id)
sy2 			= tensor(Id,jmat(1,'y'),Id,Id)
sy4				= tensor(Id,Id,Id,jmat(1,'y'))

sz1 			= tensor(jmat(1,'z'),Id,Id,Id)
sz2 			= tensor(Id,jmat(1,'z'),Id,Id)
sz4 			= tensor(Id,Id,Id,jmat(1,'z'))

#Integration variables 

#inital_state 	= tensor(one_transformed,zero_transformed,zero_transformed,zero_transformed)
inital_state 	= tensor(one,zero,zero,zero)
tlist1 			= np.linspace(0,500,500) # time to integrate over
obs_ops 		=[q1.dag()*q1,q2.dag()*q2,q4.dag()*q4,sx1,sx2,sx4,sy1,sy2,sy4,sz1,sz2,sz4]
c_ops 			= []


