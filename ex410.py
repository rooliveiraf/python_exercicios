energia_utilizada = float(input("Insira aqui a quantidade de energia utilizada (em kWh): "))
tipo = input("Qual o tipo da instalação (residencial (R), industrial (I) ou comercial (C))?")

if tipo == "R":
    if energia_utilizada <= 500:
        preco = 0.40
    else:
        preco = 0.65
        
elif tipo == "C":
    if energia_utilizada <=1000:
        preco = 0.55
    else:
        preco = 0.60
        
elif tipo == "I":
    if energia_utilizada <= 5000:
        preco = 0.55
    else:
        preco = 0.60

else:
    preço = 0
    print("Isira um caractere válido!")
    
total = energia_utilizada * preco

print("O total a pagar é R$ %6.2f." % (total))
