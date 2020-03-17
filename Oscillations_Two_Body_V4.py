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

def append_str_second(str_lst,freq1,freq2):
	F0 = -freq1 - freq2
	F1 = -freq1 + freq2
	F2 = +freq1 - freq2
	F3 = -freq1 - freq2
	F4 = +freq1 + freq2
	F5 = -freq1 + freq2
	F6 = +freq1 - freq2
	F7 = +freq1 + freq2

	if(F0 !=0):
		str_lst[0] = str_lst[0] * (1/F0)
	if(F1 !=0):
		str_lst[1] = str_lst[1] * (1/F1)
	if(F2 !=0):
		str_lst[2] = str_lst[2] * (1/F2)
	if(F3 !=0):
		str_lst[3] = str_lst[3] * (1/F3)
	if(F4 !=0):
		str_lst[4] = str_lst[4] * (1/F4)
	if(F5 !=0):
		str_lst[5] = str_lst[5] * (1/F5)
	if(F6 !=0):
		str_lst[6] = str_lst[6] * (1/F6)
	if(F7 !=0):
		str_lst[7] = str_lst[7] * (1/F7)

	return str_lst


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

def append_sin_drive_single_negitive(strength,drive,lst):
	lst.append(['q4 '		,strength,(0-1j)*q4			,-1*omega4 - drive])
	lst.append(['-q4 '	 	,strength,(0+1j)*q4			,-1*omega4 + drive])
	lst.append(['q4.dag() ' ,strength,(0-1j)*q4.dag()	,+1*omega4 - drive])
	lst.append(['-q4.dag() ',strength,(0+1j)*q4.dag()	,+1*omega4 + drive])
	return lst

def append_cos_cos_drive_double(strength,drive1,drive2,lst):
	lst.append(['q4q4 '					,strength, q4*q4 						,-2*omega4 + drive1 + drive2])
	lst.append(['q4q4 '					,strength, q4*q4 						,-2*omega4 - drive1 - drive2])
	lst.append(['q4q4 '					,strength, q4*q4 						,-2*omega4 + drive1 - drive2])
	lst.append(['q4q4 '					,strength, q4*q4 						,-2*omega4 - drive1 + drive2])
	#
	lst.append(['q4.dag()q4 '			,strength, q4.dag()*q4 					,+ drive1 + drive2])
	lst.append(['q4.dag()q4 '			,strength, q4.dag()*q4 					,- drive1 - drive2])
	lst.append(['q4.dag()q4 '			,strength, q4.dag()*q4 					,+ drive1 - drive2])
	lst.append(['q4.dag()q4 '			,strength, q4.dag()*q4 					,- drive1 + drive2])
	#
	lst.append(['q4q4.dag() '			,strength, q4*q4.dag() 					,+ drive1 + drive2])
	lst.append(['q4q4.dag() '			,strength, q4*q4.dag() 					,- drive1 - drive2])
	lst.append(['q4q4.dag() '			,strength, q4*q4.dag() 					,+ drive1 - drive2])
	lst.append(['q4q4.dag() '			,strength, q4*q4.dag() 					,- drive1 + drive2])
	#
	lst.append(['q4.dag()q4.dag() '		,strength, q4.dag()*q4.dag() 			,+2*omega4 + drive1 + drive2])
	lst.append(['q4.dag()q4.dag() '		,strength, q4.dag()*q4.dag() 			,+2*omega4 - drive1 - drive2])
	lst.append(['q4.dag()q4.dag() '		,strength, q4.dag()*q4.dag() 			,+2*omega4 + drive1 - drive2])
	lst.append(['q4.dag()q4.dag() '		,strength, q4.dag()*q4.dag() 			,+2*omega4 - drive1 + drive2])

	return lst

def append_cos_sin_drive_double(strength,drive1,drive2,lst):
	lst.append(['q4q4 '					,strength,(0 - 1j) * q4*q4 							,-2*omega4 + drive1 + drive2])
	lst.append(['q4q4 '					,strength,(0 + 1j)* q4*q4 							,-2*omega4 - drive1 - drive2])
	lst.append(['q4q4 '					,strength,(0 - 1j)* q4*q4 							,-2*omega4 + drive1 - drive2])
	lst.append(['q4q4 '					,strength,(0 + 1j)* q4*q4 							,-2*omega4 - drive1 + drive2])
	#
	lst.append(['q4.dag()q4 '			,strength,(0 - 1j)* q4.dag()*q4 					,+ drive1 + drive2])
	lst.append(['q4.dag()q4 '			,strength,(0 + 1j)* q4.dag()*q4 					,- drive1 - drive2])
	lst.append(['q4.dag()q4 '			,strength,(0 - 1j)* q4.dag()*q4 					,+ drive1 - drive2])
	lst.append(['q4.dag()q4 '			,strength,(0 + 1j)* q4.dag()*q4 					,- drive1 + drive2])
	#
	lst.append(['q4q4.dag() '			,strength,(0 - 1j)* q4*q4.dag() 					,+ drive1 + drive2])
	lst.append(['q4q4.dag() '			,strength,(0 + 1j)* q4*q4.dag() 					,- drive1 - drive2])
	lst.append(['q4q4.dag() '			,strength,(0 - 1j)* q4*q4.dag() 					,+ drive1 - drive2])
	lst.append(['q4q4.dag() '			,strength,(0 + 1j)* q4*q4.dag() 					,- drive1 + drive2])
	#
	lst.append(['q4.dag()q4.dag() '		,strength,(0 - 1j)* q4.dag()*q4.dag() 				,+2*omega4 + drive1 + drive2])
	lst.append(['q4.dag()q4.dag() '		,strength,(0 + 1j)* q4.dag()*q4.dag() 				,+2*omega4 - drive1 - drive2])
	lst.append(['q4.dag()q4.dag() '		,strength,(0 - 1j)* q4.dag()*q4.dag() 				,+2*omega4 + drive1 - drive2])
	lst.append(['q4.dag()q4.dag() '		,strength,(0 + 1j)* q4.dag()*q4.dag() 				,+2*omega4 - drive1 + drive2])

	return lst

def append_cos_sin_drive_double_negitive(strength,drive1,drive2,lst):
	lst.append(['q4q4 '					,strength,(0 + 1j) * q4*q4 							,-2*omega4 + drive1 + drive2])
	lst.append(['q4q4 '					,strength,(0 - 1j)* q4*q4 							,-2*omega4 - drive1 - drive2])
	lst.append(['q4q4 '					,strength,(0 + 1j)* q4*q4 							,-2*omega4 + drive1 - drive2])
	lst.append(['q4q4 '					,strength,(0 - 1j)* q4*q4 							,-2*omega4 - drive1 + drive2])
	#
	lst.append(['q4.dag()q4 '			,strength,(0 + 1j)* q4.dag()*q4 					,+ drive1 + drive2])
	lst.append(['q4.dag()q4 '			,strength,(0 - 1j)* q4.dag()*q4 					,- drive1 - drive2])
	lst.append(['q4.dag()q4 '			,strength,(0 + 1j)* q4.dag()*q4 					,+ drive1 - drive2])
	lst.append(['q4.dag()q4 '			,strength,(0 - 1j)* q4.dag()*q4 					,- drive1 + drive2])
	#
	lst.append(['q4q4.dag() '			,strength,(0 + 1j)* q4*q4.dag() 					,+ drive1 + drive2])
	lst.append(['q4q4.dag() '			,strength,(0 - 1j)* q4*q4.dag() 					,- drive1 - drive2])
	lst.append(['q4q4.dag() '			,strength,(0 + 1j)* q4*q4.dag() 					,+ drive1 - drive2])
	lst.append(['q4q4.dag() '			,strength,(0 - 1j)* q4*q4.dag() 					,- drive1 + drive2])
	#
	lst.append(['q4.dag()q4.dag() '		,strength,(0 + 1j)* q4.dag()*q4.dag() 				,+2*omega4 + drive1 + drive2])
	lst.append(['q4.dag()q4.dag() '		,strength,(0 - 1j)* q4.dag()*q4.dag() 				,+2*omega4 - drive1 - drive2])
	lst.append(['q4.dag()q4.dag() '		,strength,(0 + 1j)* q4.dag()*q4.dag() 				,+2*omega4 + drive1 - drive2])
	lst.append(['q4.dag()q4.dag() '		,strength,(0 - 1j)* q4.dag()*q4.dag() 				,+2*omega4 - drive1 + drive2])

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
					#print(i[0],j[0],str_lst[k])
			
	return [H,H0]

def Dyson_second_approx(str_op_freq_lst,H):
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
					#print(i[0],j[0],str_lst[k])

	for i in str_op_freq_lst:
		for j in str_op_freq_lst:
			for k in str_op_freq_lst:
				#for all of the operators create the relavent list of combinations ( for now best to write these out in full) 
				str3 = i[1] * j[1] * k[1]
				op_lst 	 = [	i[2]*j[2]*k[2]				,i[2]*j[2]*k[2].dag()		,i[2]*j[2].dag()*k[2]		,i[2].dag()*j[2]*k[2],
						   		i[2]*j[2].dag()*k[2].dag()	,i[2].dag()*j[2]*k[2].dag()	,i[2].dag()*j[2].dag()*k[2]	,i[2].dag()*j[2].dag()*k[2].dag()]
				freq_lst = [	-i[3] - j[3] -k[3],-i[3] - j[3] +k[3],-i[3] + j[3] -k[3],+i[3] - j[3] -k[3],
						    	-i[3] + j[3] +k[3],+i[3] - j[3] +k[3],+i[3] + j[3] -k[3],+i[3] + j[3] +k[3],]

				str_lst  = [ 	str3 * (1/(-k[3])),
								str3 * (1/(k[3])),
								str3 * (1/(-k[3])),
								str3 * (1/(-k[3])),
								str3 * (1/(k[3])),
								str3 * (1/(k[3])),
								str3 * (1/(-k[3])),
								str3 * (1/(k[3])),]
				str_lst = append_str_second(str_lst,j[3],k[3])

				for l in range(0,8):
					if(freq_lst[l] == 0):
						H.append([str_lst[l]*op_lst[l] ,'cos(' + str(freq_lst[l]) + '*t) + (0 + 1j)*sin(' + str(freq_lst[l]) + '*t)'])
						H0 += op_lst[l]*0.1
	return [H,H0]
				
#Defining Hamiltonian

#First need to define the list of operators for this system. For the first approximation we will ony use the firs integral.
print("Begining Two Body Simulation\nDefining Hamiltonian")
t0 = time.time() 
str_op_freq_lst 	= [] # [names,strengths,operator,frequency]
str_op_freq_lst 	= append_op(q1	,omega1,g, 'q1',q4 	,omega4 ,1,'q4' 	,str_op_freq_lst)
str_op_freq_lst 	= append_op(q2 	,omega2,g, 'q2',q4 	,omega4 ,1,'q4' 	,str_op_freq_lst)

#str_op_freq_lst 	= append_cos_drive_single(EJ,omega2,str_op_freq_lst)
#str_op_freq_lst 	= append_sin_drive_single_negitive(EJ,omega1,str_op_freq_lst)
str_op_freq_lst 	= append_cos_sin_drive_double_negitive(EJ,omega2,omega1,str_op_freq_lst)

#Now need to input this list of operators into methods to generate the sums in the Hamiltonian.
#Will also add an anharmonic term to this system to ensure the lowest two levels are protected.

H = []

# Now append the rest of the Dyson series expansion
D2 = Dyson_second_approx(str_op_freq_lst,H) 
H = D2[0]
H1 = D2[1]

H.append([U*q1.dag()*q1.dag()*q1*q1 + U*q2.dag()*q2.dag()*q2*q2,'cos(' + str(0) + '*t) + (0 + 1j)*sin(' + str(0) + '*t)'])
H1 += U*q1.dag()*q1.dag()*q1*q1 + U*q2.dag()*q2.dag()*q2*q2
#print(H1)
#print((q1+q1.dag())*(q2+q2.dag()))
#print(inital_state)


#Integrating Hamiltonian
print("Integrating Hamiltonian")

t1 = time.time()
result = mesolve(H1,inital_state,tlist1,c_ops,obs_ops,options=Options(nsteps = 20000,store_states = True)) # Perform the integration using qutip
tf = time.time()
print("Defining Hamiltonian Took:%f s"%(t1-t0))
print("Integration Took:%f s"%(tf-t1))
print("Simulation Took:%f"%(tf-t0))

print("Outputing Results")
out2(result)

print("Plotting Results")
plot_data(result)

print("Done")
print("===========================")