import os 
os.system ("cls")

numero = int(input("ingrese un numero de 4 cifras: "))

cifra_1 = int(numero/1000)
cifra_2 = int((numero%1000)/100)
cifra_3 = int(((numero%1000)%100)/10)
cifra_4 = numero%10

print("la suma de los digitos es",cifra_1 + cifra_2 + cifra_3 + cifra_4)