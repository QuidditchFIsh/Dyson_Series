
from qutip import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from Output import *
from Constants_2 import *
from Plotting import *
import time

T1 = +1 * q1 * q4 * q2 * q4 * q4.dag() * q4.dag() -1 * q1.dag() * q4 * q2 * q4 * q4.dag() * q4.dag() +1 * q1 * q4 * q2.dag() * q4 * q4.dag() * q4.dag() -1 * q1.dag() * q4 * q2.dag() * q4 * q4.dag() * q4.dag()
T2 = -1 * q1 * q4 * q2 * q4.dag() * q4 * q4.dag() +1 * q1.dag() * q4 * q2 * q4.dag() * q4 * q4.dag() -1 * q1 * q4 * q2.dag() * q4.dag() * q4 * q4.dag() +1 * q1.dag() * q4 * q2.dag() * q4.dag() * q4 * q4.dag()
T3 = -1 * q1 * q4.dag() * q2 * q4 * q4 * q4.dag() +1 * q1.dag() * q4.dag() * q2 * q4 * q4 * q4.dag() -1 * q1 * q4.dag() * q2.dag() * q4 * q4 * q4.dag() +1 * q1.dag() * q4.dag() * q2.dag() * q4 * q4 * q4.dag()
T4 = -1 * q1 * q4 * q2 * q4.dag() * q4.dag() * q4 +1 * q1.dag() * q4 * q2 * q4.dag() * q4.dag() * q4 -1 * q1 * q4 * q2.dag() * q4.dag() * q4.dag() * q4 +1 * q1.dag() * q4 * q2.dag() * q4.dag() * q4.dag() * q4
T5 = -1 * q1 * q4.dag() * q2 * q4 * q4.dag() * q4 +1 * q1.dag() * q4.dag() * q2 * q4 * q4.dag() * q4 -1 * q1 * q4.dag() * q2.dag() * q4 * q4.dag() * q4 +1 * q1.dag() * q4.dag() * q2.dag() * q4 * q4.dag() * q4
T6 = +1 * q1 * q4.dag() * q2 * q4.dag() * q4 * q4 -1 * q1.dag() * q4.dag() * q2 * q4.dag() * q4 * q4 +1 * q1 * q4.dag() * q2.dag() * q4.dag() * q4 * q4 -1 * q1.dag() * q4.dag() * q2.dag() * q4.dag() * q4 * q4
'''
T1 = +1 * q1 * q4 * q4.dag() 
T2 = -1 * q1 * q4.dag()  * q4 
T3 = 0
T4 = 0
T5 = 0
T6 = 0
'''

H1 = (0-1j)*(T1 + T2 + T3 + T4 + T5 + T6) + (q2 + q2.dag()) - (0+1j)*(q1 - q1.dag()) + U*q1.dag()*q1.dag()*q1*q1 + U*q2.dag()*q2.dag()*q2*q2
H2 = (0-1j)*(q1-q1.dag())*(q2+q2.dag()) + U*q1.dag()*q1.dag()*q1*q1 + U*q2.dag()*q2.dag()*q2*q2

with open('Hamiltonian.dat','w') as ham:
	for i in H1.full():
		for j in i:
			ham.write(str(round(j.real,2)) + " ")
		ham.write("\n")
with open('Hamiltonian_real.dat','w') as ham:
	for i in H2.full():
		for j in i:
			ham.write(str(round(j.real,2)) + " ")
		ham.write("\n")
inital_state_11 	= tensor(one_transformed,one_transformed,zero_transformed)
#inital_state_11 	= tensor(zero,zero,zero)
result_11 = mesolve(H1,inital_state_11,tlist1,c_ops,obs_ops,options=Options(nsteps = 40000,store_states = True)) # Perform the integration using qutip

inital_state_00 	= tensor(zero_transformed,zero_transformed,zero_transformed)
#inital_state_00 	= tensor(zero,zero,zero)
result_00 = mesolve(H1,inital_state_00,tlist1,c_ops,obs_ops,options=Options(nsteps = 40000,store_states = True)) # Perform the integration using qutip

out2(result_11,'11')
out2(result_00,'00')