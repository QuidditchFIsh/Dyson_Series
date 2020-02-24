from qutip import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from Output import *
from Constants import *

#Second version of code. Trying to implmenet the full Hamiltonian with rotating terms this time
#trying string format this time

#define all methods 

def append_op(op1,op2,freq1,freq2,lst):
	for i in [[op1,-1*freq1],[op1.dag(),freq1]]:
		for j in [[op2,-1*freq2],[op2.dag(),freq2]]:
			lst.append([(1/freq2)*i[0]*j[0],i[1]+j[1],'cos(' + str(i[1]+j[1]) + '*t) + (0 + 1j)*sin(' + str(i[1]+j[1]) + '*t)'])
	return lst


print("Begining Simulation\nDefining Hamiltonian")

op_freq_lst 	= []
op_freq_lst 	= append_op(g*q1	,omega1 	,g*q4 	,omega4 	,op_freq_lst)
op_freq_lst 	= append_op(g*q2 	,omega2 	,g*q4 	,omega4 	,op_freq_lst)
op_freq_lst 	= append_op(EJ*q4	,omega4 	,I 		,omegad1 	,op_freq_lst)
op_freq_lst 	= append_op(EJ*q4	,omega4 	,q4 	,omegad1 	,op_freq_lst)
H 				= []

for i in op_freq_lst:
	for j in op_freq_lst:
		H.append([i[0]		*j[0] 		, 'cos(' + str(-i[1]-j[1]) + '*t) + (0 + 1j)*sin(' + str(-i[1]-j[1]) + '*t)'])
		H.append([i[0]		*j[0].dag() , 'cos(' + str(-i[1]+j[1]) + '*t) + (0 + 1j)*sin(' + str(-i[1]+j[1]) + '*t)'])
		H.append([i[0].dag()*j[0] 		, 'cos(' + str(i[1]-j[1])  + '*t) + (0 + 1j)*sin(' + str(i[1]-j[1])  + '*t)'])
		H.append([i[0].dag()*j[0].dag() , 'cos(' + str(i[1]+j[1])  + '*t) + (0 + 1j)*sin(' + str(i[1]+j[1])  + '*t)'])

print("Integrating Hamiltonian")

result = mesolve(H,inital_state,tlist1,c_ops,obs_ops,options=Options(nsteps = 20000,store_states = True)) # Perform the integration using qutip

print("Outputing Results")
out(result)

print("Done")
print("===========================")