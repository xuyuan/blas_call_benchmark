all: bench_fortran bench_numpy bench_blas bench_openblas bench_atlas bench_numpy_py plot

bench_fortran: bench_fortran.f90
	gfortran -O3 -o $@ $^ -lblas
	./bench_fortran > out_fortran.dat

bench_numpy_py:
	python bench_numpy.py numpy.core.multiarray.dot > out_numpy_py.dat

bench_numpy:
	python bench_numpy.py > out_numpy.dat	

bench_blas:
	python bench_blas.py > out_blas.dat

bench_atlas:
	python bench_blas.py /usr/lib/atlas-base/atlas/libblas.so.3 > out_atlas.dat

bench_openblas:
	python bench_blas.py /usr/lib/openblas-base/libopenblas.so.0 > out_openblas.dat

plot:
	python plot.py

clean:
	rm -f *.dat bench_fortran plot.png

