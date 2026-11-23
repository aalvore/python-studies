valores = list()
posicoesM = list()
posicoesm = list()
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
maior = max(valores)
menor = min(valores)
for v in enumerate(valores):
    if v[1] == maior:
        posicoesM.append(v[0])
    if v[1] == menor:
        posicoesm.append(v[0])

print(f'O maior valor digitado foi {maior} e ele esta nas posições {posicoesM}',)
print(f'O menor valor digitado foi o {menor} e ele esta nas posições {posicoesm}')