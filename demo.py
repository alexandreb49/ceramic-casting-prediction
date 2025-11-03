import matplotlib.pyplot as plt
import numpy as np
import random

MIN_HEIGHT = 0
MAX_HEIGHT = 255
IMAGE_RESOLUTION = 100

mat_initiale = np.array( [[random.randint(MIN_HEIGHT, MAX_HEIGHT) for _ in range(IMAGE_RESOLUTION)] for __ in range(IMAGE_RESOLUTION)],dtype=np.uint8)



class ProcessIterator(np.ndarray) :

    pass 

    # def __iter__(self) : 

    #     for block in

    #         yield block 

mat_finale = np.array([])

def droplet(block) : 
    # ici qu'on appelle l'ia 

    # determine taille du block ( taille impactée + une marge )

    #déterminer propriétés utiles 
    # 1ere passe ou plusieurs passes
    # propriétés couche de départ
    # propriétés gouttes
    # propriétés thermiques
    # propriétés process : inclinaison, etc... 


    # Parameters	Scope
    # O2 flow (slpm)	200–240
    # CH4 flow (slpm)	120–200
    # Air flow (slpm)	300
    # Carrier gas flow (slpm)	40
    # stand-off distance (mm)	200–320
    # Spray gun speed (mm/s)	400
    # Powder feeding speed (g/min)	30


    # format sortie liste de liste de float 

    return block 

#définisse un sens pour itérer 
for block in mat_initiale : 

    coordonnée_bloc = 0

    mat_finale[coordonnée_bloc] =  droplet(block)


plt.imshow(mat_finale, cmap="gray", vmin=MIN_HEIGHT, vmax=MAX_HEIGHT, interpolation="nearest")
plt.axis("off")
plt.show()
