num1 = float(input("Digite um número: "))
num2 = float (input("Digite um outro número: "))
operacao = input("Escolha uma operação: \n Divisão (/) \n Multiplicação (*) \n Divisão por inteiro (//) \n Sobra da divisão (%) \n soma (+) \n subtração (-): ")

if operacao == '+':
    soma = num1 + num2
    print (f" o resultado é: {soma}!")
elif operacao == '-':
    subtracao = num1 - num2
    print(f" o resultado é: {subtracao}!")
elif operacao == '/':
    if num2 != 0:
        divisao = num1 / num2
        print (f" o resultado é: {divisao}!")
    else:
        print("Erro! Divisão por 0 não é permitida!")
elif operacao == '//':
    if num2 != 0:
        div_inteiro = num1 // num2
        print (f" o resultado é: {div_inteiro}!")
    else:
        print ("ERRO! Divisão por 0 não é permitida")
elif operacao == '%':
    if num2 != 0:
        sobra_div = num1 % num2
        print(f" o resultado é: {sobra_div}!")
    else:
        print ("ERRO! Divisão por 0 não é permitida")
elif operacao == '*':
    multiplicacao = num1 * num2
    print(f" o resultado é: {multiplicacao}!" )


