from __future__ import division
import matplotlib.pyplot as plt
import collections
import numpy as np
import matplotlib.mlab as mlab
from numpy import sqrt,cos,sin,log,pi


state = 100
m= 2**31-1
a = 7**5
stateval=[]
stateval2=[]

def randomgen():
	global state
	state = (state*a)%m  
	
for j in xrange(0,10000):
	stateval.append(np.zeros((10000)))	
	for i in xrange(0,10000):
		randomgen()
		stateval[j][i]=(state/m)

new_x=np.zeros((10000))
for i in xrange(0,10000):	
	for j in xrange(0,10000):
		new_x[i]=(new_x[i] + stateval[j][i])%m

mean = sum(new_x)/len(new_x)
variance = sum([(xi-mean)**2 for xi in new_x]) / len(new_x)

z=np.zeros((10000))
for i in xrange(0,10000):
	z[i]= (new_x[i] - mean)/ sqrt(variance)

# z1,z2 = boxmuller(stateval,stateval2)

plt.hist(z)
plt.show()
# plt.subplot(221)
# plt.hist(stateval)
# plt.subplot(222)
# plt.hist(stateval2)
# plt.subplot(223)
# plt.hist(z1)
# plt.subplot(224)
# plt.hist(z2)
# plt.show()

