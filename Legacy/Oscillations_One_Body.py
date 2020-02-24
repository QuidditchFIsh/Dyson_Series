from math import *
from qutip import *
import numpy as np

#This code is for a one body interaction. For two body interactions we would need
#A more complicated loop.

#Define all of the frequecnies we will need
omega1 = 4
omega2 = 5
omega3 = 7
omega4 = 17

omegad1 = omega1
omegad2 = omega2 

#Define operators to use
dim = 2

a = destroy(dim)

q1 = tensor(a,qeye(dim),qeye(dim),qeye(dim))
q2 = tensor(qeye(dim),a,qeye(dim),qeye(dim))
q3 = tensor(qeye(dim),qeye(dim),a,qeye(dim))
q4 = tensor(qeye(dim),qeye(dim),qeye(dim),a)

g = 0.1

EJ = 2

freq_lst = [];oper_lst = []
I = tensor(qeye(dim),qeye(dim),qeye(dim),qeye(dim))

#define all methods 

def append_op(op1,freq1,op2,freq2,lst):
	for i in [[op1,-1*freq1],[op1.dag(),freq1]]:
		for j in [[op2,-1*freq2],[op2.dag(),freq2]]:
			lst.append([(1/freq2)*i[0]*j[0],i[1]+j[1]])
	return lst

def append_op_sin(op1,freq1,op2,freq2,lst):
	for i in [[op1,-1*freq1],[op1.dag(),freq1]]:
		for j in [[op2,-1*freq2],[-1*op2.dag(),freq2]]:
			lst.append([(0 - 1j)*i[0]*j[0],i[1]+j[1]])
	return lst

def exponential(t,args):
	return (cos(args[0] * t) - (0 + 1j) * sin(args[0] * t))

op_freq_lst = []
op_freq_lst = append_op(g*q1,omega1,g*q4,omega4,op_freq_lst)
op_freq_lst = append_op(g*q2,omega2,g*q4,omega4,op_freq_lst)
op_freq_lst = append_op(EJ*q4,omega4,I,omegad1,op_freq_lst)
#op_freq_lst = append_op_sin(EJ*q4,omega4,I,omegad2,op_freq_lst)

#loop through the list to calculate each of the 
k=0
combinations = []
for i in range(0,len(op_freq_lst)):
	for j in range(k,len(op_freq_lst)):
		combinations.append([i+1,j+1,op_freq_lst[i][1] + op_freq_lst[j][1]])
		combinations.append([-(i+1),j+1,-1*op_freq_lst[i][1] + op_freq_lst[j][1]])
		combinations.append([i+1,-(j+1),op_freq_lst[i][1] + -1*op_freq_lst[j][1]])
		combinations.append([-(i+1),-(j+1),-1*op_freq_lst[i][1] + -1*op_freq_lst[j][1]])
	k = k + 1

#Now create the Hamiltonian which corresponds to these non rotating terms
H = 0
op1 = 0;op2 = 0

for i in combinations:
	if (i[2]==0):
		#if(abs(i[0]) != abs(i[1])):
		#Determine if we need to conjugate the operator
		if(i[0] < 0):
			op1 = op_freq_lst[abs(i[0])-1][0].dag()
		else:
			 op1 = op_freq_lst[abs(i[0])-1][0]
		if(i[1] < 0):
			op2 = op_freq_lst[abs(i[1])-1][0].dag()
		else:
			 op2 = op_freq_lst[abs(i[1])-1][0]
		H += op1*op2


#Define all of the variables needed for qutip
#print(H)
one = basis(dim,1)
zero = basis(dim,0)

inital_state = tensor(zero,zero,zero,zero)

#operators to measure
Id = qeye(dim)
sx1 = tensor(sigmax(),Id,Id,Id)
sx2 = tensor(Id,sigmax(),Id,Id)
sx4 = tensor(Id,Id,Id,sigmax())

sy1 = tensor(sigmay(),Id,Id,Id)
sy2 = tensor(Id,sigmay(),Id,Id)
sy4 = tensor(Id,Id,Id,sigmay())

sz1 = tensor(sigmaz(),Id,Id,Id)
sz2 = tensor(Id,sigmaz(),Id,Id)
sz4 = tensor(Id,Id,Id,sigmaz())

obs_ops =[q1.dag()*q1,q2.dag()*q2,q4.dag()*q4,sx1,sx2,sx4,sy1,sy2,sy4,sz1,sz2,sz4]
c_ops = []
tlist1 = np.linspace(0,500,100) # time to integrate over
print(H)
result_1 = mesolve(H,inital_state,tlist1,c_ops,obs_ops,options=Options(nsteps = 20000,store_states = True)) # Perform the integration using qutip

with open('ocp_q1.dat','w') as fileq1:
	for j in result_1.expect[0]:
		fileq1.write(str(j) + "\n")

with open('ocp_q2.dat','w') as fileq2:
	for j in result_1.expect[1]:
		fileq2.write(str(j) + "\n")

with open('ocp_q4.dat','w') as fileq4:
	for j in result_1.expect[2]:
		fileq4.write(str(j) + "\n")


with open('sx_q1.dat','w') as filesx1:
	for j in result_1.expect[3]:
		filesx1.write(str(j) + "\n")

with open('sx_q2.dat','w') as filesx2:
	for j in result_1.expect[4]:
		filesx2.write(str(j) + "\n")

with open('sx_q4.dat','w') as filesx4:
	for j in result_1.expect[5]:
		filesx4.write(str(j) + "\n")


with open('sy_q1.dat','w') as filesy1:
	for j in result_1.expect[6]:
		filesy1.write(str(j) + "\n")

with open('sy_q2.dat','w') as filesy2:
	for j in result_1.expect[7]:
		filesy2.write(str(j) + "\n")

with open('sy_q4.dat','w') as filesy4:
	for j in result_1.expect[8]:
		filesy4.write(str(j) + "\n")


with open('sz_q1.dat','w') as filesz1:
	for j in result_1.expect[9]:
		filesz1.write(str(j) + "\n")

with open('sz_q2.dat','w') as filesz2:
	for j in result_1.expect[10]:
		filesz2.write(str(j) + "\n")

with open('sz_q4.dat','w') as filesz4:
	for j in result_1.expect[11]:
		filesz4.write(str(j) + "\n")

