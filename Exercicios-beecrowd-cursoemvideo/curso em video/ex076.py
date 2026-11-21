preços = ('Pao', 1, 'Macarrao', 10, 'Frango', 50, 'Feijoada', 20, 'Lapis', 3)

print('LISTAGEM DE PREÇOS')
for produto in range(0, len(preços), 2):
    print(f'{preços[produto]}.....\tR${preços[produto + 1]}')