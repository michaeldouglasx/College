vendas = [
    ("Iphone", 500, 200),
    ('Samsung', 400, 5000),
    ("Xiaomi", 200, 150)
]

for produto, vendas2019, vendas2020 in vendas:
    if vendas2020>vendas2019:
        crescimento = vendas2020/vendas2019 -1
        print (f"{produto} vendeu {vendas2019} celulares em 2019 e {vendas2020} celulares em 2020, e teve um crescimento de {crescimento :.0%}")