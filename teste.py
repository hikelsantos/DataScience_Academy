with open('lista_jogos.txt', encoding='utf8') as lista:
  conteudo = lista.read().split('\n').upper()
  
  print(conteudo)
  for indice in conteudo:
    print(indice)
    indice = indice.replace('Á', 'A')
    indice = indice.replace('É', 'E')
    indice = indice.replace('Í', 'I')
    indice = indice.replace('Ó', 'O')
    indice = indice.replace('Ú', 'U')
  print(conteudo)