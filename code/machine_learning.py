# import keras
# import tensorflow as tf 



# # parametres 
# NEURONS_PER_LAYER = 128
# SIZE = 0.8



# #importation des données 
# X, Y = [],[]


# #formattage des données + normalization


# # RBG() +  [ [ [255,45,85]     ]] => NOIR ET BLANC [ [ values ]] 



# #split les données val, training 
# X_train, Y_train = X[:SIZE * len(X)], Y[:SIZE * len(X)]

# #créer le modele 
# model = keras.Sequential([
#         keras.layers.Input(shape=(X.shape[0], X_train_norm.shape[2])),
        
#         # Lightweight architecture for 4GB Docker constraints
#         keras.layers.Conv1D(NEURONS_PER_LAYER, kernel_size=3, activation='relu', padding='same'),
#         # Single LSTM layer
#         keras.layers.LSTM(NEURONS_PER_LAYER//2, return_sequences=False),
#         # Single dense layer
#         keras.layers.Dense(NEURONS_PER_LAYER//4, activation='relu'),
#         # Output layer for 3 classes
#         keras.layers.Dense(3, activation='softmax', dtype='float32')
#     ])


# # entrainement + validation
# optimizer = keras.optimizers.Adam(learning_rate=0.001, clipnorm=1.0)  # Add gradient clipping
# model.compile(
#     loss='categorical_crossentropy',
#     optimizer=optimizer,
#     metrics=['accuracy']
# )



import tensorflow as tf
import keras 
import keras.layers as layers



particles_layers = []

# input= 
# output = 

particles_model = keras.Sequential(particles_layers)



INPUT_SHAPE = (64,64,64,1)

main_model = keras.Sequential([
    layers.Conv3D(64, (3,3,3), activation='relu', padding='same', input_shape=INPUT_SHAPE),
    layers.AvgPool3D((2,2,2)),

    layers.Conv3D(128, (3,3,3), activation='relu', padding='same'),
    layers.AvgPool3D((2,2,2)),

    layers.Conv3D(64, (3,3,3), activation='relu', padding='same'),
    
    # --- dernière couche convolutionnelle qui produit une matrice 3D ---
    layers.Conv3D(1, (1,1,1), activation='relu', padding='same')  
])











