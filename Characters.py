import weapons as wp
import equipment as plt
from random import randint
def calc_stats(self):
    self.actual_stats["Level"] = self.level
    self.actual_stats["Attack"] = self.damage
    self.actual_stats["Armor"] = self.defense
    self.actual_stats["Health"] = self.health

""" ALL CHARACTERS WILL BE LIKE """
class CharacterLike:
    def __init__(self, name_, class_, damage_base, defense_base, health_base, base_weapon, level = 1):
        """ Base Statistics """
        self.name = name_
        self.class_ = class_
        self.base_damage = damage_base
        self.damage_scaling = self.base_damage * 0.05
        self.base_defense = defense_base
        self.defense_scaling = self.base_defense * 0.05
        self.base_health = health_base
        self.health_scaling = self.base_health * 0.05
        self.level = level
        self.weapon = base_weapon
        self.lvl_exp = self.level * 200 + 400
        self.exp = 0
        self.damage = self.damage_scaling * self.level + self.base_damage
        self.defense = self.defense_scaling * self.level + self.base_defense
        self.health = self.health_scaling * self.level + self.base_health
        self.actual_stats = {}
        calc_stats(self)

        """ Equipement """
        
        self.actual_health = self.health

        self.base_stats = [self.name, self.base_damage, self.base_defense, 
                            self.base_health, self.level, self.class_, self.weapon]
        
        """ Items
        blob: explosiv effect, prairie zone              serpent venin orb: poison effect, jungle zone
        wolf tooth: blood effect, snow montain zone      giant fishbone: drowing effect, aquatic zone
        ancient silex: crit_damages, desert              void ring: decay effect, = abbysal zone
        """
        self.inventary = {"blob": 0, "wolf tooth": 0, "ancient silex": 0, "serpent venin orb": 0, 
                          "giant fishbone": 0, "void ring": 0, "pheonix feather": 3, "weapons":[], "equipment": []}
    
    def hit(self, target):
        self.actualisate()
        self.weapon.actualisate()
        target.actualisate()
        target.plastron.actualisate()
        if randint(1, 100) > self.weapon.crit_chance:
            damage_given = self.damage * self.weapon.attack
            crit = False
        else:
            crit = True            
            damage_given = self.damage * self.weapon.attack  * self.weapon.crit_damage
        dealing_damage = damage_given - target.defense + self.weapon.lethality 
        if dealing_damage > target.health/5:
            dealing_damage -= target.health / 5
        else:
            pass
        target.actual_health -= dealing_damage
        if crit == True:
            return f"CRIT ! {target.name} has token {dealing_damage} damages!"
        else:    
            return f"{target.name} has token {dealing_damage} damages!"

    def actualisate(self):
        self.lvl_exp = self.level * 200 + 400
        self.damage = self.damage_scaling * self.level + self.base_damage 
        self.defense = self.defense_scaling * self.level + self.base_defense + self.plastron.defense 
        self.health = self.health_scaling * self.level + self.base_health + self.plastron.health

""" Classes of Character"""
class Paladin(CharacterLike): 
    def __init__(self, name_, level=1):
        super().__init__(name_, "paladin", 4, 10, 300, wp.Basic_sword(1), level)
        self.plastron = plt.Renforced_Plastron(1)
        
class Fighter(CharacterLike): 
    def __init__(self, name_, level=1):
        super().__init__(name_, "fighter", 7, 7, 300, wp.Basic_sword(1), level)
        self.plastron = plt.Cloth_Armor(1)

class Assasin(CharacterLike):
    def __init__(self, name_, level=1):
        super().__init__(name_, "assasin", 10, 3, 250, wp.Serrated_Daguer(1), level)
        self.plastron = plt.Assasin_cape(1)
    
class Archerer(CharacterLike):
    def __init__(self, name_, level=1):
        super().__init__(name_, "assasin", 10, 3.5, 250, wp.Saplin_Bow(1), level)
        self.plastron = plt.Basic_Cloth(1)

def wpon_level(level):
    if level <= 20:
        return 1
    elif level <= 40 and level > 10:
        return 2
    elif level <= 60 and level > 40:
        return 3
    elif level <= 80 and level > 60:
        return 4
    elif level > 80:
        return 5
    else:
        raise TypeError("Enemy level can't be a negativ number.")

class Slime(CharacterLike):
    def __init__(self, name_, level=1):
        items = wpon_level(level)
        super().__init__(name_, "enemy_slime", 4, 10, 300, wp.Basic_sword(items), level)
        self.plastron = plt.slime_skin(items)

class Wolf(CharacterLike):
    def __init__(self, name_, level=1):
        items = wpon_level(level)
        super().__init__(name_, "enemy_wolf", 10, 3, 250, wp.Serrated_Daguer(items), level)
        self.plastron = plt.wolf_skin(items)

class Cirstal_Rock(CharacterLike):
    def __init__(self, name_, level=1):
        items = wpon_level(level)
        super().__init__(name_, "enemy_cristal_rock", 4, 10, 300, wp.Basic_sword(items), level)
        self.plastron = plt.cristal_rock_skin(items)

class Anaconda_Serpent(CharacterLike):
    def __init__(self, name_, level=1):
        items = wpon_level(level)
        super().__init__(name_, "enemy_anaconda_serpent", 10, 3.5, 250, wp.Saplin_Bow(items), level)
        self.plastron = plt.anaconda_serpent_skin(items)

class Dreadful_fish(CharacterLike):
    def __init__(self, name_, level=1):
        items = wpon_level(level)
        super().__init__(name_, "enemy_dreadful_fish", 7, 7, 300, wp.Basic_sword(items), level)
        self.plastron = plt.dreadful_fish_skin(items)

class Abyssal_decay(CharacterLike):
    def __init__(self, name_, level=1):
        items = wpon_level(level)
        super().__init__(name_, "paladin", 4, 10, 300,wp. Serrated_Daguer(items), level)
        self.plastron = plt.abyssal_decay_skin(items)