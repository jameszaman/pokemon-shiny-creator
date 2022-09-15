from PIL import Image


def to_image(arr):
  if type(arr) != 'numpy':
    return Image.fromarray(arr)
  elif type(arr) == 'list':
    return Image.fromarray(np.array(arr))
  else:
    raise Exception(f'Invalid type: {type(arr)}')