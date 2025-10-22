def main():
    # Diccionario de números a letras
    numeros_letras = {
        0: "Cero",
        1: "Uno",
        2: "Dos",
        3: "Tres",
        4: "Cuatro",
        5: "Cinco",
        6: "Seis",
        7: "Siete",
        8: "Ocho",
        9: "Nueve"
    }

    # Pedimos el número al usuario
    num = int(input("Introduce un número de una cifra (0-9): "))

    # Verificamos que sea de una cifra
    if 0 <= num <= 9:
        print("Número en letras:", numeros_letras[num])
    else:
        print("¡Error! Debes introducir un número de una sola cifra.")

if __name__ == "__main__":
    main()
