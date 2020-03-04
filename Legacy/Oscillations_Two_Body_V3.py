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



def strs_two_body(w1,w2):
#Method to generate strengths associated with each freqeuncy in the integration
	f_str = 0
	if(w1 + w2 == 0):
		f_str = 1/w1
	else:
		f_str = (1/w1) * (1/(w1+w2))
	return f_str


def append_oneBody(H,str_op_freq_lst):
#Hamiltonian creation method for the one body hamiltonian
	H0 = 0
	for i in str_op_freq_lst:
		for j in str_op_freq_lst:
			StrOpFreq_lst = [[i[1] * j[1] * i[2] * j[2],-1*i[3] - j[3]],
			[i[1] * j[1] * i[2] * j[2].dag(),-1*i[3] + j[3]],
			[i[1] * j[1] * i[2].dag() * j[2],i[3] - j[3]],
			[i[1] * j[1] * i[2].dag() * j[2].dag(),i[3] + j[3]]]
			for k in StrOpFreq_lst:
			#loop over the possible operators
				freq = k[1]
				op = k[0]
				#i[0] and j[0] are the names of the operators
				#i[1] and j[1] are the strengths of the interactions
				#i[2] and j[2] are the operators
				#i[3] and j[3] are the frequencies 
				#Now add the rotating wave condition
				if(freq == 0):
					H.append([op,'cos(' + str(freq) + '*t) + (0 + 1j)*sin(' + str(freq)  + '*t)'])	
					print(i[0],j[0])
				elif(abs((i[1]*j[1])/(freq*j[3])) > 0.02):
					H.append([op,'cos(' + str(freq) + '*t) + (0 + 1j)*sin(' + str(freq)  + '*t)'])	
					print(i[0],j[0])
						
	return [H,H0]

def append_twoBody(H,str_op_freq_lst):
#Hamiltonian creation method for the two body hamiltonian
	H0 = 0
	for i in str_op_freq_lst:
		for j in str_op_freq_lst:
			for k in str_op_freq_lst:

				for ii in [-1,1]:
					for jj in [-1,1]:
						for kk in [-1,1]:
							#There are alot of terms in this Hamiltonian. Need to think about how to throw away some of the terms.
							freq = ii*i[3] + jj*j[3] + kk*k[3]
							if(freq == 0): # if non rotating automatically append it
								H.append([i[1]*j[1]*k[1]*i[2]*j[2]*k[2],'cos(' + str(freq) + '*t) + (0 + 1j)*sin(' + str(freq)  + '*t)'])
								#print(i[0]+j[0]+k[0])
								H0 += i[1]*j[1]*k[1]
							elif(((ii*i[3] + jj*j[3] + kk*k[3])*(jj*j[3] + kk*k[3])*(kk*k[3])) == 0):#else if to deal with terms in the expansion which have zero wl+wn values
								if(abs((i[1]*j[1]*k[1])/(ii*i[3]*(kk*k[3]))) > 0.02):
									H.append([i[1]*j[1]*k[1]*i[2]*j[2]*k[2],'cos(' + str(freq) + '*t) + (0 + 1j)*sin(' + str(freq)  + '*t)'])
								#print(i[0]+j[0]+k[0])
								H0 += i[1]*j[1]*k[1]
							elif(abs((i[1]*j[1]*k[1])/((ii*i[3] + jj*j[3] + kk*k[3])*(jj*j[3] + kk*k[3])*(kk*k[3]))) > 0.02):
								H.append([i[1]*j[1]*k[1]*i[2]*j[2]*k[2],'cos(' + str(freq) + '*t) + (0 + 1j)*sin(' + str(freq)  + '*t)'])	
								#print(i[0],j[0],k[0])
								#print(freq)
								#print(i[3],j[3],k[3])
								#print('==========')

	return [H,H0]

def append_op(op1,freq1,str1,op_name1,op2,freq2,str2,op_name2,lst):
	for i in [[op1,-1*freq1,op_name1 + ' '],[-0*op1.dag(),freq1,'-'+op_name1 +'.dag() ']]:
		for j in [[op2,-1*freq2,op_name2 + ' '],[op2.dag(),freq2,op_name2 +'.dag() ']]:
			lst.append([i[2]+j[2],str1*str2,i[0]*j[0],i[1]+j[1]])
	return lst

def append_op_sin(op1,freq1,str1,op_name1,op2,freq2,str2,op_name2,lst):
	for i in [[op1,-1*freq1,op_name1 + ' '],[op1.dag(),freq1,op_name1 +'.dag() ']]:
		for j in [[op2,-1*freq2,op_name2 + ' '],[op2.dag(),freq2,op_name2 +'.dag() ']]:
			lst.append([i[2]+j[2],str1*str2,i[0]*j[0],i[1]+j[1]])
	return lst

#For the two body interation we need to add a three body version of the method above.
#Need to add the frequencys to this method
def append_op3(op1,freq1,str1,op_name1,op2,freq2,str2,op_name2,freq3,lst):
	for i in [[op1,-1*freq1,op_name1 + ' '],[op1.dag(),freq1,op_name1 + '.dag() ']]:
		for j in [[op2,-1*freq2,op_name2 + ' '],[op2.dag(),freq2,op_name2 + '.dag() ']]:
			lst.append([i[2]+j[2],str1*str2,i[0]*j[0],i[1]+j[1]+freq3])
			lst.append([i[2]+j[2],str1*str2,i[0]*j[0],i[1]+j[1]-freq3])
	return lst

def append_cos_drive_single(strength,drive,lst):
	lst.append(['q4 '		,strength,q4		,-1*omega4 - drive])
	lst.append(['q4 '	 	,strength,q4		,-1*omega4 + drive])
	lst.append(['q4.dag() '	,strength,q4.dag()	,+1*omega4 - drive])
	lst.append(['q4.dag() '	,strength,q4.dag()	,+1*omega4 + drive])
	return lst

def append_sin_drive_single(strength,drive,lst):
	lst.append(['q4 '		,-1*strength,q4			,-1*omega4 - drive])
	lst.append(['-q4 '	 	,-1*strength,q4			,-1*omega4 + drive])
	lst.append(['-q4.dag() ',strength,q4.dag()	,+1*omega4 - drive])
	lst.append(['q4.dag() '	,strength,q4.dag()	,+1*omega4 + drive])
	return lst


print("Begining Two Body Simulation\nDefining Hamiltonian")

str_op_freq_lst 	= [] # [names,strengths,operator,frequency]
str_op_freq_lst 	= append_op(q1	,omega1,g, 'q1',q4 	,omega4 ,1,'q4' 	,str_op_freq_lst)
#str_op_freq_lst 	= append_op(q2 	,omega2,g, 'q2',q4 	,omega4 ,1,'q4' 	,str_op_freq_lst)
str_op_freq_lst 	= append_cos_drive_single(EJ,omega1,str_op_freq_lst)
#str_op_freq_lst 	= append_op(q4	,omega4,EJ,'q4',I 	,omegad2,1,'I' 		,str_op_freq_lst) # Testing one body interactions
#str_op_freq_lst 	= append_op3(q4	,omega4,EJ,'q4',q4 	,omega4 ,EJ,'q4' 	,omegad12	,str_op_freq_lst) # Testing Two body interactions
#str_op_freq_lst 	= append_op3(q4	,omega4,EJ,'q4',q4 	,omega4 ,EJ,'q4' 	,omegad12d	,str_op_freq_lst) # Testing Two body interactions

H=[]
H = append_oneBody(H,str_op_freq_lst)[0] 
#H2 = append_oneBody(H,str_op_freq_lst)[1] # all the terms which don't rotate
H1 = 0
for i in H:
	H1 += i[0] 
#print(append_oneBody(H,str_op_freq_lst)[1])
#
print(H) # the hamiltonian without the rotating parts
#print(H2)
print((q1-0*q1.dag()) )
#print(H)




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