from __future__ import division
import matplotlib.pyplot as plt
import collections
import numpy as np
import matplotlib.mlab as mlab
from numpy import sqrt,cos,sin,log,pi

mu , sigma = 0 ,0.1
x = np.linspace(mu - 3*sigma,mu + 3*sigma,100)
plt.plot(x,mlab.normpdf(x,mu,sigma))
plt.show()

state = 100
m= 2**31-1
a = 7**5
stateval=[]
stateval2=[]

def randomgen():
	global state
	state = (state*a)%m  
	

def boxmuller(u1,u2):
	u1=np.asarray(u1)
	print type(u1)
	u2=np.asarray(u2)
	z1= sqrt(-2*log(u1+ 1e-12))*cos(2*pi*u2)
	z2= sqrt(-2*log(u1+ 1e-12))*sin(2*pi*u2)
	return z1,z2
	
for i in xrange(0,10000):
	randomgen()
	stateval.append(state/m)

for i in xrange(0,10000):
	randomgen()
	stateval2.append(state/m)

z1,z2 = boxmuller(stateval,stateval2)

plt.hist(stateval)
plt.subplot(221)
plt.hist(stateval)
plt.subplot(222)
plt.hist(stateval2)
plt.subplot(223)
plt.hist(z1)
plt.subplot(224)
plt.hist(z2)
plt.show()
