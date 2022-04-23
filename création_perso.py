############################################################
####### CE SCRIPT EST EN R&D DONC AU FUR ET A MESURE #######
#######QU'ON AJOUTERA DES FONCTIONALITES ELLES SERONT#######
#######          IMPLEMENTES DANS CE SCRIPT          #######
############################################################

import os
import Armure as arm
import weapons as wea

#PV = Points de vie DE BASE
#PAT = Points d'attaque DE BASE
#PDEF = Points de défense
#armor = dictionnaire permettant d'équiper et de visualiser l'armure

#système d'attaque incomplet car les monstres et autres types d'ennemis ne sont implémentés et que les différentes features des armes
#notemment sur les différentes attaques dispos etc... ne sont pas encore implémentés

class character:
    def __init__(self, PV, PAT, PDEF = 0, armor = {"helmet" : None, "chestplate" : None, "leggings" : None, "boots" : None}):
        self.PV = PV 
        self.PVB = PV 
        self.PAT = PAT 
        self.PATB = PAT 
        self.PDEF = PDEF 
        self.armor = armor 
        if self.name == "Carlos de Miguel":
            gamerule_churros = True 

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
# tu devrais faire un: def move(): pour ffaire bouger le personnage
# et un self.pos pour la position actuelle du personnage sur la map(ps j'ai créé une map fait moi des retours)

os.system("pause")
