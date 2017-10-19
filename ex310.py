salário = float(input("Salário: "))
aumento_percentual = float(input("Porcentagem do aumento: "))
aumento = salário * aumento_percentual / 100
salário_final = salário + aumento

print("Valor do aumento: %7.2f" % aumento)
print("Salário final: %7.2f" % salário_final)

