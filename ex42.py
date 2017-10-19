velocidade = float(input("Velocidade veículo:"))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Valor da multa: R$ %7.2f!" % multa)
if velocidade <=80:
    print("OK")
