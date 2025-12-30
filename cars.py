import pygame
from config import CAR_COLORS, CARS_SIZE

# Dictionnaire pour les voitures de différentes couleurs et directions
cars_dict = {
    "left": [ ],
    "right": [ ]
} 



# ======================== PARTIE 2.1 ========================
# TODO : 
# 1. Parcourir la liste des couleurs (CAR_COLORS) à l'aide d'une boucle
# 2. Pour chaque couleur :
#    - Chargez l'image vers la droite ("_right") et celle vers la gauche ("_left") à l'aide de pygame.image.load().
#    - Redimensionnez chaque image à CARS_SIZE à l’aide de la fonction pygame.transform.scale().
#    - Ajoutez les images redimensionnées dans la bonne liste ("left" ou "right") du dictionnaire cars_dict.

# Écrire votre code ici : 
#Charger l'image: 
for c in CAR_COLORS: 
    image_right= pygame.image.load(f'images/car_{c}_right.png')
    image_left= pygame.image.load(f'images/car_{c}_left.png')

#redimensionnez image
    image_right=pygame.transform.scale(image_right , CARS_SIZE)
    image_left=pygame.transform.scale(image_left, CARS_SIZE)
# ajouter dans la bonne list: 
    cars_dict['right'].append(image_right)
    cars_dict['left'].append(image_left)

# ===============================================================
