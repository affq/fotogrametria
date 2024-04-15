def kmhtoms(kmh):
    return kmh * (1000 / 3600)

class Camera:
    def __init__(self, name, pixel_size, focal_length, frame_long, frame_short):
        self.name = name
        self.pixel_size = pixel_size * 1e-6
        self.focal_length = focal_length * 1e-3
        self.frame_long = frame_long
        self.frame_short = frame_short
    

class Plane:
    def __init__(self, name, velocity_min, velocity_max, ceiling, flight_time):
        self.name = name
        self.velocity_min = kmhtoms(velocity_min)
        self.velocity_max = kmhtoms(velocity_max)
        self.ceiling = ceiling
        self.flight_time = flight_time
