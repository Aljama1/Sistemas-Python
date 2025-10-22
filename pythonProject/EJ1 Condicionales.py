lado1 = float(input("A:"))
lado2 = float(input("B:"))
lado3 = float(input("C:"))

if lado1 ** 2 == (lado2 ** 2 + lado3 ** 2):
    print("Rectangulo")
if lado1 == lado2 and lado2 == lado3:
    print("Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isósceles")
else:
    print("Escaleno")