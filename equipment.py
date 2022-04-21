""" Classes of Plastron """
class PlastronLike:
    def __init__(self, rarety, base_defense, base_health, base_dodge, lvl=1) -> None:
        """ Base Statistics """
        self.rarety = rarety
        self.level = lvl
        self.base_defense = base_defense * self.rarety
        self.defense = self.base_defense * self.level * 0.2 + self.base_defense
        self.dodge_chance = base_dodge * rarety
        self.base_health = base_health * rarety
        self.health = self.base_health * 0.2 * self.level + self.base_health
    
    def actualisate(self):
        self.defense = self.base_defense * self.level * 0.2 + self.base_defense
        self.health = self.base_health * 0.2 * self.level + self.base_health

class Renforced_Plastron(PlastronLike):  
    def __init__(self, rarety, lvl=1) -> None:
        super().__init__(rarety, 11, 80, 1, lvl)

class Cloth_Armor(PlastronLike): 
    def __init__(self, rarety, lvl=1) -> None:
        super().__init__(rarety, 4, 90, 5, lvl)

class Assasin_cape(PlastronLike): # Assasin for
    def __init__(self, rarety, lvl=1) -> None:
        super().__init__(rarety, 3, 45, 25, lvl)

class Basic_Cloth(PlastronLike): # Archerer for
    def __init__(self, rarety, lvl=1) -> None:
        super().__init__(rarety, 5, 65, 1, lvl)
