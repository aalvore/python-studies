valores = list()
resposta = 'S'

while resposta == 'S':
    valores.append(int(input('Digite um valor: ')))

    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

print(f'{len(valores)} numeros foram digitados')
print(f'{sorted(valores, reverse=True)} em ordem decrescente')
if 5 in valores:
    print('O numero 5 foi digitado, e está na lista.')
else:
    print('O numero 5 não foi digitado, e não está na lista.')