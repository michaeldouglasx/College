num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

if num1>num2 and num1>num3:
    print(f'O Número {num1} é o maior!')
elif num2>num1 and num2>num3:
    print(f'O Número {num2} é o maior!')
else:
    print(f'O número {num3} é o maior!')