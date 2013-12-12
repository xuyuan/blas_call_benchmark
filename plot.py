import matplotlib.pyplot as plt
import numpy as np

t_numpy = np.loadtxt('out_numpy.dat', comments='%')
t_blas = np.loadtxt('out_blas.dat', comments='%')
t_fortran = np.loadtxt('out_fortran.dat', comments='%')

plt.plot(t_numpy[:,0], t_numpy[:,1], 'b-x', label='Numpy')
plt.plot(t_blas[:,0], t_blas[:,1], 'g-x', label='Ctypes+Blas')
plt.plot(t_fortran[:,0], t_fortran[:,1], 'r-x', label='Fortran')
plt.legend(loc='lower right')
plt.xlabel('N')
plt.ylabel('time [s]')
plt.yscale('log')
plt.savefig('plot.png')
plt.show()
