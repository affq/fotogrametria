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

def check_interval(dtx: float, cam: Camera):
    """
    Funkcja sprawdza czy odstęp między zdjęciami jest większy niż cykl kamery.

            Argumenty:
                    dtx (float): obliczony interwał czasu między zdjęciami
                    cam (Camera): obiekt klasy Camera
            
            Zwraca:
                    bool: True jeśli odstęp jest większy niż cykl, False jeśli nie
    """
    if dtx >= cam.cycle:
        return True
    else:
        return False

def calculate_number_of_photos(nx: int, ny: int):
    """
    Funkcja oblicza liczbę zdjęć w całym nalocie.
    """
    return nx * ny

def calculate_Dx_Dy(point_1: tuple, point_2: tuple):
    """
    Funkcja oblicza zasięg obszaru opracowania wzdłuż i poprzek kierunku lotu.
        
                Argumenty:
                        point_1 (tuple): współrzędne pierwszego punktu
                        point_2 (tuple): współrzędne drugiego punktu
                
                Zwraca:
                        Dx, Dy (float): zasięg obszaru opracowania wzdłuż i poprzek kierunku lotu
    """
    Dx = abs(point_1[0] - point_2[0])
    Dy = abs(point_1[1] - point_2[1])
    return Dx, Dy

def calculate_max_velocity(plane: Plane, camera: Camera, bx: float):
    max_freq = 1.1*(camera.cycle)
    max_velocity = bx / max_freq
    return max_velocity

def calculate_max_height(plane: Plane, hmin: float, hmax: float):
    avg_height = (hmin + hmax)/2
    height = .9*(plane.ceiling - avg_height)
    return height

def recalc_after_ceil(nx: int, ny: int, bx: float, by: float, Dx: float, Dy: float, Lx: float, Ly: float):
    """
    Funkcja ponownie liczy wymiary terenowe bazy oraz pokrycia po zaokrągleniu w górę liczby zdjęć.

        Argumenty:
                nx (int): liczba zdjęć w pojedynczym szeregu
                ny (int): liczba szeregów
                bx (float): terenowy wymiar bazy fotografowania w poprzek kierunku lotu
                by (float): terenowy wymiar bazy fotografowania wzdłuż kierunku lotu
                Dx (float): zasięg obszaru opracowania wzdłuż kierunku lotu
                Dy (float): zasięg obszaru opracowania w poprzek kierunku lotu
                Lx (float): terenowy zasięg zdjęcia w poprzek kierunku lotu
                Ly (float): terenowy zasięg zdjęcia wzdłuż kierunku lotu
        
        Zwraca:
                bx, by (float): terenowe wymiary bazy fotografowania
                p, q (float): pokrycie podłużne i poprzeczne
    """
    by = Dy/ny
    bx = Dx/nx - 4
    p = 100 - 100*bx/Lx
    q = 100 - 100*by/Ly
    return bx, by, p, q

def recalc_after_height_change(camera: Camera, velocity: float, p: float, q: float, plane: Plane, point_1: tuple, point_2: tuple, hmin: float, hmax: float, height: float):
        """
        Funkcja ponownie liczy terenowy rozmiar piksela po zmianie wysokości lotu.
        
                Argumenty:
                        height (float): wysokość lotu
                        camera (Camera): obiekt klasy Camera
        
                Zwraca:
                        gsd (float): terenowy rozmiar piksela
        """
        gsd = camera.pixel_size * height / camera.focal_length
        Lx, Ly = calculate_range(gsd, camera)
        bx, by = calculate_base(Ly, Lx, p, q)
        Dx, Dy = calculate_Dx_Dy(point_1, point_2)
        ny, nx = calculate_amount_of_series(Dx, bx, Dy, by)
        bx, by, p, q = recalc_after_ceil(nx, ny, bx, by, Dx, Dy, Lx, Ly)
        n = calculate_number_of_photos(nx, ny)
        dtx = bx / velocity
        bool_interval = check_interval(dtx, camera)

        if bool_interval == False:
            print("Odstęp czasowy między zdjęciami jest mniejszy niż cykl kamery. Zmniejszam prędkość samolotu.")
            velocity = calculate_max_velocity(plane, camera, bx)
            print(f"Prędkość zmniejszona do {velocity} m/s.")

        return gsd, Lx, Ly, bx, by, nx, ny, n, bool_interval

def calculate(gsd: float, camera: Camera, velocity: float, p: float, q: float, plane: Plane, point_1: tuple, point_2: tuple, hmin: float, hmax: float):
    
    '''
    Funkcja oblicza parametry nalotu.

            Argumenty:
                    gsd (float): terenowy rozmiar piksela
                    camera (Camera): obiekt klasy Camera
                    velocity (float): prędkość lotu wybrana przez użytkownika
                    p (float): pokrycie podłużne
                    q (float): pokrycie poprzeczne
                    plane (Plane): obiekt klasy Plane

            Zwraca:
                    height (float): wysokość lotu
                    Lx (float): terenowy zasięg zdjęcia w poprzek kierunku lotu
                    Ly (float): terenowy zasięg zdjęcia wzdłuż kierunku lotu
                    bx (float): terenowy wymiar bazy fotografowania w poprzek kierunku lotu
                    by (float): terenowy wymiar bazy fotografowania wzdłuż kierunku lotu
                    nx (int): liczba zdjęć w pojedynczym szeregu
                    ny (int): liczba szeregów
                    n (int): liczba zdjęć w całym nalocie   
                    bool_interval (bool): True jeśli odstęp jest większy niż cykl, False jeśli nie
                    bool_height (bool): True jeśli wysokość jest możliwa, False jeśli nie

    '''
    height = calculate_height(gsd, camera)
    Lx, Ly = calculate_range(gsd, camera)
    bx, by = calculate_base(Ly, Lx, p, q)
    Dx, Dy = calculate_Dx_Dy(point_1, point_2)
    ny, nx = calculate_amount_of_series(Dx, bx, Dy, by)
    bx, by, p, q = recalc_after_ceil(nx, ny, bx, by, Dx, Dy, Lx, Ly)
    n = calculate_number_of_photos(nx, ny)
    dtx = bx / velocity
    bool_interval = check_interval(dtx, camera)
    bool_height = check_height(height, hmin, hmax, plane)
    
    if bool_interval == False:
        print("Odstęp czasowy między zdjęciami jest mniejszy niż cykl kamery. Zmniejszam prędkość samolotu.")
        velocity = calculate_max_velocity(plane, camera, bx)
        print(f"Prędkość zmniejszona do {velocity} m/s.")

    if bool_height == False:
        print("Wysokość lotu jest zbyt duża dla wybranego samolotu.")
        height = calculate_max_height(plane, hmin, hmax)
        print(f"Zmniejszono wysokość lotu do {height} m n. p. m.")
        gsd, Lx, Ly, bx, by, nx, ny, n, bool_interval = recalc_after_height_change(camera, velocity, p, q, plane, point_1, point_2, hmin, hmax, height)
        print("Przeliczono ponownie parametry nalotu.")

    # skala = calculate_scale(height, camera)
    # Bx = bx * skala
    # By = by * skala

        return height, Lx, Ly, bx, by, nx, ny, n, bool_interval, bool_height
    