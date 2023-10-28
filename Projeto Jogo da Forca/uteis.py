def cabecalho(texto, pula_linha = False):
    print('+-=-=-=-=-=-=-=-=-=-+')
    print(f'{texto:^21}')
    print('+-=-=-=-=-=-=-=-=-=-+')
    if pula_linha == True:
      print('')

def verifica_letra(letras_acumulada):
  while True:
    letra = str(input('\nEscolha uma letra\n\t-> ')).strip().upper()[0]
    if letra.isalpha():
      if not letra in letras_acumulada:
        break
      else:
        print(' ## Valor já inserido! ##')
    else:
        print(' ## Digite apenas letras! ##')
  return letra

def revela_letra(nome_escolhido, nome_secreto, letra):
      nome_temp = list(nome_secreto)
      for posicao, indice in enumerate(nome_escolhido):
        if indice == letra:
          nome_temp[posicao] = letra
      nome_secreto = ''.join(nome_temp)
      return nome_secreto