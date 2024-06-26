def kmhtoms(kmh):
    return kmh * (1000 / 3600)

def mstokmh(ms):
    return ms * (3600 / 1000)

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
    
    def get_pixel_size(self):
        return self.pixel_size
    
    def get_focal_length(self):
        return self.focal_length
    
    def get_frame_long(self):
        return self.frame_long
    
    def get_frame_short(self):
        return self.frame_short
    
    def get_cycle(self):
        return self.cycle
    
    def get_name(self):
        return self.name

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
        self.velocity_avg = (self.get_velocity_min() + self.get_velocity_max()) / 2

    def get_velocity_min(self):
        return self.velocity_min

    def get_velocity_max(self):
        return self.velocity_max
    
    def get_velocity_avg(self):
        return self.velocity_avg
    
    def get_ceiling(self):
        return self.ceiling
    
    def get_flight_time(self):
        return self.flight_time
    
    def get_name(self):
        return self.name
    