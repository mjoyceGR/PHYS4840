program SolveMassConservation
    implicit none
    real(8) :: r, m, dr, k1, k2, k3, k4, r_end
    real(8) :: rho_c, R, rho, pi
    integer :: n, i
    
    ! Constants
    pi = 4.0d0 * atan(1.0d0)
    rho_c = 1.0d0     ! Central density (arbitrary units)
    R = 10.0d0        ! Radius of the star (arbitrary units)
    
    ! Initial conditions
    r = 0.0d0
    m = 0.0d0
    dr = 0.01d0
    r_end = R
    n = int((r_end - r) / dr)
    
    ! Open output file
    open(unit=10, file="mass_profile.dat", status="replace")
    write(10,*) "r m"
    write(10,*) r, m

    ! RK4 integration loop
    do i = 1, n
        rho = density_profile(r, rho_c, R)
        k1 = dr * (4.0d0 * pi * r**2 * rho)
        
        rho = density_profile(r + 0.5d0 * dr, rho_c, R)
        k2 = dr * (4.0d0 * pi * (r + 0.5d0 * dr)**2 * rho)
        
        rho = density_profile(r + 0.5d0 * dr, rho_c, R)
        k3 = dr * (4.0d0 * pi * (r + 0.5d0 * dr)**2 * rho)
        
        rho = density_profile(r + dr, rho_c, R)
        k4 = dr * (4.0d0 * pi * (r + dr)**2 * rho)
        
        m = m + (k1 + 2.0d0*k2 + 2.0d0*k3 + k4) / 6.0d0
        r = r + dr
        
        write(10,*) r, m
    end do

    close(10)
    print *, "Mass profile saved to mass_profile.dat"
    
contains

    function density_profile(r, rho_c, R) result(rho)
        implicit none
        real(8), intent(in) :: r, rho_c, R
        real(8) :: rho
        if (r < R) then
            rho = rho_c * (1.0d0 - r / R)
        else
            rho = 0.0d0
        end if
    end function density_profile

end program SolveMassConservation
