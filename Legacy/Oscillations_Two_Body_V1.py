from qutip import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from Output import *
from Constants import *

#Second version of code. Trying to implmenet the full Hamiltonian with rotating terms this time
#trying string format this time

#define all methods 

def append_op(op1,freq1,op2,freq2,lst):
	for i in [[op1,-1*freq1],[op1.dag(),freq1]]:
		for j in [[op2,-1*freq2],[op2.dag(),freq2]]:
			lst.append([(1/freq2)*i[0]*j[0],i[1]+j[1],'cos(' + str(i[1]+j[1]) + '*t) + (0 + 1j)*sin(' + str(i[1]+j[1]) + '*t)'])
	return lst

#For the two body interation we need to add a three body version of the method above.
#Need to add the frequencys to this method
def append_op3(op1,freq1,op2,freq2,freq3,lst):
	for i in [[op1,-1*freq1],[op1.dag(),freq1]]:
		for j in [[op2,-1*freq2],[op2.dag(),freq2]]:
			lst.append([(1/freq2)*i[0]*j[0],i[1]+j[1]+freq3,'cos(' + str(i[1]+j[1]+freq3) + '*t) + (0 + 1j)*sin(' + str(i[1]+j[1]+freq3) + '*t)'])
			lst.append([(1/freq2)*i[0]*j[0],i[1]+j[1]-freq3,'cos(' + str(i[1]+j[1]-freq3) + '*t) + (0 + 1j)*sin(' + str(i[1]+j[1]-freq3) + '*t)'])
	return lst

print("Begining Two Body Simulation\nDefining Hamiltonian")

op_freq_lst 	= []
op_freq_lst 	= append_op(g*q1	,omega1 	,g*q4 	,omega4 	,op_freq_lst)
op_freq_lst 	= append_op(g*q2 	,omega2 	,g*q4 	,omega4 	,op_freq_lst)
#op_freq_lst 	= append_op(EJ*q4	,omega4 	,I 		,omegad1 	,op_freq_lst)
op_freq_lst 	= append_op3(EJ*q4	,omega4 	,EJ*q4 	,omegad4 	,omegad12	,op_freq_lst)
H 				= []

#Hamiltonian for the first integral in the Dyson series
for i in op_freq_lst:
	for j in op_freq_lst:
		H.append([i[0]		*j[0] 		, 'cos(' + str(-i[1]-j[1])  + '*t) + (0 + 1j)*sin(' + str(-i[1]-j[1])  + '*t)'])
		H.append([i[0]		*j[0].dag() , 'cos(' + str(-i[1]+j[1])  + '*t) + (0 + 1j)*sin(' + str(-i[1]+j[1])  + '*t)'])
		H.append([i[0].dag()*j[0] 		, 'cos(' + str(+i[1]-j[1])  + '*t) + (0 + 1j)*sin(' + str(+i[1]-j[1])  + '*t)'])
		H.append([i[0].dag()*j[0].dag() , 'cos(' + str(+i[1]+j[1])  + '*t) + (0 + 1j)*sin(' + str(+i[1]+j[1])  + '*t)'])

#Now need to create the Hamiltonian for the second integral in the Hamiltonian. We also need to add the 1/omega terms for the second integral
for i in op_freq_lst:
	for j in op_freq_lst:
		for k in op_freq_lst:
			H.append([i[0]		 *j[0] 		 *k[0], 		'cos(' + str(-i[1]-j[1]-k[1]) + '*t) + (0 + 1j)*sin(' + str(-i[1]-j[1]-k[1])  + '*t)'])
			H.append([i[0].dag() *j[0] 		 *k[0], 		'cos(' + str(+i[1]-j[1]-k[1]) + '*t) + (0 + 1j)*sin(' + str(+i[1]-j[1]-k[1])  + '*t)'])
			H.append([i[0]		 *j[0].dag() *k[0], 		'cos(' + str(-i[1]+j[1]-k[1]) + '*t) + (0 + 1j)*sin(' + str(-i[1]+j[1]-k[1])  + '*t)'])
			H.append([i[0]		 *j[0] 		 *k[0].dag(), 	'cos(' + str(-i[1]-j[1]+k[1]) + '*t) + (0 + 1j)*sin(' + str(-i[1]-j[1]+k[1])  + '*t)'])
			H.append([i[0]		 *j[0].dag() *k[0].dag(), 	'cos(' + str(-i[1]+j[1]+k[1]) + '*t) + (0 + 1j)*sin(' + str(-i[1]+j[1]+k[1])  + '*t)'])
			H.append([i[0].dag() *j[0] 		 *k[0].dag(),	'cos(' + str(+i[1]-j[1]+k[1]) + '*t) + (0 + 1j)*sin(' + str(+i[1]-j[1]+k[1])  + '*t)'])
			H.append([i[0].dag() *j[0].dag() *k[0], 		'cos(' + str(+i[1]+j[1]-k[1]) + '*t) + (0 + 1j)*sin(' + str(+i[1]+j[1]-k[1])  + '*t)'])
			H.append([i[0].dag() *j[0].dag() *k[0].dag(), 	'cos(' + str(+i[1]+j[1]+k[1]) + '*t) + (0 + 1j)*sin(' + str(+i[1]+j[1]+k[1])  + '*t)'])



print("Integrating Hamiltonian")

result = mesolve(H,inital_state,tlist1,c_ops,obs_ops,options=Options(nsteps = 20000,store_states = True)) # Perform the integration using qutip

print("Outputing Results")
out(result)

print("Done")
print("===========================")