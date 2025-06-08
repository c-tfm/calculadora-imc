def name():
#Aqui llenamos los datos
    while True:
        nombres = input("Ingrese su nombre (uno o dos): ").strip()
        if nombres:
            partes = nombres.split()
            if 1 <= len(partes) <= 2:
                return nombres
            else:
                print("Solo se permiten uno o dos nombres.")
        else:
            print("El texto no puede estar vacío. Inténtelo de nuevo.")
#Arriba limitamos a 2 nombres, y también los separamos
#Limitamos a que no puedan existir campos vacíos
def text(campo):
    while True:
        value = input(f"Ingrese su {campo}: ").strip()
        if value:
            return value
        else:
            print("El texto no puede estar vacío. Inténtelo de nuevo.")

def num(campo, tipo=float):
    while True:
        value = input(f"Ingrese su {campo}: ").strip()
        if not value:
            print("El número no puede estar vacío. Inténtelo de nuevo.")
            continue
        try:
            numero = tipo(value)
            if tipo == float and numero <= 0:
                print("El número tiene que ser mayor a 0.")
            else:
                return numero
        except ValueError:
            print("Ingrese un número válido.")
#Aquí metemos un bucle, así si se quiere usar mas de una vez puede hacerlo
while True:
#Aquí es donde se muestran los datos al usuario

    nombres = name()
    apellidop = text("apellido paterno")
    apellidom = text("apellido materno")
    edad = num("edad", int)
    peso = num("peso en kg", float)
    estatura = num("estatura en metros NO usar cm", float)

    imc = peso/(estatura**2)

    print("\n--- Datos del Usuario ---")
    print("Nombre completo:", nombres, apellidop, apellidom)
    print("Edad:", edad, "años")
    print("Peso:", peso, "kg")
    print("Estatura:", estatura, "m")
    print("IMC:", round(imc))

# Aquí se determina la categoría del IMC
    if imc >= 0 and imc <= 15.99:
        print("Categoría de IMC: Delgadez severa, se recomienda visitar a un nutriologo")
    elif imc >= 16.00 and imc <= 16.99:
        print("Categoría de IMC: Delgadez moderada, se recomienda visitar a un nutriologo")
    elif imc >= 17.00 and imc <= 18.49:
        print("Categoría de IMC: Delgadez leve, se recomienda tomar precauciones para estar en un peso saludable")
    elif imc >= 18.50 and imc <= 24.99:
        print("Categoría de IMC: ¡Felicidades! Tu IMC es normal :) ¡Que saludable!")
    elif imc >= 25.00 and imc <= 29.99:
        print("Categoría de IMC: Sobrepeso, se recomienda tomar precauciones para estar en un peso saludable")
    elif imc >= 30.00 and imc <= 34.99:
        print("Categoría de IMC: Obesidad leve, se recomienda visitar a un nutriologo")
    elif imc >= 35.00 and imc <= 39.99:
        print("Categoría de IMC: Obesidad media, se recomienda visitar a un nutriologo")
    elif imc >= 40.00:
        print("Categoría de IMC: Obesidad mórbida, se recomienda visitar a un nutriologo")

# Preguntar si desea repetir, para esto metimos el bucle
    repetir = input("\n¿Quieres agregar otros datos? Si/No: ").strip().lower()
    if repetir != "si":
        print("Perfecto, ¡Que tengas buen día! Hasta luego")
        break
