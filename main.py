import tkinter as tk
import cv2 as cv

root = tk.Tk()
root.title("projekt nalotu")

cameras = [
    {'nazwa': 'Z/I DMC IIe 140', 'dp': 0.0000072, 'f': 0.092, 'lx': 11200, 'ly': 12096},
    {'nazwa': 'Z/I DMC IIe 230', 'dp': 0.0000056, 'f': 0.092, 'lx': 15552, 'ly': 14144},
    {'nazwa': 'UltraCam Falcon', 'dp': 0.0000072, 'f': 0.07, 'lx': 14430, 'ly': 9420},
    {'nazwa': 'UltraCam Hawk', 'dp': 0.000006, 'f': 0.07, 'lx': 11704, 'ly': 7920}
]

planes = [
    {'nazwa': 'Cessna 402', 'vmin': 132, 'vmax': 428, 'pułap': 8200, 'flighttime': 5}
    # km/h ^
]

root.mainloop()