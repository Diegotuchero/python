import os
os.system ("cls")

angulo = int(input("clasificación de los angulos segun sus medidas: "))

if angulo == 0:
    print("angulo nulo")
elif angulo > 0 and angulo < 90:
    print("Este ángulo, al tener medir ", " en grados, se clasifica como agudo.")
elif angulo == 90:
    print("Este ángulo, al tener medir ", " en grados, se clasifica como recto.")
elif angulo > 90 and angulo < 180:
    print("Este ángulo, al tener medir ", " en grados, se clasifica como obtusp.")
elif angulo == 180:
    print("Este ángulo, al tener medir ", " en grados, se clasifica como llano.")
elif angulo > 180 and angulo < 360:
    print("Este ángulo, al tener medir ", " en grados, se clasifica como cóncavo.")
elif angulo == 360:
    print("angulo completo")
