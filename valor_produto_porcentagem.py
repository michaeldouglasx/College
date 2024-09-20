entrada =input("digite os valores dos produtos separados por virgula: ")

valor_produto = [float(valor) for valor in entrada.split(",")]
acrescimo = float(input("Qual a porcentagem desejada?")) /100

for preco in valor_produto:
    novo_preco = preco * (1 + acrescimo)
    print (novo_preco)
