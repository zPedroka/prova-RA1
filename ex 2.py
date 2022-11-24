peso = float(input("Qual é seu peso?"))
altura= float(input("qual é sua altura?"))
IMC= peso/(altura**2)

if IMC < 16:
    print("Magreza grave")
elif IMC < 17:
    print("Magreza moderada")
elif IMC < 18.5:
    print("Magreza leve")
elif IMC < 25:
    print ("Saudavel")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 35:
    print("Oesidade grau 1")
elif IMC < 40:
    print ("Obesidade grau 2")
elif IMC >= 40:
    print ("Obesidade grau 2")
