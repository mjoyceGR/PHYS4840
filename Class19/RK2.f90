program RungeKutta2
    implicit none
    real(8) :: t, x, dt, k1, k2, t_end
    integer :: n, i
    
    ! Define initial conditions
    t = 0.0d0      ! Initial time
    x = 1.0d0      ! Initial condition for x
    dt = 0.1d0     ! Time step
    t_end = 10.0d0 ! Final time
    
    ! Number of time steps
    n = 10000 !int((t_end - t) / dt)
    
    ! Open a file to store results
    open(unit=10, file="rk2_results.dat", status="replace")
    write(10,*) "t x"
    write(10,*) t, x
    
    ! RK2 integration loop
    do i = 1, n
        k1 = dt * (-x**3 + sin(t))
        k2 = dt * (-(x + 0.5d0*k1)**3 + sin(t + 0.5d0*dt))
        
        x = x + k2
        t = t + dt
        
        ! Write results to file
        write(10,*) t, x
    end do
    
    ! Close file
    close(10)
    
    print *, "Integration complete. Results saved to rk2_results.dat"
    
end program RungeKutta2