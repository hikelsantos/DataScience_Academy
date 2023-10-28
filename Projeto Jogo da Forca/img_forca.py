def mostra_forca(level):
  print(' +------+')
  print(' |      |')

  if level >= 1:
    print(' |      0')
  else:
    print(' |')

  if level == 2:
    print(' |      |')
  elif level == 3:
    print(' |     /|')
  elif level >= 4:
    print(' |     /|\\')
  else:
    print(' |')
        
  if level == 5:
    print(' |     /')
  if level >= 6:
    print(' |     / \\')
  else:
    print(' |')

  print(' |')
  print('==========')
