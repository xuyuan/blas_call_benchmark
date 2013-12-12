import timeit
import numpy as np
import ctypes
import sys

libblas_name = "libblas.so"
if len(sys.argv) > 1:
    libblas_name = sys.argv[1]

_blaslib = ctypes.cdll.LoadLibrary(libblas_name)


def mul(m1, m2, i, r):
    no_trans = ctypes.c_char("n")
    n = ctypes.c_int(i)
    one = ctypes.c_float(1.0)
    zero = ctypes.c_float(0.0)

    _blaslib.sgemm_(
        ctypes.byref(no_trans),
        ctypes.byref(no_trans),
        ctypes.byref(n),
        ctypes.byref(n),
        ctypes.byref(n), 
        ctypes.byref(one),
        m1.ctypes.data_as(ctypes.c_void_p),
        ctypes.byref(n), 
        m2.ctypes.data_as(ctypes.c_void_p),
        ctypes.byref(n),
        ctypes.byref(zero), 
        r.ctypes.data_as(ctypes.c_void_p),
        ctypes.byref(n))


results = []

print "% CTypes & " + libblas_name
print "% Size, Time [ms]"

for i in xrange(1, 500, 20):
    m1 = np.random.rand(i,i).astype(np.float32)
    m2 = np.random.rand(i,i).astype(np.float32)
    r = np.random.rand(i,i).astype(np.float32)

    timer = timeit.Timer("mul(m1, m2, i, r)",
                         "import numpy; from __main__ import m1, m2, r, i, mul")

    print i, min(timer.repeat(50, 1))
