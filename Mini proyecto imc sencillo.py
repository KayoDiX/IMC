x = int(input("Coloca tu estatura en cm:"))

y = int(input("Coloca tu peso en kg:"))

z = int(input("Coloca tu edad:"))

a = input("Coloca tu sexo (H/M):")

imc = y / (x/100)**2

print("Tu IMC es:", round(imc, 2))

if imc < 18.5:
    print("Por lo que estás: Bajo de peso")
elif 18.5 <= imc < 24.9:
    print("Por lo que estás: Normal")     
elif 25 <= imc < 29.9:
    print("Por lo que estás en: Sobrepeso")      
elif 30 <= imc < 34.9:
    print("Por lo que tienes: Obesidad grado 1")
elif 35 <= imc < 39.9:
    print("Por lo que tienes: Obesidad grado 2")
elif imc >= 40:
    print("Por lo que tienes: Obesidad grado 3")

# made by KayoDiX