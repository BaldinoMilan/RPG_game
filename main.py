from operator import inv
import création_perso as crea 
from email.policy import default
import os
import Armure as arm
import weapons as wea
import ND_arrays as nd
import Rpg_map as mp
import capacitys as cap
import monster as mob

churros = crea.food("PV", 200)

test_bull = mob.bull(10, 2, 3, None, None, 3)
heathcliff = crea.character("Heathcliff", 100, 5, 0, [], [churros])

basic_armor = arm.armor("Basic Armor", "common", 10, 1)
hunter_armor = arm.armor("Hunter Armor", "rare", 15, 1)

print(heathcliff.PV)
test_bull.charge(heathcliff)
print(heathcliff.PV)
heathcliff.attack(test_bull, None)
print(heathcliff.inv[0])
heathcliff.eat(heathcliff.inv[0])
print(heathcliff.PV)
print(heathcliff.PDEF)
heathcliff.equip_armor(hunter_armor)
print(heathcliff.PDEF)

os.system("pause")