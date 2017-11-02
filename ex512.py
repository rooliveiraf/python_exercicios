taxa_de_juros = float(input("Digite a taxa de juros mensal:"))
principal = float(input("Digite o valor depositado inicalmente:"))
depósito_mensal = float(input("Digite o valor dos depósitos mensais:"))
mês = 1
saldo = principal
while mês <= 24:
    saldo = saldo + depósito_mensal + (saldo * (taxa_de_juros/100))
    print ("Saldo do mês %d é de R$ %5.2f" % (mês, saldo))
    mês = mês + 1

print ("O total obtido com a taxa sugerida no período foi de %8.2f" % (saldo - principal))

