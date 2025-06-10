num = int(input('Digite o número para ver a tabuada: '))

print('Sua tabuada é:')
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
