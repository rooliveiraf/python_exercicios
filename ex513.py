total_dívida = float(input("Total da dívida:"))
taxa = float(input("Juros aplicados sobre a dívida:"))
amortização = float(input("Amortizações mensais:"))
mês = 1

saldo = total_dívida
juros_pago = amortização

while saldo > amortização:
    juros = saldo * (taxa / 100)
    saldo = saldo + juros - amortização
    juros_pago = juros_pago + juros
    print("O saldo da dívida no mês %d é de R$ %6.2f" % (mês, saldo))
    mês = mês + 1

print("Pagando uma dívida de %8.2f com a incidência de %4.2f %% de juros mensais" % (total_dívida, taxa))
print("o valor será quitado em %d meses e o montante total de juros pagos será de %8.2f." % (mês, juros_pago))


    
    

