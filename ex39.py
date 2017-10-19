dias = int(input("Dias do usuário: "))
horas = int(input("Horas do usuário: "))
minutos = int(input("Minutos do usuário: "))
segundos = int (input("Segundos do usuário: "))

total = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + (segundos)

print("O total em segundos é %d ." % total)
