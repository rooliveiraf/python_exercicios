velocidade = float(input("Coloque aqui uma velocidade, em km/h: "))

excesso_velocidade = velocidade - 80
multa = excesso_velocidade * 5

if velocidade > 80:
    print("Você foi multado! O valor da multa é R$ %4.2f" % (multa))

if velocidade <= 80:
    print("Tudo certo, boa viagem!")
