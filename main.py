from fun import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk


class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Projektant nalotu fotogrametrycznego")
        self.root.geometry("800x600")

        self.options_frame = tk.LabelFrame(self.root, text="Opcje")
        self.options_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        
        self.top_left_frame = tk.LabelFrame(self.options_frame, text="Lewy górny róg")
        self.top_left_frame.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)
        self.top_left_x = ttk.Label(self.top_left_frame, text="X:")
        self.top_left_x.pack(side=tk.LEFT, pady=10)
        self.top_left_x_entry = ttk.Entry(self.top_left_frame, width=10)
        self.top_left_x_entry.pack(side=tk.LEFT, padx=10)
        self.top_left_x_entry.insert(0, "0")


        self.top_left_y = ttk.Label(self.top_left_frame, text="Y:")
        self.top_left_y.pack(side=tk.LEFT, pady=10)
        self.top_left_y_entry = ttk.Entry(self.top_left_frame, width=10)
        self.top_left_y_entry.pack(side=tk.LEFT, padx=10)
        self.top_left_y_entry.insert(0, "0")

        self.bottom_right_frame = tk.LabelFrame(self.options_frame, text="Prawy dolny róg")
        self.bottom_right_frame.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)
        self.bottom_right_x = ttk.Label(self.bottom_right_frame, text="X:")
        self.bottom_right_x.pack(side=tk.LEFT, pady=10)
        self.bottom_right_x_entry = ttk.Entry(self.bottom_right_frame, width=10)
        self.bottom_right_x_entry.insert(0, "19090")
        self.bottom_right_x_entry.pack(side=tk.LEFT, padx=10)


        self.bottom_right_y = ttk.Label(self.bottom_right_frame, text="Y:")
        self.bottom_right_y.pack(side=tk.LEFT, pady=10)
        self.bottom_right_y_entry = ttk.Entry(self.bottom_right_frame, width=10)
        self.bottom_right_y_entry.insert(0, "17219")
        self.bottom_right_y_entry.pack(side=tk.LEFT, padx=10)

        self.heights_frame = tk.LabelFrame(self.options_frame, text="Wysokości terenu")
        self.heights_frame.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)

        self.min_height = ttk.Label(self.heights_frame, text="Min:")
        self.min_height.pack(side=tk.LEFT, pady=10)
        self.min_height_entry = ttk.Entry(self.heights_frame, width=10)
        self.min_height_entry.insert(0, "140")
        self.min_height_entry.pack(side=tk.LEFT, padx=10)

        self.max_height = ttk.Label(self.heights_frame, text="Max:")
        self.max_height.pack(side=tk.LEFT, pady=10)
        self.max_height_entry = ttk.Entry(self.heights_frame, width=10)
        self.max_height_entry.insert(0, "160")
        self.max_height_entry.pack(side=tk.LEFT, padx=10)

        self.camera_frame = tk.Frame(self.options_frame)
        self.camera_frame.pack(side=tk.TOP, padx=10, anchor=tk.NW)
        self.camera_label = ttk.Label(self.camera_frame, text="Kamera:").pack(side=tk.LEFT, pady=10)
        self.camera_combobox = ttk.Combobox(self.camera_frame, values=["Z/I DMC IIe 230", "Leica DMC III", "UltraCam Falcon M2 70", "UltraCam Eagle M2 80"])
        self.camera_combobox.set("Z/I DMC IIe 230")
        self.camera_combobox.pack(side=tk.LEFT, padx=10)

        self.plane_frame = tk.Frame(self.options_frame)
        self.plane_frame.pack(side=tk.TOP, padx=10, anchor=tk.NW)
        self.plane_label = ttk.Label(self.plane_frame, text="Samolot:")
        self.plane_label.pack(side=tk.LEFT, pady=10)
        self.plane_combobox = ttk.Combobox(self.plane_frame, values=["Cessna 402", "Cessna T206H NAV III", "Vulcan Air P68 Obeserver 2", "Tencam MMA"])
        self.plane_combobox.set("Cessna 402")
        self.plane_combobox.pack(side=tk.LEFT, padx=10)
        
        self.velocity_frame = tk.Frame(self.options_frame)
        self.velocity_frame.pack(side=tk.TOP, padx=10, anchor=tk.NW)
        self.velocity_label = ttk.Label(self.velocity_frame, text="Prędkość:")
        self.velocity_label.pack(side=tk.LEFT, pady=10)
        self.velocity_entry = tk.Scale(self.velocity_frame, from_=1, to=428, resolution=1, orient=tk.HORIZONTAL)
        self.velocity_entry.set(132)
        self.velocity_entry.pack(side=tk.LEFT, padx=10)


        self.gsd_frame = tk.Frame(self.options_frame)
        self.gsd_frame.pack(side=tk.TOP, padx=10, anchor=tk.NW)
        self.gsd_label = ttk.Label(self.gsd_frame, text="GSD:")
        self.gsd_label.pack(side=tk.LEFT, pady=10)
        self.gsd_scale = tk.Scale(self.gsd_frame, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
        self.gsd_scale.set(25)
        self.gsd_scale.pack(side=tk.LEFT, padx=10)

        self.p_frame = tk.Frame(self.options_frame)
        self.p_frame.pack(side=tk.TOP, padx=10, anchor=tk.NW)
        self.p_label = ttk.Label(self.p_frame, text="Pokrycie poprzeczne:")
        self.p_label.pack(side=tk.LEFT, pady=10)
        self.p_scale = tk.Scale(self.p_frame, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL)
        self.p_scale.set(30)
        self.p_scale.pack(side=tk.LEFT, padx=10)

        self.q_frame = tk.Frame(self.options_frame)
        self.q_frame.pack(side=tk.TOP, padx=10, anchor=tk.NW)
        self.q_label = ttk.Label(self.q_frame, text="Pokrycie podłużne:")
        self.q_label.pack(side=tk.LEFT, pady=10)
        self.q_scale = tk.Scale(self.q_frame, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL)
        self.q_scale.set(60)
        self.q_scale.pack(side=tk.LEFT, padx=10)
        
        self.calculate_button = tk.Button(self.options_frame, text="Oblicz", width=15)
        self.calculate_button.pack(side=tk.TOP, pady=10)
        self.calculate_button.bind("<Button-1>", self.print_to_text_box)

        self.text_box = tk.Text(self.root, height=30, width=60)
        self.text_box.pack(side=tk.RIGHT, padx=10, pady=20, anchor=tk.NE)
        self.text_box.insert(tk.END, f"Wyniki obliczeń: \n")
        self.text_box.config(state=tk.DISABLED)

    def print_to_text_box(self, event):
        self.text_box.config(state=tk.NORMAL)
        self.text_box.insert(tk.END, f" Punkt top-left: ({self.top_left_x_entry.get()}, {self.top_left_y_entry.get()}),\n")
        self.text_box.insert(tk.END, f" Punkt bottom-right: ({self.bottom_right_x_entry.get()}, {self.bottom_right_y_entry.get()}),\n")
        self.text_box.insert(tk.END, f" Wysokości terenu: {self.min_height_entry.get()} - {self.max_height_entry.get()},\n")
        self.text_box.insert(tk.END, f" Kamera: {self.camera_combobox.get()},\n")
        self.text_box.insert(tk.END, f" Samolot: {self.plane_combobox.get()},\n")
        self.text_box.insert(tk.END, f" Prędkość: {self.velocity_entry.get()},\n")
        self.text_box.insert(tk.END, f" GSD: {self.gsd_scale.get()},\n")
        self.text_box.insert(tk.END, f" Pokrycie poprzeczne: {self.p_scale.get()},\n")
        self.text_box.insert(tk.END, f" Pokrycie podłużne: {self.q_scale.get()}\n")
        self.text_box.insert(tk.END, f"------------------------------------\n")
        self.text_box.insert(tk.END, f" Wynik: {calculate(self.gsd_scale.get(), Camera(self.camera_combobox.get()), float(self.velocity_entry.get()), float(self.p_scale.get()), float(self.q_scale.get()), Plane(self.plane_combobox.get()), (float(self.top_left_y_entry.get()), float(self.top_left_x_entry.get())), (float(self.bottom_right_y_entry.get()), float(self.bottom_right_x_entry.get())), float(self.min_height_entry.get()), float(self.max_height_entry.get()))}\n")
        self.text_box.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()