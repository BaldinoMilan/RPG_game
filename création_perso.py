############################################################
####### CE SCRIPT EST EN R&D DONC AU FUR ET A MESURE #######
#######QU'ON AJOUTERA DES FONCTIONALITES ELLES SERONT#######
#######          IMPLEMENTES DANS CE SCRIPT          #######
############################################################

from email.policy import default
import Armure as arm
import weapons as wea
import ND_arrays as nd
import Rpg_map as mp
import capacitys as cap
import monster as mob

capacitys = {}

advantages = ["PV", "PDEF"]
            

#PV = Points de vie DE BASE
#PAT = Points d'attaque DE BASE
#PDEF = Points de défense
#armor = dictionnaire permettant d'équiper et de visualiser l'armure

#système d'attaque incomplet car les monstres et autres types d'ennemis ne sont implémentés et que les différentes features des armes
#notemment sur les différentes attaques dispos etc... ne sont pas encore implémentés

class character:
    def __init__(self, name, PV, PAT, PDEF = 0, effect = [], inv = [], armor = {"helmet" : None, "chestplate" : None, "leggings" : None, "boots" : None}):
        self.name = name
        self.PV = PV 
        self.PVB = PV 
        self.PAT = PAT 
        self.PATB = PAT 
        self.PDEF = PDEF 
        self.armor = armor 
        self.pos = (49, 49) 
        self.inv = inv 
        self.effect = effect
        
        if self.name == "Carlos de Miguel":
            gamerule_churros = True 
            inv.append("Churros")

    def equip_helmet(self, helmet_1):
        self.armor["helmet"] = arm.helmet(helmet_1) 
    
    def equip_chestplate(self, chestplate_1):
        self.armor["chestplate"] = arm.chestplate(chestplate_1)
    
    def equip_leggings(self, leggings_1):
        self.armor["leggings"] = arm.leggings(leggings_1)
    
    def equip_boots(self, boots_1):
        self.armor["boots"] = arm.boots(boots_1)
        
    def attack(self, target, technic):
            if target.PDEF > 0:
                 target.PDEF -= self.PAT   #à therme on fera target.PDEF -= self.PAT + dégats de l'attaque 
                 if target.PDEF < 0:
                    target.PV += target.PDEF
                    target.PDEF = 0
                    if target.PV <= 0:
                        return f"{target.name} est mort"
                    
            elif target.PDEF == 0:
                target.PV -= self.PAT 
                if target.PV <= 0:
                    return f"{target.name} est mort"
    def move(self, x, y):
        self.pos = (self.pos[0] + x, self.pos[1] + y)
        
    def eat(self, food_to_eat):
        if food_to_eat in food_available:
            food(food_to_eat)
            if food_to_eat.adv == "PV":
                self.PV += food_to_eat.ammount
            
            elif food_to_eat.adv == "PDEF":
                self.PV += food_to_eat.ammount

        else:
            return f"{food_to_eat} n'est pas dans le jeu"
        
        # on appeleras cette fonction avec les touches du claviers, je pense savoir comment faire 
        # peut être mettre un système de mob aléatoire à chaque mouvement ? /// en vrai de ouf
        
# est-ce qu'on fait un système dd'inventaire aussi ?

class food:
    def __init__(self, adv, ammount):
        self.adv = adv
        self.ammount = ammount 

            
churros = food("PV", 200)
food_available = [churros] 