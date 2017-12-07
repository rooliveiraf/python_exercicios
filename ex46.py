distancia = float(input("Insira aqui uma distância a ser percorrida em km: "))

if distancia <= 200:
    valor_passagem = distancia * 0.5
    print("O valor total de sua passagem é de R$ %5.2f." % (valor_passagem))
else:
    valor_passagem = distancia * 0.45
    print("O valor total de sua passagem é de R$ %5.2f." % (valor_passagem))
