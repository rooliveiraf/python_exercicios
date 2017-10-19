salário = float(input("Salário:"))
pc_aumento = 0.15
if salário > 125015 / 100:
    pc_aumento = 10 / 100
aumento = salário * pc_aumento
print("Aumento: R$ %7.2f" % aumento)
