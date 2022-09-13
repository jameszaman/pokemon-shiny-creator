from bs4 import BeautifulSoup
from tqdm import tqdm

import requests
import os


def download_file(url, local_filename):
  user_agent = 'Mozilla/5.0'
  # NOTE the stream=True parameter below
  with requests.get(url, stream=True, headers={'User-Agent': user_agent}) as r:
    r.raise_for_status()
    with open(local_filename, 'wb') as f:
      for chunk in r.iter_content(chunk_size=8192): 
        # If you have chunk encoded response uncomment if
        # and set chunk_size parameter to None.
        #if chunk: 
        f.write(chunk)
  return local_filename

def download_pokemon_sprites(folder_name):
  user_agent = 'Mozilla/5.0'
  initial_url = 'https://pokemondb.net/sprites'
  data = requests.get(initial_url, stream=True, headers={'User-Agent': user_agent})
  soup = BeautifulSoup(data.content, 'html.parser')
  
  all_a_tags =  soup.find_all('a')
  pokemon_names = [tag.get('href', {'class': 'infocard'})[9:] for tag in all_a_tags if tag.get('href', {'class': 'infocard'}).startswith('/sprites/')]
  
  image_url = 'https://img.pokemondb.net/sprites/home/normal/'

  # Need to make sure that a folder exists for saving sprites
  if not os.path.exists(folder_name):
    os.makedirs(folder_name)
  
  # In case the folder already exists, there is a chance pokemons are already downloaded.
  pokemon_list = os.listdir(folder_name)
  
  for name in tqdm(pokemon_names, desc="downloading pokemon sprites"):
    if f'{name}.png' not in pokemon_list:
      download_file(f'{image_url}/{name}.png', f'{folder_name}/{name}.png')

if __name__ == '__main__':
  download_pokemon_sprites('pokemons')
