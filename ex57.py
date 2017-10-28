n = int(input("Insira o número que deseja a tabuada:"))
início = int(input("De:"))
fim = int(input("Até:"))
x = início
while x <= fim:
    print( "%d x %d = %d" % (n , x , x*n))
    x=x+1

    
