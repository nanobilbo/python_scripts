# clasificador de edades

edad = int(input("ingresa tu edad: "))

if edad < 0 or edad > 120:
    print ("edad no valida")
elif edad < 12:
    print("eres un niño")
elif edad < 18:
    print("eres adolescente pajillero")
elif edad < 65:
    print("eres adulto")
else:
    print(" eres un jubileta")