from PIL import Image
from pprint import pprint
from random import randint
from pokemon_image import get_pokemon
import numpy as np
import os
import shutil


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


# If pokemon sprites do not exist, download them.
if os.path.exists('pokemons'):
  filenames = os.listdir('pokemons')
  if len(filenames) == 0:
    get_pokemon()
    filenames = os.listdir('pokemons')
else:
  get_pokemon()
  filenames = os.listdir('pokemons')


# If a folder already exists, remove it.
if os.path.exists('shinies'):
  shutil.rmtree('shinies')
os.makedirs('shinies')

# Creating shinies.
for filename in filenames:
  image = Image.open(f'pokemons/{filename}')
  for i in range(1):
    shiny(image).save(f'shinies/{filename}')


