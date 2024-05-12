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

def calculate_base(Ly: float, Lx: float, p: float, q: float) -> tuple:
    bx = Lx * ((100-p)/100)
    by = Ly * ((100-q)/100)
    return bx, by

def calculate_amount_of_series(Dx: float, bx: float, Dy: float, by: float)-> tuple:
    ny = math.ceil(Dy/by)
    nx = math.ceil(Dx/bx + 4)
    return ny, nx

def check_interval(dtx: float, cam: Camera):
    if dtx >= cam.get_cycle():
        return True
    else:
        return False

def calculate_Dx_Dy(point_1: tuple, point_2: tuple):
    Dx = abs(point_1[0] - point_2[0])
    Dy = abs(point_1[1] - point_2[1])
    return Dx, Dy

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
    bx = Dx/nx - 4
    p = 100 - 100*bx/Lx
    q = 100 - 100*by/Ly
    return bx, by, p, q

def recalc_after_height_change(camera: Camera, velocity: float, p: float, q: float, plane: Plane, point_1: tuple, point_2: tuple, hmin: float, hmax: float, height: float):
        gsd = camera.get_pixel_size() * height / camera.get_focal_length()
        Lx, Ly = calculate_range(gsd, camera)
        bx, by = calculate_base(Ly, Lx, p, q)
        Dx, Dy = calculate_Dx_Dy(point_1, point_2)
        ny, nx = calculate_amount_of_series(Dx, bx, Dy, by)
        bx, by, p, q = recalc_after_ceil(nx, ny, bx, by, Dx, Dy, Lx, Ly)
        n = nx * ny

        if velocity > plane.get_velocity_max():
                velocity = .95* plane.get_velocity_max()
                print("Prędkość jest zbyt duża dla wybranego samolotu. Zmniejszam prędkość.")

        dtx = bx / velocity

        if dtx < camera.get_cycle():
                velocity = calculate_max_velocity(camera, bx)
                print(f"Kamera nie nadąża. Prędkość zmniejszona.")

        return gsd, Lx, Ly, bx, by, nx, ny, n

def calculate(gsd: float, camera: Camera, velocity: float, p: float, q: float, plane: Plane, point_1: tuple, point_2: tuple, hmin: float, hmax: float):
    height = calculate_height(gsd, camera)
    bool_height = check_height(height, hmin, hmax, plane)    
    Lx, Ly = calculate_range(gsd, camera)
    bx, by = calculate_base(Ly, Lx, p, q)
    Dx, Dy = calculate_Dx_Dy(point_1, point_2)
    ny, nx = calculate_amount_of_series(Dx, bx, Dy, by)
    bx, by, p, q = recalc_after_ceil(nx, ny, bx, by, Dx, Dy, Lx, Ly)
    n = nx * ny

    if velocity > plane.get_velocity_max():
        velocity = .95* plane.get_velocity_max()
        print("Prędkość jest zbyt duża dla wybranego samolotu. Zmniejszam prędkość.")

    dtx = bx / velocity
    bool_interval = check_interval(dtx, camera)

    if bool_interval == False:
        velocity = calculate_max_velocity(camera, bx)
        print(f"Interwał zbyt mały. Prędkość zmniejszona.")

    if bool_height == False:
        height = calculate_max_height(plane, hmin, hmax)
        print(f"Zbyt duża wysokość. Zmniejszono wysokość lotu.")
        gsd, Lx, Ly, bx, by, nx, ny, n = recalc_after_height_change(camera, velocity, p, q, plane, point_1, point_2, hmin, hmax, height)
        print("Przeliczono ponownie parametry nalotu.")
     
    return velocity, height, gsd, Lx, Ly, bx, by, nx, ny, n

def calculate_time(nx: int, ny: int, bx: float, plane: Plane) -> float:
    limit = 1.05
    min_interval = limit * bx / plane.get_velocity_max()
    n = nx * ny
    time = (n - 1) * min_interval + 140 * (ny - 1)
    return time

