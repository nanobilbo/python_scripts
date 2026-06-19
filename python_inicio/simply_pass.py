# pedir la contraseña al usuario
password = input("aqui tu conbtraseña:")

#verificar la longitud y contenido de la contraseña
if len(password) < 10:
    print(" la tienes demasiado corta(minimo 10 caracteres)")
elif password.isalpha(): #si solo ha puesto letras
    print(" la contraseña debe contener al menos un número")
elif password.isdigit(): # si solo ha puestto numeros
    print(" la contraseña debe contener al menos una letra")
else:
    print("la contraseña vale")
"""
vale si no se cumplen los reuisitos el programa se finaliza sin dar 
otra oportunidad. solucion bucle while true para que pregunte 
hasta que ponga bien la contraseña
"""
#while True:
 #   password = input("aqui tu conbtraseña:")