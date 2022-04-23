import ND_arrays as nd
# Pour la map je vais faire un truc du style(les numéros serais l'ordre des zones):
#[5][3][4]
#[6][0][1]
#[7][8][2] après ça peux changer"""

# 2 idées la c'esttt on peut ranger toutes les maps dans une grande carte
# ou séparément, ca change pas grand chose

Map = nd.Nd_array((3, 3), dtype=nd.Nd_array)
def instore_map():
    for i in range(3):
        for j in range(3):
            Map[i, j] = nd.Nd_array((100, 100))
            Map[i, j].instore((255, 0, 0))

insore_map()
