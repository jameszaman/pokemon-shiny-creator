import requests
import os
from bs4 import BeautifulSoup


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

def get_pokemon():
  user_agent = 'Mozilla/5.0'
  initial_url = 'https://pokemondb.net/sprites'
  data = requests.get(initial_url, stream=True, headers={'User-Agent': user_agent})
  soup = BeautifulSoup(data.content, 'html.parser')
  
  all_a_tags =  soup.find_all('a')
  pokemon_names = [tag.get('href', {'class': 'infocard'})[9:] for tag in all_a_tags if tag.get('href', {'class': 'infocard'}).startswith('/sprites/')]
  
  image_url = 'https://img.pokemondb.net/sprites/home/normal/'

  # Need to make sure that a folder exists for saving sprites
  if not os.path.exists('pokemons'):
    os.makedirs('pokemons')
  
  # In case the folder already exists, there is a chance pokemons are already downloaded.
  pokemon_list = os.listdir('pokemons')
  
  for name in pokemon_names:
    if f'{name}.png' not in pokemon_list:
      download_file(f'{image_url}/{name}.png', f'pokemons/{name}.png')

