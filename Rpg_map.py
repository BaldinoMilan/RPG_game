import ND_arrays as nd
block_color = {0 : (0, 255, 0)} # il n'y a que la couleur de l'herbe, je croit que c'est vert mais modifie la si c pas ça
# c'est un dictionnaire référence de toute les couleur pour la map(si il y a des items non défini il faut les mettres la dedans)
Map = nd((901, 901))
Map.zeros()
middle = (450, 450)
# modifier la map avec Map[coordonées] = truc que tu veux rajouter
