'''from random import randint

tupla = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
menor = tupla[0]
maior = tupla[0]

for numero in tupla:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')'''

from random import randint
tupla = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print('Os valores sorteados foram: ', end='')
for numero in tupla:
    print(f'{numero} ', end='')
print(f'\nO maior valor sorteado foi o {max(tupla)}')
print(f'O menor valor sorteado foi o {min(tupla)}')