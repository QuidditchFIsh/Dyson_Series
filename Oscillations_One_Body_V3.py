'''
Version 6 of the Code. Will be now doing it in more than 2 dimensions since that is where the creation and anhilation operators actually work!!!
'''
from qutip import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from Output import *
from Constants import *
from Plotting import *
import time

#Methods for Script

def append_op(op1,freq1,str1,op_name1,op2,freq2,str2,op_name2,lst):
	for i in [[op1,-1*freq1,op_name1 + ' '],[op1.dag(),freq1,op_name1 +'.dag() ']]:
		for j in [[op2,-1*freq2,op_name2 + ' '],[op2.dag(),freq2,op_name2 +'.dag() ']]:
			lst.append([i[2]+j[2],str1*str2,i[0]*j[0],i[1]+j[1]])
	return lst

def append_cos_drive_single(strength,drive,lst):
	lst.append(['q4 '		,strength,q4		,-1*omega4 - drive])
	lst.append(['q4 '	 	,strength,q4		,-1*omega4 + drive])
	lst.append(['q4.dag() '	,strength,q4.dag()	,+1*omega4 - drive])
	lst.append(['q4.dag() '	,strength,q4.dag()	,+1*omega4 + drive])
	return lst

def append_sin_drive_single(strength,drive,lst):
	lst.append(['q4 '		,(0+1j)*strength,q4			,-1*omega4 - drive])
	lst.append(['-q4 '	 	,(0-1j)*strength,q4			,-1*omega4 + drive])
	lst.append(['-q4.dag() ',(0-1j)*strength,q4.dag()	,+1*omega4 - drive])
	lst.append(['q4.dag() '	,(0+1j)*strength,q4.dag()	,+1*omega4 + drive])
	return lst



#Defining Hamiltonian

#First need to define the list of operators for this system. For the first approximation we will ony use the firs integral.
print("Begining Two Body Simulation\nDefining Hamiltonian")

str_op_freq_lst 	= [] # [names,strengths,operator,frequency]
str_op_freq_lst 	= append_op(q1	,omega1,g, 'q1',q4 	,omega4 ,1,'q4' 	,str_op_freq_lst)
#str_op_freq_lst 	= append_op(q2 	,omega2,g, 'q2',q4 	,omega4 ,1,'q4' 	,str_op_freq_lst)
str_op_freq_lst 	= append_cos_drive_single(EJ,omega1,str_op_freq_lst)

#Now need to input this list of operators into methods to generate the sums in the Hamiltonian.
#Will also add an anharmonic term to this system to ensure the lowest two levels are protected.

H = [[U*q1.dag()*q1.dag()*q1*q1 + U*q2.dag()*q2.dag()*q2*q2]]

# Now append the rest of the Dyson series expansion



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