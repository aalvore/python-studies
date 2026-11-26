listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}:')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'Todos os numeros digitados na lista foram {listanum}')
print(f'O maior numero digitado foi o {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if listanum[i] == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor numero digitado foi o {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if listanum[i] == menor:
        print(f'{i}... ', end='')
print()
