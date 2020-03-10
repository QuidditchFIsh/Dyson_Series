import numpy as np
from qutip import *
import matplotlib.pyplot as plt
def out(result_1):
	Output_str 		= 'Output/Data/'
#Outputing Data
	with open(Output_str + 'ocp_q1.dat','w') as fileq1:
		for j in result_1.expect[0]:
			fileq1.write(str(j) + "\n")

	with open(Output_str + 'ocp_q2.dat','w') as fileq2:
		for j in result_1.expect[1]:
			fileq2.write(str(j) + "\n")

	with open(Output_str + 'ocp_q4.dat','w') as fileq4:
		for j in result_1.expect[2]:
			fileq4.write(str(j) + "\n")


	with open(Output_str + 'sx_q1.dat','w') as filesx1:
		for j in result_1.expect[3]:
			filesx1.write(str(j) + "\n")

	with open(Output_str + 'sx_q2.dat','w') as filesx2:
		for j in result_1.expect[4]:
			filesx2.write(str(j) + "\n")

	with open(Output_str + 'sx_q4.dat','w') as filesx4:
		for j in result_1.expect[5]:
			filesx4.write(str(j) + "\n")


	with open(Output_str + 'sy_q1.dat','w') as filesy1:
		for j in result_1.expect[6]:
			filesy1.write(str(j) + "\n")

	with open(Output_str + 'sy_q2.dat','w') as filesy2:
		for j in result_1.expect[7]:
			filesy2.write(str(j) + "\n")

	with open(Output_str + 'sy_q4.dat','w') as filesy4:
		for j in result_1.expect[8]:
			filesy4.write(str(j) + "\n")


	with open(Output_str + 'sz_q1.dat','w') as filesz1:
		for j in result_1.expect[9]:
			filesz1.write(str(j) + "\n")

	with open(Output_str + 'sz_q2.dat','w') as filesz2:
		for j in result_1.expect[10]:
			filesz2.write(str(j) + "\n")

	with open(Output_str + 'sz_q4.dat','w') as filesz4:
		for j in result_1.expect[11]:
			filesz4.write(str(j) + "\n")



def out2(result_1,sim):
	Output_str 		= 'Output/Data/'+ sim + '/'
#Outputing Data
	with open(Output_str + 'ocp_q1.dat','w') as fileq1:
		for j in result_1.expect[0]:
			fileq1.write(str(j) + "\n")

	with open(Output_str + 'ocp_q2.dat','w') as fileq2:
		for j in result_1.expect[1]:
			fileq2.write(str(j) + "\n")

	with open(Output_str + 'ocp_q4.dat','w') as fileq4:
		for j in result_1.expect[2]:
			fileq4.write(str(j) + "\n")


#
	with open(Output_str + 'sx_q1.dat','w') as filesx1:
		for j in result_1.expect[3]:
			filesx1.write(str(j) + "\n")

	with open(Output_str + 'sx_q2.dat','w') as filesx2:
		for j in result_1.expect[4]:
			filesx2.write(str(j) + "\n")

	with open(Output_str + 'sx_q4.dat','w') as filesx4:
		for j in result_1.expect[5]:
			filesx4.write(str(j) + "\n")


#
	with open(Output_str + 'sy_q1.dat','w') as filesy1:
		for j in result_1.expect[6]:
			filesy1.write(str(j) + "\n")

	with open(Output_str + 'sy_q2.dat','w') as filesy2:
		for j in result_1.expect[7]:
			filesy2.write(str(j) + "\n")

	with open(Output_str + 'sy_q4.dat','w') as filesy4:
		for j in result_1.expect[8]:
			filesy4.write(str(j) + "\n")


#
	with open(Output_str + 'sz_q1.dat','w') as filesz1:
		for j in result_1.expect[9]:
			filesz1.write(str(j) + "\n")

	with open(Output_str + 'sz_q2.dat','w') as filesz2:
		for j in result_1.expect[10]:
			filesz2.write(str(j) + "\n")

	with open(Output_str + 'sz_q4.dat','w') as filesz4:
		for j in result_1.expect[11]:
			filesz4.write(str(j) + "\n")