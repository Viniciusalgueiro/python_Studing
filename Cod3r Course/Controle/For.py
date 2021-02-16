print(f'Esses são os numeros de 1 até 10: ')
for i in range(10):
    print(i, end =' ')


print(f'esses são os numeros de 1 até 11 sem mostrar o 11: ')
for i in range(1, 11):
    print(i , end =' ')

print(f'esses são os numeros de 1 até 100 indo de 5 em 5:')
for i in range(0, 100, 5):
   print( i, end=' ')

nums = [2, 4, 6, 8 ]

for n in nums:
    print(n, end='')

texto = 'keep studing Python'

for letra in texto:
    print(letra, end =' ') 

produto = {
    'Produto': 'caneta',
    'preço': 8.80,
    'desc': 0.5
}

for atrib in produto:
    print(atrib, '=>', produto[atrib])

for atrib in produto.keys():
    print(atrib, end =' ')