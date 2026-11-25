valores = list()
resposta = 'S'
while resposta == 'S':
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Numero duplicado! não vou adicionar...')
    else:
        valores.append(valor)

    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print(f'Vc digitou os valores {sorted(valores)}')