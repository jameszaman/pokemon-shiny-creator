from PIL import Image
from tqdm import tqdm
from src.pokemon_sprites import download_pokemon_sprites
from src.misc_functions import always_positive
from src.image import to_image

import os
import shutil
import numpy as np


def shiny(image):
  shiny_maker = np.random.randint(100, 200)
  shiny_index = np.random.randint(0, 3)

  image_array = np.array(image)
  for i in range(len(image_array)):
    for j in range(len(image_array[i])):
      image_array[i][j][shiny_index] = always_positive(shiny_maker - image_array[i][j][shiny_index])
  
  return to_image(image_array)

def generate_shinies(pokemon_folder='pokemons', shiny_folder='shinies'):
  # If pokemon sprites do not exist, download them.
  if os.path.exists(pokemon_folder):
    filenames = os.listdir(pokemon_folder)
    if len(filenames) == 0:
      download_pokemon_sprites(pokemon_folder)
      filenames = os.listdir(pokemon_folder)
  else:
    download_pokemon_sprites(pokemon_folder)
    filenames = os.listdir(pokemon_folder)

  # If a folder already exists, remove it.
  if os.path.exists(shiny_folder):
    shutil.rmtree(shiny_folder)
  os.makedirs(shiny_folder)

  # Creating shinies.
  for filename in tqdm(filenames, desc="Generating new shiny sprites"):
    image = Image.open(f'{pokemon_folder}/{filename}')
    for i in range(1):
      shiny(image).save(f'{shiny_folder}/{filename}')