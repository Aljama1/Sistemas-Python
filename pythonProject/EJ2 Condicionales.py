n = int(input("Ingresa el número de alumnos: "))
total = 0
if n > 0:
    if n < 30:
            total = 4000
    else:
        if n <=49:
            total = n * 95
        else:
            if n <= 99:
                total = n * 70
            else:
                total = n * 65
    print(f"En total la compañia se llevará:  {total}€")
    print(f"Cada alumno pagará: {total/n}€")