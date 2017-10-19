distância=float(input("Distância almejada (km):"))
if distância <= 200:
    passagem = 0.5 * distância
else:
    passagem = 0.45 * distância
print("Preço da passagem: R$ %7.2f" % passagem)
