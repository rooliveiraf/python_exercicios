cigarros_por_dia=int(input("Cigarros por dia:"))
anos_fumando=float(input("Anos fumando:"))
redução_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
redução_em_dias = redução_em_minutos / (24 * 60)
print("Redução do tempo de vida %9.2f dias." % redução_em_dias)
