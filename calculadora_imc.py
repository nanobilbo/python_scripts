#creamos los inputs para pedir peso y altura
peso = float(input("ingresa tu peso en kg: "))
altura = float(input("ingresa tu altura en metros: "))
#formula para calcular el imc
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Tienes bajo peso")
elif imc < 25:
    print("Tienes un peso normal")
elif imc < 30:
    print("Tienes sobrepeso")
else:
    print("Tienes obesidad")
    