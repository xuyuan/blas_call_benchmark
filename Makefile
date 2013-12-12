all: bench

bench_fortran: bench_fortran.f90
	gfortran -O3 -o $@ $^ -lblas

bench: bench_fortran
	python bench_numpy.py > out_numpy.dat
	python bench_blas.py > out_blas.dat
	./bench_fortran > out_fortran.dat
	python plot.py

zip:
	rm -f blas_call_benchmark.zip
	zip -v9 blas_call_benchmark.zip bench_fortran.f90 bench_numpy.py \
		bench_blas.py plot.png Makefile plot.py README.rst

clean:
	rm -f blas_call_benchmark.zip *.dat bench_fortran plot.png

.PHONY: bench zip clean
