import random

vidaJogador=200
vidaInimigo=200
curaJogador=0
curaInimigo=0


while vidaJogador>=1 and vidaInimigo>=1:
    acao=int(input("Digite 1 para atacar: \nDigite 2 para curar: "))
    if acao==1:
        print("=-"*30)
        print("Sua vez, você atacou")
        danoJogador=random.randint(50, 100)
        if danoJogador>=75:
            print("Você deu DANO CRÍTICO")
    elif acao==2:
        curaJogador=random.randint(30, 50)
        print("=-"*30)
        print("Sua vez, você curou ")
        print(f"Você curou {curaJogador}")
    acaoInimigo=random.randint(1, 2)
    if acaoInimigo==1:
        danoInimigo=random.randint(50, 100)
        print("=-"*30)
        print("Vez do inimigo, ele atacou")
        if danoInimigo>=75:
            print("DANO CRÍTICO do Inimigo")
    elif acao==2:
        curaInimigo=random.randint(30, 50)
        print("=-"*30)
        print("Vez do Inimigo, ele curou")
        print(f"O Inimigo curou{curaInimigo}")
    vidaJogador=vidaJogador+curaJogador
    vidaInimigo=vidaInimigo+curaInimigo
    vidaJogador=vidaJogador-danoInimigo
    vidaInimigo=vidaInimigo-danoJogador
    print(f"Sua vida atual é {vidaJogador}")
    print(f"A vida atual de seu Inimigo é {vidaInimigo}")

if vidaJogador>vidaInimigo:
    print("Parabens, você venceu")
else:
    print("Sinto muito, você foi solado")