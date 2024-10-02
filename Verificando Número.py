algo = input('digite algo: ')

if algo.isnumeric():
    
    print ('Esse dado é um número!')
    
elif algo.isalpha():
    
    print('Esse dado é uma letra!')
    
elif algo.isalnum():
    
    print('Esse dado é uma alfanumerico')
    
else:
    print ('Não é um número, letra ou alfanumerico!')

print ("o tipo primitivo desse dado é:", type (algo))

print ('É alfabeto? ', algo.isalpha())

print ('É númerico? ', algo.isnumeric())

print ('É apenas um espaço? ', algo.isspace())

print ('E alfa numérico?', algo.isalnum ())

print ('Está em letras maiúsculas?', algo.isupper())

print ('Está em letras minúsculas?  ', algo.islower())

print ('Está capitalizado', algo.istitle())
