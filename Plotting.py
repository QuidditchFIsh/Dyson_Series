import numpy as np
from qutip import *
import matplotlib.pyplot as plt

#Method to plot all of the given data

def plot_data(results,sim):
	Output_str 		= 'Output/Images/' + sim +'/'

#plot the occupation probabilities

	plt.plot(results.expect[0],label='Qubit 1')
	plt.plot(results.expect[1],label='Qubit 2')
	plt.plot(results.expect[2],label='Qubit 4')
	plt.legend()
	plt.title('Occupation Probability')
	plt.savefig(Output_str + "Occupation_Probability.png")
	plt.clf()

#plotting the expectation values for the Pauli matricies 


	plt.plot(results.expect[3],label='SX')
	plt.plot(results.expect[6],label='SY')
	plt.plot(results.expect[9],label='SZ')
	plt.legend()
	plt.title('Qubit 1 Pauli matricies')
	plt.savefig(Output_str + "Qubit_1_XYZ.png")
	plt.clf()

	plt.plot(results.expect[4],label='SX')
	plt.plot(results.expect[7],label='SY')
	plt.plot(results.expect[10],label='SZ')
	plt.legend()
	plt.title('Qubit 2 Pauli matricies')
	plt.savefig(Output_str + "Qubit_2_XYZ.png")
	plt.clf()

	plt.plot(results.expect[5],label='SX')
	plt.plot(results.expect[8],label='SY')
	plt.plot(results.expect[11],label='SZ')
	plt.legend()
	plt.title('Qubit 4 Pauli matricies')
	plt.savefig(Output_str + "Qubit_4_XYZ.png")
	plt.clf()

#plotting the pauli matricies against each other for qubit 1 and 2


	plt.plot(results.expect[3],label='Qubit 1')
	plt.plot(results.expect[4],label='Qubit 2')
	plt.legend()
	plt.title('SigmaX')
	plt.savefig(Output_str + "SigmaX.png")
	plt.clf()

	plt.plot(results.expect[6],label='Qubit 1')
	plt.plot(results.expect[7],label='Qubit 2')
	plt.legend()
	plt.title('SigmaY')
	plt.savefig(Output_str + "SigmaY.png")
	plt.clf()

	plt.plot(results.expect[9],label='Qubit 1')
	plt.plot(results.expect[10],label='Qubit 2')
	plt.legend()
	plt.title('SigmaZ')
	plt.savefig(Output_str + "SigmaZ.png")
	plt.clf()
