import timeit
import numpy as np
import sys

dot = 'numpy.dot'
if len(sys.argv) > 1:
    dot = sys.argv[1]

results = []

print "% " + dot
print "% Size, Time [ms]"

for i in xrange(1, 500, 20):
    m1 = np.random.rand(i, i).astype(np.float32)
    m2 = np.random.rand(i, i).astype(np.float32)

    timer = timeit.Timer(dot + "(m1, m2)",
                         "import numpy; from __main__ import m1, m2")

    print i, min(timer.repeat(50, 1))
