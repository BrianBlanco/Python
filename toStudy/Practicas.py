print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicacion")
print("4 - Division")
print("5 - Exponente")

arrayOperador = ["Suma", "Resta", "Multiplicacion", "Division", "Exponente"]

continuarBucle = True

while continuarBucle:
    operador = input("Dime un operador ")
    print(operador)

    if operador in arrayOperador:
        numero1 = int(input("Dime el primer numero\n"))

        numero2 = int(input("Dime el segundo numero\n"))

        if operador == "Suma":
            resultado = numero1 + numero2
        elif operador == "Resta":
            resultado = numero1 - numero2
        elif operador == "Multiplicacion":
            resultado = numero1 * numero2
        elif operador == "Division":
            if numero2 == 0:
                resultado = "Error (no se puede dividir entre 0)"
            else:
                resultado = numero1 / numero2
        elif operador == "Exponente":
            resultado = numero1 ** numero2

    else:
        resultado = "Te has equivocado"

    print(resultado)

    opcionCorrecta = True

    while opcionCorrecta:
        eleccionPersona = input("Repetir operacion S/N ")
        opcionCorrecta = False
        
        if eleccionPersona == "NO" or eleccionPersona == "No" or eleccionPersona == "N" or eleccionPersona == "n":
            continuarBucle = False

        elif eleccionPersona == "SI" or eleccionPersona == "Si" or eleccionPersona == "S" or eleccionPersona == "s":
            continuarBucle = True
        else:
            opcionCorrecta = True