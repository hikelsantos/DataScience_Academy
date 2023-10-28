from sys import exit
from random import randrange

def ocultar_texto(texto):
  texto_secreto = ''
  for indice in texto:
    if indice == ':':
      texto_secreto += ':'
    elif indice == '\'':
      texto_secreto += '\''
    elif indice == '&':
      texto_secreto += '&'
    elif indice == ' ':
      texto_secreto += ' '
    elif indice == '-':
      texto_secreto += '-'
    elif indice != '\n':
      texto_secreto += '_'  

  return texto_secreto

def sorteio_nome(escolha):
  if escolha == 1:
    with open('lista_jogos.txt', 'r') as lista_nomes:
      lista_nomes = list(lista_nomes)
      
  elif escolha == 2:
    with open('lista_filmes.txt', 'r') as lista_nomes:
      lista_nomes = list(lista_nomes)
  else:
    exit()
    
  nome_escolhido = lista_nomes[randrange(1, len(lista_nomes)+1)]
  nome_escolhido = nome_escolhido[:-1]
  nome_secreto = ocultar_texto(nome_escolhido)
  
  return nome_escolhido, nome_secreto