import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.colors import LinearSegmentedColormap
from pydantic import BaseModel 
import json 
import sys 

# a changer
IMAGE_PARAMS_PATH = 'params_image.json'
GOUTE_PARAMS_PATH = 'params_goutte.json'

with open(IMAGE_PARAMS_PATH) as f : 

    data = json.load(f)

    MIN_HEIGHT = data.get( "MIN_HEIGHT", None ) ; IMAGE_RESOLUTION = data.get( "IMAGE_RESOLUTION", None )
    MAX_HEIGHT = data.get( "MAX_HEIGHT", None ) ; COLOR = data.get( "COLOR_MAP", None )

     # améliorer l'erreur 

    # if MIN_HEIGHT != 0 or not IMAGE_RESOLUTION or not MAX_HEIGHT or not COLOR : 
    #     raise FileNotFoundError(f'ERROR IN  THE CONFIGURATION FILE {IMAGE_PARAMS_PATH}')
    
    if type(COLOR) is not dict : raise ValueError("error in the color")
    
    COLOR  = [ (item, key ) for key, item in COLOR.items()]

    
with open(GOUTE_PARAMS_PATH) as d:
    data=json.load(d)
    RAYON = data.get("RAYON",None) ; HAUTEUR = data.get("HAUTEUR",None)

    if not RAYON or not HAUTEUR : 
       raise FileNotFoundError(f"ERROR IN 'THE CONFIGURATION FILE {GOUTE_PARAMS_PATH}")

def algo_une_goutte(matrice: np.ndarray, point_impact : tuple[int, int]):
    i0, j0 = point_impact[0], point_impact[1]
    n, m = matrice.shape
    X, Y = np.ogrid[:n, :m]
    r = np.sqrt((Y - i0)**2 + (X - j0)**2)
    mask = r < RAYON
    matrice[mask] += HAUTEUR * (1 - (r[mask] / RAYON)**2)
    return matrice

def creer_chemin() -> list[tuple[int, int]]:

    D_OUTIL = 20 ; COEFF_CORRECTEUR = 8 # transformer les pixels en mm   en pixel / mmm
    D_OUTIL_PIXEL = D_OUTIL * COEFF_CORRECTEUR ; DISTANCE_ENTRE_DEUX_BILLES = 30

    list_coordonnée_point_trajet = []

    for i in range(0, 1 +  IMAGE_RESOLUTION // DISTANCE_ENTRE_DEUX_BILLES) :
        for j in range(0, 1 + IMAGE_RESOLUTION // D_OUTIL_PIXEL) : 
            list_coordonnée_point_trajet.append( (i*DISTANCE_ENTRE_DEUX_BILLES , j*D_OUTIL_PIXEL) )

    return list_coordonnée_point_trajet



mat_initiale = np.random.randint(0, 201, (IMAGE_RESOLUTION, IMAGE_RESOLUTION)).astype(np.float32)
liste_points_impact = creer_chemin()

chemin = []

# --- MATPLOTLIB VISUAL PARMAS --- # 

cmap = LinearSegmentedColormap.from_list("custom_map", COLOR)
plt.figure(figsize=(8, 8))
plt.axis("off")
plt.title("Ajout d'une goutte sphérique - profil coloré")



for point_impact in liste_points_impact : 

    chemin.append(point_impact)

    mat_initiale  = algo_une_goutte(mat_initiale, point_impact) 
    mat_finale = np.clip(mat_initiale , 0, MAX_HEIGHT)
    plt.imshow(mat_initiale, cmap=cmap, vmin=MIN_HEIGHT, vmax=MAX_HEIGHT, interpolation="nearest")

    x_vals = [p[0] for p in chemin]
    y_vals = [p[1] for p in chemin]

    plt.plot(x_vals, y_vals, color='green', marker='o', linewidth=1)
    # plt.colorbar(label="Hauteur (0-1000)")
    plt.pause(0.2)

























# def droplet(block) : 
#     # ici qu'on appelle l'ia 

#     # determine taille du block ( taille impactée + une marge )

#     #déterminer propriétés utiles 
#     # 1ere passe ou plusieurs passes
#     # propriétés couche de départ
#     # propriétés gouttes
#     # propriétés thermiques
#     # propriétés process : inclinaison, etc... 


#     # Parameters	Scope
#     # O2 flow (slpm)	200–240
#     # CH4 flow (slpm)	120–200
#     # Air flow (slpm)	300
#     # Carrier gas flow (slpm)	40
#     # stand-off distance (mm)	200–320
#     # Spray gun speed (mm/s)	400
#     # Powder feeding speed (g/min)	30


#     # format sortie liste de liste de float 

#     return block 

# #définisse un sens pour itérer 
# for block in mat_initiale : 

#     coordonnée_bloc = 0

#     # mat_finale[coordonnée_bloc] =  droplet(block)