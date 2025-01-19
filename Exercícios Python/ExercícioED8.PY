produto1 = int(input('Digite o preço de um produto: '))
produto2= int(input('Digite o preço do segundo produto: '))
produto3 = int(input('Digite o preço do terceiro produto: '))

if produto1 < produto2 and produto1 < produto2:
    print(f'Você deve comprar o produto 1 de R$ {produto1} reais !')
if produto2 < produto1 and produto2 < produto3:
    print(f'Você deve comprar o produto 2 de R$ {produto2} reais !')
else:
    print(f'Você deve comprar o produto 3 de R$ {produto2} reais !')

