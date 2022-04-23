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
            Map[i, j].zeros()

# j'avais deux idées pour remplir la map, soit 0 c'est l'herbe
# pour la mémoir
# Ou alors on met un tuple contenant la couleur de la case (ex pourr l'herbe:
# (0, 255, 0)) 

instore_map()           

Map[1, 1].insert(1, ((34, 64), (34, 64))) # c'est la zone 0
# ce que j'ai fait la c'est que les 30 block autour du spawn sont de la brique pour une ville par exemple
# la brique serai 1

#on rajoutera des items etc 
# et il faudrais peut etre faire un truc de drop aléatoire de combat quand le personnage se déplace
