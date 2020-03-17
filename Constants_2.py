'''
Little method to define all of the constants and observables needed in the simulation
'''
from qutip import *
from math import *
import numpy as np


pi 				= 0.5#3.14159265358979323
#Define all of the frequecnies we will need
omega1 			= 4
omega2 			= 5
omega3 			= 7
omega4 			= 8

omegad1			= omega1
omegad2 		= omega2 
omegad12		= omega1+omega2
omegad12d		= omega1-omega2

dim			 	= 4
g 				= 0.1
EJ 				= 0.5
U 				= 30
spin 			= (dim-1)*0.5

Id 				= qeye(dim)
I 				= tensor(qeye(dim),qeye(dim),qeye(dim))

#Define qutip operators to use

a 				= destroy(dim)

q1 				= tensor(a,qeye(dim),qeye(dim))
q2 				= tensor(qeye(dim),a,qeye(dim))
q4 				= tensor(qeye(dim),qeye(dim),a)

one 			= basis(dim,1)
zero 			= basis(dim,0)


zero_transformed 	= (1/sqrt(2)) * (zero + (0+1j)*one)
one_transformed 	= (1/sqrt(2)) * (zero - (0+1j)*one)

#operators to measure

scale = 1/sqrt(2)
sx1 			= scale*tensor(jmat(spin,'x'),Id,Id)
sx2 			= scale*tensor(Id,jmat(spin,'x'),Id)
sx4 			= scale*tensor(Id,Id,jmat(spin,'x'))

sy1 			= scale*tensor(jmat(spin,'y'),Id,Id)
sy2 			= scale*tensor(Id,jmat(spin,'y'),Id)
sy4				= scale*tensor(Id,Id,jmat(spin,'y'))

sz1 			= scale*tensor(jmat(spin,'z'),Id,Id)
sz2 			= scale*tensor(Id,jmat(spin,'z'),Id)
sz4 			= scale*tensor(Id,Id,jmat(spin,'z'))

#Integration variables 

#inital_state 	= tensor(one_transformed,zero_transformed,zero_transformed)
inital_state 	= tensor(zero,zero,zero)
tlist1 			= np.linspace(0,500,2000) # time to integrate over
obs_ops 		=[q1.dag()*q1,q2.dag()*q2,q4.dag()*q4,sx1,sx2,sx4,sy1,sy2,sy4,sz1,sz2,sz4]
c_ops 			= []


