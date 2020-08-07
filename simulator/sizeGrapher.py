import matplotlib.pyplot as plt
import numpy as np
import sys

fc0 = []
fc750 = []
nenov = []
lra = []
zero = []

for line in sys.stdin:
	if "fc0" in line:
		fc0.append(int(line.split(": ")[1]))
	if "fc750" in line:
		fc750.append(int(line.split(": ")[1]))
	if "nenov" in line:
		nenov.append(int(line.split(": ")[1]))
	if "lra" in line:
		lra.append(int(line.split(": ")[1]))
		zero.append(0)
	#if "Min" in line:
	#	mins.append(int(line.split(": ")[1]))

x = np.linspace(0, 20, len(fc0))

plt.plot(x, zero, 'C1', label='LRA:0')
plt.plot(x, fc0, 'C2', label='FinalCache:0 & LRAwe:0')
plt.plot(x, lra, 'C5', label='LRA:3000')
plt.plot(x, nenov, 'C4', label='LRAwe:3000')
plt.plot(x, fc750, 'C3', label='FinalCache:750')

plt.annotate('LRA:0', xy=(10,100))
plt.annotate('FinalCache:0\n & LRAwe:0', xy=(5,1100))
plt.annotate('LRA:3000', xy=(17,3100))
plt.annotate('FinalCache:750\n & LRAwe:3000', xy=(13,5300))

#plt.plot(x, mins, '-r', label='Min')
#plt.title("FinalCache Max Size over Time")
plt.xlabel("Cache Operations")
plt.xticks([])
plt.ylabel("Max Size")
plt.legend()
plt.show()
