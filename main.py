from PIL import Image
from pprint import pprint
from random import randint
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
  shiny_maker = randint(0, 255)
  shiny_index = np.random.randint(0, 3)
  print(shiny_maker, shiny_index)

  image_array = np.array(image)
  for i in range(len(image_array)):
    for j in range(len(image_array[i])):
      image_array[i][j][shiny_index] = always_positive(shiny_maker - image_array[i][j][shiny_index])
  
  return to_image(image_array)


filename = 'pikachu-f.png'
image = Image.open(filename)
image.show()

for i in range(5):
  shiny(image).show()
