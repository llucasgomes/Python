import operacoes
    


print('Calculadora')
print('\nMenu','\n\n1 - Somar','\n2 - Subtrair','\n3 - Multiplicar','\n4 - Dividir')


op = int(input('\n\nInsira a operação: '))
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

if op == 1:
    print(operacoes.soma(n1,n2))
elif op == 2:
    print(operacoes.sub(n1,n2))
elif op == 3:
    print(operacoes.vezes(n1,n2))
elif op == 4:
    print(operacoes.div(n1,n2))
