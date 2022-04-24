import os

class monster:
    def __init__(self, PV, PAT, zone, name, type, lvl = 1):
        self.PV = PV 
        self.PAT = PAT 
        self.zone = zone
        self.lvl = lvl 
        self.name = name 
        self.type = type 

    def attack(self, target):
        target.PDEF -= self.PAT 
        if target < 0:
            target.PV += target.PDEF
            target.PDEF = 0
        
        else:
            pass 

class goblin(monster):
    def poison(self, target):
        target.effect = "poison"
        
        
class bull(monster):
    def charge(self, target):
        damage = self.PAT * 2
        target.PDEF -= damage  
        if target.PDEF < 0:
            target.PV += target.PDEF
            target.PDEF = 0 
            
        else:
            pass
          
os.system("pause")
