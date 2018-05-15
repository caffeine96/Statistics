from __future__ import division
import matplotlib.pyplot as plt
import collections

state = 100
m= 2**31-1
a = 7**5
stateval=[]
def randomgen():
	global state
	state = (state*a)%m  
	
for i in xrange(0,10000):
	randomgen()
	stateval.append(state)
	
plt.hist(stateval)
plt.show()

mean = sum(stateval)/len(stateval)
ana_mean = (max(stateval)+min(stateval))/2
print "Mean: "+ str(mean)
print "Analytical Mean: " + str(ana_mean)

variance = sum([(xi-mean)**2 for xi in stateval]) / len(stateval)
ana_variance = ((max(stateval)-min(stateval))**2)/2
print "Variance: " + str(variance)
print "Analytical Variance: " + str(ana_variance) 