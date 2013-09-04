import numpy
import numpy
from matplotlib import pyplot as plt, rc

class Plotter:
	#def __init__(self,x_labels,y_labels):
	#	self.x_labels = x_labels
	#	self.y_labels = y_labels


	def plot(self,x, y, x_labels, y_labels):
		fig = plt.figure(figsize=(10, 8), dpi=80)
		graph = fig.add_subplot(111)
		graph.plot(x,y)
		plt.show()
		font = {'family':'Droid Sans', 'size': 8}
		rc('font', **font)
		graph.set_yticklabels(x_labels)
		graph.set_xticklabels(y_labels)
		