total = 0
nota = 0
qtde = 0 

'''while x <100:
    x = x + 5  
    print(x)'''

while nota != -1:
    total += float(input('Informe a nota ou 5 oara sair:'))
    if nota != -1:
        qtde += 1
        total += nota

print('A média da turma é {total / qtde } ')

