import ND_arrays as nd
import random

block_color = {0 : (0, 255, 0)} # il n'y a que la couleur de l'herbe, je croit que c'est vert mais modifie la si c pas ça
# c'est un dictionnaire référence de toute les couleur pour la map(si il y a des items non défini il faut les mettres la dedans)
Png_object = {}
Map = {}
for i in range(1, 9):
  Map[f"zone{i}"] = nd.Nd_array((100, 100))
  Map[f"zone{i}"][random.randint(0, 100), random.randint(0, 100)] = Png_object # <-- faut creer un objeet png ou jsp 

# modifier la map avec Map[coordonées] = truc que tu veux rajouter
