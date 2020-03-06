'''
Little method to define all of the constants and observables needed in the simulation
'''
from qutip import *
from math import *
import numpy as np


pi 				= 3.14159265358979323
#Define all of the frequecnies we will need
omega1 			= 4
omega2 			= 5
omega3 			= 7
omega4 			= 17

omegad1			= omega1
omegad2 		= omega2 
omegad12		= omega1+omega2
omegad12d		= omega1-omega2

dim			 	= 3
g 				= 0.2
EJ 				= 1
U 				= 0.2

Id 				= qeye(dim)
I 				= tensor(qeye(dim),qeye(dim),qeye(dim))

#Define qutip operators to use

a 				= destroy(dim)

q1 				= tensor(a,qeye(dim),qeye(dim))
q2 				= tensor(qeye(dim),a,qeye(dim))
q4 				= tensor(qeye(dim),qeye(dim),a)

one 			= basis(dim,1)
zero 			= basis(dim,0)

zero_transformed = sqrt(2)*(zero + (0 + 1j)*one)
one_transformed = sqrt(2) *(zero - (0 + 1j)*one)

#operators to measure
spin = (dim-1)*0.5
sx1 			= tensor(jmat(spin,'x'),Id,Id)
sx2 			= tensor(Id,jmat(spin,'x'),Id)
sx4 			= tensor(Id,Id,jmat(spin,'x'))

sy1 			= tensor(jmat(spin,'y'),Id,Id)
sy2 			= tensor(Id,jmat(spin,'y'),Id)
sy4				= tensor(Id,Id,jmat(spin,'y'))

sz1 			= tensor(jmat(spin,'z'),Id,Id)
sz2 			= tensor(Id,jmat(spin,'z'),Id)
sz4 			= tensor(Id,Id,jmat(spin,'z'))
'''
if(dim == 2):
	sx1 			= tensor(sigmax(),Id,Id)
	sx2 			= tensor(Id,sigmax(),Id)
	sx4 			= tensor(Id,Id,sigmax())

	sy1 			= tensor(sigmay(),Id,Id)
	sy2 			= tensor(Id,sigmay(),Id)
	sy4				= tensor(Id,Id,sigmay())

	sz1 			= tensor(sigmaz(),Id,Id)
	sz2 			= tensor(Id,sigmaz(),Id)
	sz4 			= tensor(Id,Id,sigmaz())
if(dim == 3):
	sx1 			= tensor(jmat(1,'x'),Id,Id)
	sx2 			= tensor(Id,jmat(1,'x'),Id)
	sx4 			= tensor(Id,Id,jmat(1,'x'))

	sy1 			= tensor(jmat(1,'y'),Id,Id)
	sy2 			= tensor(Id,jmat(1,'y'),Id)
	sy4				= tensor(Id,Id,jmat(1,'y'))

	sz1 			= tensor(jmat(1,'z'),Id,Id)
	sz2 			= tensor(Id,jmat(1,'z'),Id)
	sz4 			= tensor(Id,Id,jmat(1,'z'))
if(dim == 4):
	sx1 			= tensor(jmat(1.5,'x'),Id,Id)
	sx2 			= tensor(Id,jmat(1.5,'x'),Id)
	sx4 			= tensor(Id,Id,jmat(1.5,'x'))

	sy1 			= tensor(jmat(1.5,'y'),Id,Id)
	sy2 			= tensor(Id,jmat(1.5,'y'),Id)
	sy4				= tensor(Id,Id,jmat(1.5,'y'))

	sz1 			= tensor(jmat(1.5,'z'),Id,Id)
	sz2 			= tensor(Id,jmat(1.5,'z'),Id)
	sz4 			= tensor(Id,Id,jmat(1.5,'z'))
if(dim == 4):
	sx1 			= tensor(jmat(1.5,'x'),Id,Id)
	sx2 			= tensor(Id,jmat(1.5,'x'),Id)
	sx4 			= tensor(Id,Id,jmat(1.5,'x'))

	sy1 			= tensor(jmat(1.5,'y'),Id,Id)
	sy2 			= tensor(Id,jmat(1.5,'y'),Id)
	sy4				= tensor(Id,Id,jmat(1.5,'y'))

	sz1 			= tensor(jmat(1.5,'z'),Id,Id)
	sz2 			= tensor(Id,jmat(1.5,'z'),Id)
	sz4 			= tensor(Id,Id,jmat(1.5,'z'))
'''
#Integration variables 

#inital_state 	= tensor(one_transformed,zero_transformed,zero_transformed,zero_transformed)
inital_state 	= tensor(zero,zero,zero)
tlist1 			= np.linspace(0,3000,1000) # time to integrate over
obs_ops 		=[q1.dag()*q1,q2.dag()*q2,q4.dag()*q4,sx1,sx2,sx4,sy1,sy2,sy4,sz1,sz2,sz4]
c_ops 			= []


