extenso = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    ler = int(input('Digite um numero de 1 ate 10: '))

    if 1 <= ler <= 10:
        break

    print('Tente novamente.', end=' ')


print(f'Voce digitou o numero {extenso[ler - 1]}')
