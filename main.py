import tkinter as tk
import cv2 as cv
from camsandplanes import Camera, Plane
import math

def calculate(gsd, camera, velocity, p, q):
    height = camera.focal_length * gsd / camera.pixel_size
    Lx = camera.frame_short * gsd
    Ly = camera.frame_long * gsd
    bx = Lx * ((100-p)/100)
    by = Ly * ((100-q)/100)
    skala = camera.focal_length / height
    Bx = bx * skala
    By = by * skala
    tbx = Bx / velocity

def calculate_height(gsd, camera):
    '''
    gsd: terenowy wymiar piksela, wartość podana przez użytkownika
    camera: obiekt klasy Camera
    '''
    height = camera.focal_length * gsd / camera.pixel_size
    return height

def check_height(height, hmin, hmax, plane):
    '''
    height: projektowana wysokość lotu
    hmin: minimalna wysokość terenu na obszarze opracowania
    hmax: maksymalna wysokość terenu na obszarze opracowania
    plane: obiekt klasy Plane
    '''
    average_height = (hmin + hmax)/2
    absolutna_height = height + average_height
    if absolutna_height > plane.ceiling: 
        return False
    else:
        return True

def calculate_range(gsd, camera):
    '''
    oblicza terenowy zasięg zdjęcia
    gsd: terenowy wymiar piksela, wartość podana przez użytkownika
    camera: obiekt klasy Camera, wybrana przez użytkownika
    '''
    Lx = camera.frame_short * gsd
    Ly = camera.frame_long * gsd
    return Lx, Ly

def calculate_base(Ly, Lx, p, q):
    '''
    obliczna wymiar terenowy bazy podłużnej i poprzecznej
    Lx, Ly: terenowe wymiary zdjęcia
    p: pokrycie podłużne
    q: pokrycie poprzeczne
    '''
    bx = Lx * ((100-p)/100)
    by = Ly * ((100-q)/100)
    return bx, by

def calculate_amount_of_series(Dx, bx, Dy, by):
    '''
    oblicza liczbę szeregów i liczbę zdjęć w pojedynczym szeregu
    Dx
    '''
    ny = math.ceil(by/Dy)
    nx = math.ceil(bx/Dx + 4)
    return nx, ny


root = tk.Tk()
root.title("projekt nalotu")

root.mainloop()