nota = float(input( 'Informe a nota do aluno: '))
comportado = True if input('Comportado ? (s/n) ') == 's' else False

if nota >= 9 and comportado :
    print(' Voce passou com SS !! ')
    print(' Parabens')
    print(' Voce entrou para o Quadro de Honra ')

elif nota >= 7:
    print('Aprovado com MS')


elif nota >= 6:
    print('Aprovado com MM')

else:
    print('Reprovado')


print (nota)