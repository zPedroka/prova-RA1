nome= str(input("Qual é seu nome"))
mes= str(input("Que mês você nasceu?"))
ano= int(input("Que ano você nasceu?"))

if mes!=('janeiro', 'fevereiro', 'março', 'abril', 'maio') and ano > 2005:
    print ("Você não poderá realizar a inscrição")

else:
    print("Parabéns, você poderá realizar a inscrição")
