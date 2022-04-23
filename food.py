import os
import capacitys as cap 
import création_perso as crea

advantages = ["PV", "PDEF"]

class food:
    def __init__(self, adv, ammount):
        self.adv = adv
        self.ammount = ammount 
        if self.adv == "PV":
            crea.character.PV += ammount 
        
        elif self.adv == "PDEF":
            crea.character.PDEF += ammount 

            
churros = food("PV", 200)
        

os.system("pause")