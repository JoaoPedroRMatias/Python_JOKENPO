import random 
import time

game = ('pedra', 'papel', 'tesoura')
computador = random.randint(0,2)

print('-=' * 30)
print('ESCOLHA UMA DAS OPÇÕES:')
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
print('-=' * 30)

while True:
    try:
        player = int(input('Qual sua escolha?'))
        if player != 1 and player != 2 and player != 3:
            print('Escolha apenas entre as opções apresentadas!')
        else:
            break
    except ValueError:
        print('Escolha apenas entre as opções apresentadas!')

print('[JO]')
time.sleep(1)
print('[KEN]')
time.sleep(1)
print('[PÔ!!!]\n')
time.sleep(1)

if game[computador] == 'pedra':
    if player == 1:
        print('EMPATE\n')
    if player == 2:
        print('GANHOU\n')
    if player == 3:
        print('PERDEU\n')

if game[computador] == 'papel':
    if player == 1:
        print('PERDEU\n')
    if player == 2:
        print('EMPATE\n')
    if player == 3:
        print('GANHOU\n')

if game[computador] == 'tesoura':
    if player == 1:
        print('GANHOU\n')
    if player == 2:
        print('PERDEU\n')
    if player == 3:
        print('EMPATE\n')

print("A máquina escolheu:", game[computador])