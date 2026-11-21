vazia = ()

for numero in range(1, 5):
    valor = int(input('Digite um valor: '))
    tupla = valor,
    vazia = vazia + tupla

par = ()
for numeros in vazia:
    if numeros % 2 == 0:
        par += (numeros,)

print(f'Voce digitou os valores {vazia}')

print(f'O valor de 9 apareceu {vazia.count(9)} vezes')
if not 3 in vazia:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {vazia.index(3)} posição')
print(f'Os valores pares digitados foram {par}')