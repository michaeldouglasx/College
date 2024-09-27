algo = input('digite algo: ')
if algo.isnumeric():
    print ('Esse dado é um número!')
elif algo.isalpha():
    print('Esse dado é uma letra!')
elif algo.isalnum():
    print('Esse dado é uma alfanumerico')
else:
    print ('Erro')