from qutip import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from Output import *
from Constants import *
from Plotting import *
import time

#Second version of code. Trying to implmenet the full Hamiltonian with rotating terms this time
#trying string format this time

#define all methods 

def append_op(op1,freq1,op2,freq2,lst):
	for i in [[op1,-1*freq1],[op1.dag(),freq1]]:
		for j in [[op2,-1*freq2],[op2.dag(),freq2]]:
			lst.append([i[0]*j[0],i[1]+j[1]])
	return lst

#For the two body interation we need to add a three body version of the method above.
#Need to add the frequencys to this method
def append_op3(op1,freq1,op2,freq2,freq3,lst):
	for i in [[op1,-1*freq1],[op1.dag(),freq1]]:
		for j in [[op2,-1*freq2],[op2.dag(),freq2]]:
			lst.append([i[0]*j[0],i[1]+j[1]+freq3])
			lst.append([i[0]*j[0],i[1]+j[1]-freq3])
	return lst

def strs_two_body(w1,w2):
#Method to generate strengths associated with each freqeuncy in the integration
	f_str = 0
	if(w1 + w2 == 0):
		f_str = 1/w1
	else:
		f_str = (1/w1) * (1/(w1+w2))
	return f_str


def append_oneBody(H,op_freq_lst):
#Hamiltonian creation method for the one body hamiltonian
	H0 = 0
	for i in op_freq_lst:
		for j in op_freq_lst:

			for ii in [-1,1]:
				for jj in [-1,1]:
					freq = ii*i[1] + jj*j[1]
					#if(freq == 0):
					H.append([i[0]*j[0],'cos(' + str(freq) + '*t) + (0 + 1j)*sin(' + str(freq)  + '*t)'])	
					if(freq == 0):
						H0 += i[0]*j[0]
	return [H,H0]

def append_twoBody(H,op_freq_lst):
#Hamiltonian creation method for the two body hamiltonian
	for i in op_freq_lst:
		for j in op_freq_lst:
			for k in op_freq_lst:

				for ii in [-1,1]:
					for jj in [-1,1]:
						for kk in [-1,1]:
							#There are alot of terms in this Hamiltonian. Need to think about how to throw away some of the terms.
							freq = ii*i[1] + jj*j[1] + kk*k[1]
							freq_strength = 1
							#freq_strength = strs_two_body(jj*j[1],kk*k[1])
							if (freq == 0): 
							#Keep all of the terms which are non rotating
								#H.append([freq_strength*i[0]*j[0]*k[0],'cos(' + str(freq) + '*t) + (0 + 1j)*sin(' + str(freq)  + '*t)'])	
								H+=freq_strength*i[0]*j[0]*k[0]
							#elif(freq_strength > 0.01):
							#	H.append([freq_strength*i[0]*j[0]*k[0],'cos(' + str(freq) + '*t) + (0 + 1j)*sin(' + str(freq)  + '*t)'])	

	return H


print("Begining Two Body Simulation\nDefining Hamiltonian")

op_freq_lst 	= []
op_freq_lst 	= append_op(g*q1	,omega1 	,q4 	,omega4 	,op_freq_lst)
op_freq_lst 	= append_op(g*q2 	,omega2 	,q4 	,omega4 	,op_freq_lst)
op_freq_lst 	= append_op(EJ*q4	,omega4 	,I 		,omegad1 	,op_freq_lst) # Testing one body interactions
#op_freq_lst 	= append_op(EJ*q4	,omega4 	,I 		,omegad2 	,op_freq_lst) # Testing one body interactions
#op_freq_lst 	= append_op3(EJ*q4	,omega4 	,EJ*q4 	,omega4 	,omegad12	,op_freq_lst) # Testing Two body interactions
#op_freq_lst 	= append_op3(EJ*q4	,omega4 	,EJ*q4 	,omega4 	,omegad12d	,op_freq_lst) # Testing Two body interactions
H=[]
H = append_oneBody(H,op_freq_lst)[0] 
H2 = append_oneBody(H,op_freq_lst)[1] # all the terms which don't rotate
H1 = 0
for i in H:
	H1 += i[0] 
#print(append_oneBody(H,op_freq_lst)[1])
#
print(H1) # the hamiltonian without the rotating parts
print(H2)
print(q1+q1.dag() + q2 + q2.dag())
#print(H)



'''
print("Integrating Hamiltonian")

t0 = time.time() 
result = mesolve(H,inital_state,tlist1,c_ops,obs_ops,options=Options(nsteps = 20000,store_states = True)) # Perform the integration using qutip
t1 = time.time()
print("Simulation Took:%f s"%(t1-t0))

print("Outputing Results")
out(result)

print("Plotting Results")
plot_data(result)
'''
print("Done")
print("===========================")