valores = list()
par = list()
impar = list()
resposta = 'S'

while resposta == 'S':
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

    valores.append(valor)
    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

print(f'A lista completa é {valores}')
print(f'A lista completa de pares é {par}')
print(f'A lista completa de impares é {impar}')
