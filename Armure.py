class armor:
    def __init__(self, name, rarety, PDEF, zone):
        self.name = name 
        self.rarety = rarety
        self.PDEF = PDEF 
        self.zone = zone 
        
    def __repr__(self):
        return f"name : {self.name}"