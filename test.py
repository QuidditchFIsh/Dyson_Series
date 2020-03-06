from qutip import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from Output import *
from Plotting import *
import time

#Testing script for some ideas

dim = 3
a 				= destroy(dim)

q1 				= tensor(a,qeye(dim))
#q2 				= tensor(qeye(dim),a,qeye(dim))
q4 				= tensor(qeye(dim),a)

H = q1*q4*q4.dag() - q1*q4.dag()*q4 + q1.dag()*q4*q4.dag() -q1.dag()*q4.dag()*q4 
print(H)
#H = q1 + q1.dag()
one 			= basis(dim,1)
zero 			= basis(dim,0)

inital_state 	= tensor(one,zero)
tlist1 			= np.linspace(0,10,500) # time to integrate over
obs_ops 		=[q1.dag()*q1,q4.dag()*q4]
c_ops 			= []


print("Integrating Hamiltonian")

t0 = time.time() 
result_1 = mesolve(H,inital_state,tlist1,c_ops,obs_ops,options=Options(nsteps = 20000,store_states = True)) # Perform the integration using qutip
t1 = time.time()
print("Simulation Took:%f s"%(t1-t0))

print("Outputing Results")
Output_str 		= 'Output/Data/'
#Outputing Data
with open(Output_str + 'ocp_q1.dat','w') as fileq1:
	for j in result_1.expect[0]:
		fileq1.write(str(j) + "\n")

with open(Output_str + 'ocp_q4.dat','w') as fileq4:
	for j in result_1.expect[1]:
		fileq4.write(str(j) + "\n")


