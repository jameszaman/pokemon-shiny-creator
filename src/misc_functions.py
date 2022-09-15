def full_print(arr):
  for i in arr:
    for j in i:
      print(j)

def always_positive(num):
  if num < 0:
    return num * -1
  return num