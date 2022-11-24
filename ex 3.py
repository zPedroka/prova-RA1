par= 0
impar= 0
contador= 0
lista= []
while contador < 10:
    numero= int(input("Qual é seu numero?"))
    lista.append(numero)
    if numero %2==0:
        par += 1
    else:
        impar+= 1
    
    

    contador+=1
print( f"são {par} numeros pares e {impar} números impares")
print(f"o maior numero é {max(lista)}")
print(f"o menor numero é {min(lista)}")
