import numpy as np
from qutip import *
import matplotlib.pyplot as plt

#Method to plot all of the given data

def plot_data(results):
	Output_str 		= 'Output/Images/'

#plot the occupation probabilities

	plt.plot(results.expect[0],label='Qubit 1')
	plt.plot(results.expect[1],label='Qubit 2')
	plt.plot(results.expect[2],label='Qubit 4')
	plt.legend()
	plt.title('Occupation Probability')
	plt.savefig(Output_str + "Occupation_Probability.png")
	plt.clf()

