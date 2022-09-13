from PIL import Image
from tqdm import tqdm
from pprint import pprint
from random import randint
from pokemon_image import download_pokemon_sprites

import os
import shutil
import numpy as np


def to_image(arr):
  if type(arr) != 'numpy':
    return Image.fromarray(arr)
  elif type(arr) == 'list':
    return Image.fromarray(np.array(arr))
  else:
    raise Exception(f'Invalid type: {type(arr)}')

def full_print(arr):
  for i in arr:
    for j in i:
      print(j)

def always_positive(num):
  if num < 0:
    return num * -1
  return num

def shiny(image):
  shiny_maker = randint(100, 200)
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

if __name__ == '__main__':
  generate_shinies()