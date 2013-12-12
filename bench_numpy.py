import timeit
import numpy as np

results = []

print "% Numpy"
print "% Size, Time [ms]"

for i in xrange(1, 500, 20):
    m1 = np.random.rand(i,i).astype(np.float32)
    m2 = np.random.rand(i,i).astype(np.float32)

    timer = timeit.Timer("numpy.dot(m1, m2)",
                         "import numpy; from __main__ import m1, m2")

    print i, min(timer.repeat(50, 1))
