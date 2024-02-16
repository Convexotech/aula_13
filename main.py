import random

#essencial 
for n in range(1,4):
    print('chance nº', n)
    aleatorio =  random.randint(1,2)
    meu_numero = int(input('Chute >'))
    if aleatorio == meu_numero:
       print('Você ganhou o Jogo ')
       break
    else:
       print('você perdeu > ', aleatorio)
     





















   
 














