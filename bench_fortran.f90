program main
  integer, parameter :: nrepeat = 50
  integer :: i, repeat, times, ntimes
  real :: total_elapsed, elapsed, elapsed_min

  write(*,*) '% Fortran'
  write(*,*) '% Size, Time [ms]'
  do i = 1, 500, 20
     elapsed_min = 1e9
     total_elapsed = 0
     do repeat = 1, nrepeat 
        call bench(i, elapsed, 1)
        elapsed_min = min(elapsed_min, elapsed)
     end do
     write(*,*) i, elapsed_min
  end do

contains

  subroutine bench(i, elapsed, ntimes)
    integer, intent(in) :: i, ntimes

    real, intent(out) :: elapsed
    integer :: start, finish, count_rate, k

    real, dimension(i, i) :: m1, m2, r
    real :: alpha, beta

    call nonrandom_fill(i, m1)
    call nonrandom_fill(i, m2)

    call system_clock(start, count_rate)

    do k = 1, ntimes
       alpha = 1.0
       beta = 0.0
       call sgemm('N', 'N', i, i, i, alpha, m1, i, m2, i, beta, r, i)
    end do

    call system_clock(finish, count_rate)

    elapsed = (finish - start) * 1d0 / count_rate / ntimes
  end subroutine bench

  subroutine nonrandom_fill(i, m1)
    integer, intent(in) :: i
    real, intent(out), dimension(i,i) :: m1
    integer :: p, q
    do p = 1, i
       do q = 1, i
          m1(p, q) = p + i*q
       end do
    end do
  end subroutine nonrandom_fill
end program main
