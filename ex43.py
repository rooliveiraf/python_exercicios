a=int(input("Primeiro valor:"))
b=int(input("Segundo valor:"))
c=int(input("Terceiro valor:"))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print("menor número: %d" % menor)
print("maior número: %d" % maior)

