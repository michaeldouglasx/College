idade = int(input("Digite sua idade: "))
if idade < 10:
    print ("Você é uma criança! ")
elif 11 <= idade < 18:
    print("Você é um(a) pré adolescente! ") 
elif 18 <= idade < 65:
    print("Você é um adulto! ")
else:
    print("Você é um idoso! ")