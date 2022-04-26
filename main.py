import création_perso as crea 
from email.policy import default
import os
import Armure as arm
import weapons as wea
import ND_arrays as nd
import Rpg_map as mp
import capacitys as cap
import monster as mob

test_bull = mob.bull(10, 2, 3, None, None, 3)
heathcliff = crea.character("Heathcliff", 100, 5, 0, [], [crea.churros])

basic_armor = arm.armor("Basic Armor", "common", )

print(heathcliff.PV)
test_bull.charge(heathcliff)
print(heathcliff.PV)
heathcliff.attack(test_bull, None)

os.system("pause")