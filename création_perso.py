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

food_available = []

#PV = Points de vie DE BASE
#PAT = Points d'attaque DE BASE
#PDEF = Points de défense
#armor = dictionnaire permettant d'équiper et de visualiser l'armure

#système d'attaque incomplet car les monstres et autres types d'ennemis ne sont implémentés et que les différentes features des armes
#notemment sur les différentes attaques dispos etc... ne sont pas encore implémentés

class food:
    def __init__(self, adv, ammount):
        self.adv = adv
        self.ammount = ammount 

class character:
    def __init__(self, name, PV, PAT, PDEF = 0, effect = [], inv = [], armor = None, attacked = False, in_fight = False):
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
        self.attacked = attacked
        self.in_fight = in_fight
        self.attacker = None
        
        if self.name == "Carlos de Miguel":
            gamerule_churros = True 
            inv.append("Churros")

    def equip_armor(self, armor_1):
        self.armor = armor_1 
        self.PDEF += armor_1.PDEF
        
    def attack(self, target, technic):
        target.PDEF -= self.PAT 
        if target.PDEF < 0:
            target.PV += target.PDEF
            target.PDEF = 0
        
        else:
            pass 
                    
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

class paladin(character):
    def parade(self, attacker):
        if self.in_fight and self.attacked:
            attacker = self.attacker 
            attacker.PAT += self.PV
            if self.PV > self.PVB:
                self.PV -= self.PVB 
                self.PDEF = self.PV 
                self.PV = self.PVB
    
    def critical(self, target):
        target.PDEF -= self.PAT * 1.75
        if target.PDEF < 0:
            target.PV -= target.PDEF