from qutip import *
from math import *

#Define all of the frequecnies we will need
omega1 = 4
omega2 = 5
omega3 = 7
omega4 = 17

omegad = omega1

freq_lst = [];oper_lst = []

#Define operators to use
dim = 2

a = destroy(dim)

q1 = tensor(a,qeye(dim),qeye(dim))
q2 = tensor(qeye(dim),a,qeye(dim))
q4 = tensor(qeye(dim),qeye(dim),a)

i_d = tensor(qeye(dim),qeye(dim),qeye(dim))

#define all methods 

def append_op(op1,freq1,op2,freq2,lst):
	for i in [[op1,-1*freq1],[op1.dag(),freq1]]:
		for j in [[op2,-1*freq2],[op2.dag(),freq2]]:
			lst.append([i[0]*j[0],i[1]+j[1]])
	return lst

test = []

test = append_op(q1,omega1,q4,omega4,test)
test = append_op(q4,omega4,i_d,omegad,test)
print(test)






