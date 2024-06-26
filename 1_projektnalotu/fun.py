from camsandplanes import *
import math

def calculate_height(gsd: float, camera: Camera) -> float:
    height = camera.get_focal_length() * gsd / camera.get_pixel_size()
    return height

def check_height(height: float, hmin: float, hmax: float, plane: Plane) -> bool:
    average_height = (hmin + hmax)/2
    absolutna_height = height + average_height
    if absolutna_height > plane.get_ceiling(): 
        return False
    else:
        return True

def calculate_range(gsd: float, camera: Camera) -> tuple:
    Lx = camera.get_frame_short() * gsd
    Ly = camera.get_frame_long() * gsd
    return Lx, Ly

def calculate_base(Lx: float, Ly: float, p: float, q: float) -> tuple:
    bx = Lx * ((100-p)/100)
    by = Ly * ((100-q)/100)
    return bx, by

def calculate_amount_of_series(bx, by, Dx, Dy):
    ny = math.ceil(Dy/by)
    nx = math.ceil(Dx/bx + 4)
    return nx, ny

def check_interval(dtx: float, cam: Camera):
    if dtx >= cam.get_cycle():
        return True
    else:
        return False

def calculate_Dx_Dy(point_1: tuple, point_2: tuple):
    length_1 = abs(point_1[0] - point_2[0])
    length_2 = abs(point_1[1] - point_2[1])
    orientation = 0
    if length_1 >= length_2:
         orientation = 'v'
         return length_1, length_2, orientation
    else:
        orientation = 'h'
        return length_2, length_1, orientation

def calculate_max_velocity(camera: Camera, bx: float):
    max_freq = camera.get_cycle()
    max_velocity = bx / max_freq
    limit = .95
    return limit * max_velocity

def calculate_max_height(plane: Plane, hmin: float, hmax: float):
    avg_height = (hmin + hmax)/2
    height = plane.get_ceiling() - avg_height
    limit = .95
    return limit * height

def recalc_after_ceil(nx: int, ny: int, bx: float, by: float, Dx: float, Dy: float, Lx: float, Ly: float):
    by = Dy/ny
    bx = Dx/(nx - 4)
    p = 100 - 100*bx/Lx
    q = 100 - 100*by/Ly
    return bx, by, p, q

def recalc_after_height_change(camera: Camera, velocity: float, p: float, q: float, plane: Plane, point_1: tuple, point_2: tuple, hmin: float, hmax: float, height: float):
        gsd = camera.get_pixel_size() * height / camera.get_focal_length()
        Lx, Ly = calculate_range(gsd, camera)
        bx, by = calculate_base(Lx, Ly, p, q)
        Dx, Dy, _ = calculate_Dx_Dy(point_1, point_2)
        nx, ny = calculate_amount_of_series(bx, by, Dx, Dy)
        bx, by, p, q = recalc_after_ceil(nx, ny, bx, by, Dx, Dy, Lx, Ly)
        n = nx * ny

        if velocity > plane.get_velocity_max():
                velocity = .95* plane.get_velocity_max()

        dtx = bx / velocity

        if dtx < camera.get_cycle():
                velocity = calculate_max_velocity(camera, bx)

        return gsd, Lx, Ly, bx, by, nx, ny, n

def calculate(gsd: float, camera: Camera, velocity: float, p: float, q: float, plane: Plane, point_1: tuple, point_2: tuple, hmin: float, hmax: float):
    height = calculate_height(gsd, camera)
    bool_height = check_height(height, hmin, hmax, plane)
    Dx, Dy, orientation = calculate_Dx_Dy(point_1, point_2)
    Lx, Ly = calculate_range(gsd, camera)
    bx0, by0 = calculate_base(Lx, Ly, p, q)
    nx, ny = calculate_amount_of_series(bx0, by0, Dx, Dy)
    bx, by, p, q = recalc_after_ceil(nx, ny, bx0, by0, Dx, Dy, Lx, Ly)
    n = nx * ny
    comms = []

    if velocity > plane.get_velocity_max():
        velocity = .95* plane.get_velocity_max()
        comms.append("Wybrana prędkość jest zbyt duża dla wybranego samolotu. Zmniejszono prędkość.")

    dtx = bx / velocity
    bool_interval = check_interval(dtx, camera)

    if bool_interval == False:
        velocity = calculate_max_velocity(camera, bx)
        comms.append("Interwał czasu pomiędzy ekspozycjami jest mniejszy od cyklu pracy kamery. Zmniejszono prędkość.")

    if bool_height == False:
        height = calculate_max_height(plane, hmin, hmax)
        gsd, Lx, Ly, bx, by, nx, ny, n = recalc_after_height_change(camera, velocity, p, q, plane, point_1, point_2, hmin, hmax, height)
    
    k = K(bx, by, n, Dx, Dy)
    return velocity, height, gsd, Lx, Ly, bx, by, nx, ny, n, p, q, bx0, by0, comms, orientation, Dx, Dy, k

def calculate_time(n, ny, bx, velocity) -> float:
    arc_time = 140*(ny-1)
    time = (n * bx) / velocity + arc_time
    return time

def K(bx, by, n, Dx, Dy) -> float:
    pn = bx * by
    pt = Dx * Dy
    k = n * pn / pt
    return k

