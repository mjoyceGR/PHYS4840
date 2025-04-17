program Solver
    implicit none
    real(8) :: r, m, dr, k1, k2, k3, k4, r_end
    real(8) :: rho_c, R_star, rho, pi
    integer :: n, i
    
    ! Constants
    pi = 4.0d0 * atan(1.0d0)
    rho_c = 1.0d0     ! Central density (arbitrary units)
    R_star = 10.0d0        ! R_staradius of the star (arbitrary units)
    
    ! Initial conditions
    r = 0.0d0
    m = 0.0d0
    dr = 0.01d0
    r_end = R_star
    n = int((r_end - r) / dr)
    
    ! Open output file
    open(unit=10, file="profile.dat", status="replace")
    write(10,*) "r m"
    write(10,*) r, m

    ! R_starK4 integration loop
    do i = 1, n
        rho = density_profile(r, rho_c, R_star)
        k1 = dr * (4.0d0 * pi * r**2 * rho)
        
        rho = density_profile(r + 0.5d0 * dr, rho_c, R_star)
        k2 = dr * (4.0d0 * pi * (r + 0.5d0 * dr)**2 * rho)
        
        rho = density_profile(r + 0.5d0 * dr, rho_c, R_star)
        k3 = dr * (4.0d0 * pi * (r + 0.5d0 * dr)**2 * rho)
        
        rho = density_profile(r + dr, rho_c, R_star)
        k4 = dr * (4.0d0 * pi * (r + dr)**2 * rho)
        
        m = m + (k1 + 2.0d0*k2 + 2.0d0*k3 + k4) / 6.0d0
        r = r + dr
        
        write(10,*) r, m
    end do

    close(10)
    print *, "Profile saved to profile.dat"
    
contains

    function density_profile(r, rho_c, R_star) result(rho)
        implicit none
        real(8), intent(in) :: r, rho_c, R_star
        real(8) :: rho
        if (r < R_star) then
            rho = rho_c * (1.0d0 - r / R_star)
        else
            rho = 0.0d0
        end if
    end function density_profile

end program Solver
