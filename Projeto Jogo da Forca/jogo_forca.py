import uteis, img_forca, os
import manip_texto as txt

## MAIN ##
while True:
  level = 0

  input('APERTE QUALQUER TECLA PARA INICIAR')
  os.system('cls')

  uteis.cabecalho('JOGO DA FORCA')
  print('''
  ESCOLHA O TEMA:
  \t1 - JOGO
  \t2 - FILME
  \t0 - SAIR
        ''')

  while True:
    try:
      opcao = int(input('\t-> '))
    except:
      print(' ## Escolha um valor válido! ##')
    else:
      break
  nome_escolhido, nome_secreto = txt.sorteio_nome(opcao)
  letras_acumulada = ''
  os.system('cls')

  while True:
    print (f'\n{nome_secreto}\n')
    img_forca.mostra_forca(level)
    print(letras_acumulada)

    letra = uteis.verifica_letra(letras_acumulada)
    letras_acumulada += letra + ' '

    if nome_escolhido.count(letra) == 0:
      level += 1
    else:
      nome_secreto = uteis.revela_letra(nome_escolhido, nome_secreto, letra)

    if not '_' in nome_secreto:
      print('Você acertou! O título se chama: ', nome_escolhido, '\n')
      break
    elif level > 6:
      print('Você não acertou! O título era: ', nome_escolhido, '\n')
      break
    os.system('cls')