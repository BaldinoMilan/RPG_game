import Characters as crt 
import weapons as wp
import equipment as plt
import ND_arrays as nd
""" MAP: 9 maps = 9 zones
[map_1] [map_2] [map_3]
[map_4] [main_map] [map_5]
[map_6] [map_7] [map_8] """

block = {0: "grass", 1: "water"}

main_map = nd.Nd_array((30, 30), dtype=int)
main_map.zeros()

map_1 = nd.Nd_array((30, 30), dtype=int)
map_1.zeros()