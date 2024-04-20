from camsandplanes import Camera, Plane
import math

def calculate_height(gsd: float, camera: Camera) -> float:
    '''
    Funkcja oblicza wysokość lotu.

            Argumenty:
                    gsd (float): terenowy rozmiar piksela
                    camera (Camera): obiekt klasy Camera

            Zwraca:
                    height (float): wysokość lotu
    '''
    height = camera.focal_length * gsd / camera.pixel_size
    return height

def calculate_base_terrain_dimensions(Ly: float, Lx: float, p: float, q: float) -> tuple:
    '''
    Funkcja oblicza terenowe wymiary bazy fotografowania.

            Argumenty:
                    Ly (float): terenowy zasięg zdjęcia w poprzek kierunku lotu
                    Lx (float): terenowy zasięg zdjęcia wzdłuż kierunku lotu
                    p (float): pokrycie podłużne
                    q (float): pokrycie poprzeczne

            Zwraca:
                    bx (float): terenowy wymiar bazy fotografowania w poprzek kierunku lotu
                    by (float): terenowy wymiar bazy fotografowania wzdłuż kierunku lotu
    '''
    bx = Lx * ((100-p)/100)
    by = Ly * ((100-q)/100)
    return bx, by

def calculate_scale(height: float, camera: Camera) -> float:
    '''
    Funkcja oblicza skalę zdjęcia.

            Argumenty:
                    height (float): wysokość lotu
                    camera (Camera): obiekt klasy Camera

            Zwraca:
                    skala (float): skala zdjęcia
    '''
    skala = camera.focal_length / height
    return skala

def check_height(height: float, hmin: float, hmax: float, plane: Plane) -> bool:
    '''
    Funkcja sprawdza czy projektowana wysokość lotu jest możliwa dla wybranego samolotu.

            Argumenty:
                    height (float): projektowana wysokość lotu
                    hmin (float): minimalna wysokość terenu na obszarze opracowania
                    hmax (float): maksymalna wysokość terenu na obszarze opracowania
                    plane (Plane): obiekt klasy Plane

            Zwraca:
                    bool: True jeśli wysokość jest możliwa, False jeśli nie
    '''
    average_height = (hmin + hmax)/2
    absolutna_height = height + average_height
    if absolutna_height > plane.ceiling: 
        return False
    else:
        return True

def calculate_range(gsd: float, camera: Camera) -> tuple:
    '''
    Funkcja oblicza zasięg terenowy zdjęcia.

            Argumenty:
                    gsd (float): terenowy rozmiar piksela
                    camera (Camera): obiekt klasy Camera
            
            Zwraca:
                    Lx, Ly (float): terenowe wymiary zdjęcia
    '''
    Lx = camera.frame_short * gsd
    Ly = camera.frame_long * gsd
    return Lx, Ly

def calculate_base(Ly: float, Lx: float, p: float, q: float) -> tuple:
    '''
    Funkcja wyznacza terenowy wymiar baz fotografowania.
    
            Argumenty:
                    Ly (float): terenowy zasięg zdjęcia w poprzek kierunku lotu
                    Lx (float): terenowy zasięg zdjęcia wzdłuż kierunku lotu
                    p (float): pokrycie podłużne
                    q (float): pokrycie poprzeczne
            
            Zwraca:
                    bx, by (float): terenowe wymiary bazy fotografowania
    '''
    bx = Lx * ((100-p)/100)
    by = Ly * ((100-q)/100)
    return bx, by

def calculate_amount_of_series(Dx: float, bx: float, Dy: float, by: float)-> tuple:
    '''
    Funkcja wyznacza liczbę szeregów oraz liczbę zdjęć w pojedynczym szeregu.
    
            Argumenty:
            Dx (float): zasięg obszaru opracowania wzdłuż kierunku lotu
            bx (float): wymiar terenowy bazy podłużnej
            Dy (float): zasięg obszaru opracowania w poprzek kierunku lotu
            by (float): wymiar terenowy bazy poprzecznej

            Zwraca:
            ny (int): liczba szeregów
            nx (int): liczba zdjęć w pojedynczym szeregu
    '''
    ny = math.ceil(Dy/by)
    nx = math.ceil(Dx/bx + 4)
    return ny, nx

def check_interval(bx: float, v: float, cam: Camera):
    """
    Funkcja sprawdza czy odstęp między zdjęciami jest większy niż cykl kamery.

            Argumenty:
                    bx (float): terenowy wymiar bazy fotografowania w poprzek kierunku lotu
                    v (float): prędkość lotu
                    cam (Camera): obiekt klasy Camera
            
            Zwraca:
                    bool: True jeśli odstęp jest większy niż cykl, False jeśli nie
    """
    interval = bx / v
    if interval >= cam.cycle:
        return True
    else:
        return False

def calculate_number_of_photos(nx: int, ny: int):
    """
    Funkcja oblicza liczbę zdjęć w całym nalocie.
    """
    return nx * ny

def calculate(gsd: float, camera: Camera, velocity: float, p: float, q: float):
    '''
    Funkcja oblicza parametry nalotu.

            Argumenty:
                    gsd (float): terenowy rozmiar piksela
                    camera (Camera): obiekt klasy Camera
                    velocity (float): prędkość lotu
                    p (float): pokrycie podłużne
                    q (float): pokrycie poprzeczne

            Zwraca:
                    height (float): wysokość lotu
                    Lx (float): terenowy zasięg zdjęcia w poprzek kierunku lotu
                    Ly (float): terenowy zasięg zdjęcia wzdłuż kierunku lotu
                    bx (float): terenowy wymiar bazy fotografowania w poprzek kierunku lotu
                    by (float): terenowy wymiar bazy fotografowania wzdłuż kierunku lotu

    '''
    height = calculate_height(gsd, camera)
    Lx, Ly = calculate_range(gsd, camera)
    bx, by = calculate_base_terrain_dimensions(Ly, Lx, p, q)
    ny, nx = calculate_amount_of_series(Lx, bx, Ly, by)
    n = calculate_number_of_photos(nx, ny)
    # skala = calculate_scale(height, camera)
    # Bx = bx * skala
    # By = by * skala
    # tbx = Bx / velocity
    