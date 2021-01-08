import matplotlib.pyplot as plt
from scipy.stats import expon
import csv
import sys
import random

import numpy as np

# plot distribution
'''poss=[]
m = int(sys.argv[1])
c = int(sys.argv[2])
with open("distribution") as f:
    line = f.readline()
    poss.extend(line.split(' '))
    poss = [float(x) for x in poss[:-1]]

# x axis values
x = range(0,m-c)
# corresponding y axis values
y = poss

# plotting the points
plt.plot(x, y,marker='x', markerfacecolor='red', markersize=1)
plt.ylim(0,0.15)
plt.xlim(1,m-c)
# naming the x axis
plt.xlabel('user')
# naming the y axis
plt.ylabel('possibility')
# giving a title to my graph
plt.title('Distribution')
# function to show the plot
plt.show()'''

# generate distribution file
''''m = int(sys.argv[1])
c = int(sys.argv[2])
d = expon.rvs(size=m - c, loc=11000, scale=10000)
d = [abs(i) for i in d]
d.sort(reverse=True)
for i in range(0, int((m - c) / 10)):
    d[i]*= 10
random.shuffle(d)
ss = sum(d)
d /= ss
print max(d)
with open("distribution", "w") as f:
    for i in d:
        f.write("%s " % i)'''

#  generate corr file
'''m = int(sys.argv[1])
c = int(sys.argv[2])
rangeC = range(0, m)
corr = []
for i in range(0, c):
    x = random.choice(rangeC)
    corr.append(x)
    rangeC.remove(x)
for c in corr:
    print c'''

# generate users file
m = int(sys.argv[1])
c = int(sys.argv[2])
corr = []
poss = []
with open("corr") as f:
    corr = f.readlines()
    corr = [int(i) for i in corr]
with open("distribution") as f:
    line = f.readline()
    poss.extend(line.split(' '))
    poss = [float(x) for x in poss[:-1]]
corr.sort()
for i in corr:
    poss.insert(i, 0)
users = []
for i in range(0, 100000):
    x = np.random.choice(a=range(0, m), p=poss) #non-uniform distribution
    #x = np.random.choice(a=range(0, m))  # uniform distribution
    users.append(x)
for user in users:
    print user
