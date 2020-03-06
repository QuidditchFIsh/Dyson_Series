'''
Version 6 of the Code. Will be now doing it in more than 2 dimensions since that is where the creation and anhilation operators actually work!!!
'''
from qutip import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from Output import *
from Constants_2 import *
from Plotting import *
import time

#Methods for Script

def append_op(op1,freq1,str1,op_name1,op2,freq2,str2,op_name2,lst):
	for i in [[op1,-1*freq1,op_name1 + ' ',str1],[op1.dag(),freq1,op_name1 +'.dag() ',-1*str1]]:# The minus sign for the operators in this is in the strengths!!!
		for j in [[op2,-1*freq2,op_name2 + ' ',str2],[op2.dag(),freq2,op_name2 +'.dag() ',-1*str2]]:
			lst.append([i[2]+j[2],i[3]*j[3],i[0]*j[0],i[1]+j[1]])
	return lst

def append_cos_drive_single(strength,drive,lst):
	lst.append(['q4 '		,strength,q4		,-1*omega4 - drive])
	lst.append(['q4 '	 	,strength,q4		,-1*omega4 + drive])
	lst.append(['q4.dag() '	,strength,q4.dag()	,+1*omega4 - drive])
	lst.append(['q4.dag() '	,strength,q4.dag()	,+1*omega4 + drive])
	return lst

def append_sin_drive_single(strength,drive,lst):
	lst.append(['q4 '		,strength,(0+1j)*q4			,-1*omega4 - drive])
	lst.append(['-q4 '	 	,strength,(0-1j)*q4			,-1*omega4 + drive])
	lst.append(['q4.dag() ' ,strength,(0+1j)*q4.dag()	,+1*omega4 - drive])
	lst.append(['-q4.dag() ',strength,(0-1j)*q4.dag()	,+1*omega4 + drive])
	return lst

def Dyson_first_approx(str_op_freq_lst,H):
	#loop over the operator list and combine each operator with another in the 
	H0 = 0
	for i in str_op_freq_lst:
		for j in str_op_freq_lst:
			#for each pair of operators in the list we need to create four pairs corresponding the each of the hermitian conjugates possible
			op_lst 		= [i[2]*j[2]		,i[2].dag()*j[2]		,i[2]*j[2].dag()	,i[2].dag()*j[2].dag()]
			freq_lst 	= [-1*i[3] - j[3]	,i[3] - j[3]			,-1*i[3] + j[3]		,i[3] + j[3]]
			str_lst 	= [i[1]*j[1]*(-1/j[3])	,i[1]*j[1]*(-1/j[3])			,i[1]*j[1]*(1/j[3])			,i[1]*j[1]*(1/j[3])]
			for k in range(0,4):
				if(freq_lst[k] == 0):
					H.append([str_lst[k]*op_lst[k] ,'cos(' + str(freq_lst[k]) + '*t) + (0 + 1j)*sin(' + str(freq_lst[k]) + '*t)'])
					H0 += op_lst[k]*str_lst[k]
					print(i[0],j[0],str_lst[k])
				elif((str_lst[k])/(j[3]*freq_lst[k]) > 0.02):
					H.append([str_lst[k]*op_lst[k] ,'cos(' + str(freq_lst[k]) + '*t) + (0 + 1j)*sin(' + str(freq_lst[k]) + '*t)'])
					H0 += op_lst[k]*str_lst[k]
					print("welp")
			
	return [H,H0]
#Defining Hamiltonian

#First need to define the list of operators for this system. For the first approximation we will ony use the firs integral.
print("Begining Two Body Simulation\nDefining Hamiltonian")

str_op_freq_lst 	= [] # [names,strengths,operator,frequency]
str_op_freq_lst 	= append_op(q1	,omega1,g, 'q1',q4 	,omega4 ,1,'q4' 	,str_op_freq_lst)
str_op_freq_lst 	= append_op(q2 	,omega2,g, 'q2',q4 	,omega4 ,1,'q4' 	,str_op_freq_lst)
str_op_freq_lst 	= append_cos_drive_single(EJ,omega1,str_op_freq_lst)
str_op_freq_lst 	= append_cos_drive_single(EJ,omega2,str_op_freq_lst)

#Now need to input this list of operators into methods to generate the sums in the Hamiltonian.
#Will also add an anharmonic term to this system to ensure the lowest two levels are protected.

H = []


# Now append the rest of the Dyson series expansion
D1 = Dyson_first_approx(str_op_freq_lst,H)
H = D1[0]
H1 = D1[1]

#print(H1)
#print((0+1j)*(q1-q1.dag()))
#print(inital_state)


#Integrating Hamiltonian
print("Integrating Hamiltonian")

t0 = time.time() 
result = mesolve(H,inital_state,tlist1,c_ops,obs_ops,options=Options(nsteps = 20000,store_states = True)) # Perform the integration using qutip
t1 = time.time()
print("Simulation Took:%f s"%(t1-t0))

print("Outputing Results")
out(result)

print("Plotting Results")
plot_data(result)

print("Done")
print("===========================")