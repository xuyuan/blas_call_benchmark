import matplotlib.pyplot as plt
import numpy as np
import os
pwd = os.path.dirname(os.path.realpath(__file__))
data_files = [f for f in os.listdir(pwd) if os.path.isfile(os.path.join(pwd, f)) and f.endswith('.dat')]
print data_files

for f in data_files:
    data = np.loadtxt(f, comments='%')
    name = open(f, 'r').readline()[2:]
    plt.plot(data[:, 0], data[:, 1], '-x', label=name)

plt.legend(loc='lower right')
plt.xlabel('N')
plt.ylabel('time [s]')
plt.yscale('log')
plt.show()
plt.savefig('plot.png')
