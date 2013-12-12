all: bench_fortran bench_numpy bench_blas bench_openblas plot

bench_fortran: bench_fortran.f90
	gfortran -O3 -o $@ $^ -lblas
	./bench_fortran > out_fortran.dat

bench_numpy:
	python bench_numpy.py > out_numpy.dat	

bench_blas:
	python bench_blas.py > out_blas.dat

bench_openblas:
	python bench_blas.py /usr/lib/openblas-base/libopenblas.so.0 > out_openblas.dat

plot:
	python plot.py

clean:
	rm -f *.dat bench_fortran plot.png

