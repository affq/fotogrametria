def kmhtoms(kmh):
    return kmh * (1000 / 3600)

class Camera:
    def __init__(self, name):
        if name == "Z/I DMC IIe 230":
            self.name = name
            self.pixel_size = 5.6e-6
            self.focal_length = 92e-3
            self.frame_long = 15552
            self.frame_short = 14144
            self.cycle = 1.8
        elif name == "Leica DMC III":
            self.name = name
            self.pixel_size = 3.9e-6
            self.focal_length = 92e-3
            self.frame_long = 25728
            self.frame_short = 14592
            self.cycle = 1.9
        elif name == "UltraCam Falcon M2 70":
            self.name = name
            self.pixel_size = 6e-6
            self.focal_length = 70e-3
            self.frame_long = 17310
            self.frame_short = 11310
            self.cycle = 1.35
        elif name == "UltraCam Eagle M2 80":
            self.name = name
            self.pixel_size = 4.6e-6
            self.focal_length = 80e-3
            self.frame_long = 23010
            self.frame_short = 14790
            self.cycle = 1.65

class Plane:
    def __init__(self, name):
        self.name = name
        if name == "Cessna 402":
            self.velocity_min = kmhtoms(132)
            self.velocity_max = kmhtoms(428)
            self.ceiling = 8200
            self.flight_time = 5
        elif name == "Cessna T206H NAV III":
            self.velocity_min = kmhtoms(100)
            self.velocity_max = kmhtoms(280)
            self.ceiling = 4785
            self.flight_time = 5
        elif name == "Vulcan Air P68 Obeserver 2":
            self.velocity_min = kmhtoms(135)
            self.velocity_max = kmhtoms(275)
            self.ceiling = 6100
            self.flight_time = 6
        elif name == "Tencam MMA":
            self.velocity_min = kmhtoms(120)
            self.velocity_max = kmhtoms(267)
            self.ceiling = 4572
            self.flight_time = 6
        self.velocity_avg = (self.velocity_min + self.velocity_max) / 2