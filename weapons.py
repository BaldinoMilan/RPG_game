class melee_weapon:
    def __init__(self, name, rarety, damage, speed, zone, range = 1):
        self.name = name 
        self.rarety = rarety 
        self.damage = damage 
        self.speed = speed 
        self.zone = zone 
        
class ranged_weapon:
    def __init__(self, name, rarety, damage, zone, range = 2):
        self.name = name
        self.rarety = rarety 
        self.damage = damage 
        self.zone = zone 
        self.range = range 
