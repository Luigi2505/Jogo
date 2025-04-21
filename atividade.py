import random

print("Vamos jogar pedra papel e tesoura? ")
nome = input("Qual é o seu nome?: ")
print(f"Olá, {nome}! Vamos jogar?")

escolha = input("Escolha o modo de jogo: \n1 - Jogador vs Computador \n2 - Jogador vs Jogador \n3 - Computador vs Computador \n4 - Sair \nDigite seu modo: ")
time_jogador = 0
time_computador = 0

if escolha == "1":
    print("Você escolheu Jogador vs Computador")
while escolha == "1":
    jogador = input("Escolha entre pedra, papel ou tesoura: ").lower()
    comp = random.choice(["pedra", "papel", "tesoura"])
    print(f"Computador escolheu: {comp}")

    if jogador == comp:
        print("Empate")
        time_jogador += 0
        time_computador += 0

    elif jogador == "pedra" and comp == "tesoura":
        print("Você ganhou!")
        time_jogador += 1

    elif jogador == "pedra" and comp == "papel":
        print("Você perdeu!")
        time_computador += 1

    elif jogador == "tesoura" and comp == "papel":
        print("Você ganhou!")
        time_jogador += 1

    elif jogador == "tesoura" and comp == "pedra":
        print("Você perdeu!")
        time_computador += 1

    elif jogador == "papel" and comp == "pedra":
        print("Você ganhou!")
        time_jogador += 1

    elif jogador == "papel" and comp == "tesoura":
        print("Você perdeu!")
        time_computador += 1

    print(f"---PLACAR--- \n{nome}: {time_jogador} \nComputador: {time_computador}")
    escolha = input("Digite 1 se deseja continuar e 4 se deseja sair: ")

time_jogador1 = 0
time_jogador2 = 0
if escolha == '2':
    print("Você escolheu Jogador vs Jogador")
    nome_jogador2 = input("Insira o nome do jogador 2: ")

while escolha == '2':
    jogador1 = input(f"{nome}, escolha entre pedra, papel, tesoura: ").lower()
    jogador2 = input(f"{nome_jogador2}, escolha entre pedra, papel, tesoura: ").lower()

    if jogador1 == jogador2:
        print("Empate")
        time_jogador1 += 0
        time_jogador2 += 0

    elif jogador1 == "pedra" and jogador2 == "tesoura":
        print(f"{nome} ganhou!")
        time_jogador1 +=1

    elif jogador1 == "pedra" and jogador2 == "papel":
        print(f"{nome_jogador2} ganhou!")
        time_jogador2 += 1

    elif jogador1 == "papel" and jogador2 == "tesoura":
        print(f"{nome_jogador2} ganhou!")
        time_jogador2 += 1

    elif jogador1 == "papel" and jogador2 == "pedra":
        print(f"{nome} ganhou!")
        time_jogador1 += 1

    elif jogador1 == "tesoura" and jogador2 == "papel":
        print(f"{nome} ganhou!")
        time_jogador1 += 1

    elif jogador1 == "tesoura" and jogador2 == "pedra":
        print(f"{nome_jogador2} ganhou!")
        time_jogador2 += 1

    print(f"---PLACAR--- \n{nome}: {time_jogador1} \n{nome_jogador2}: {time_jogador2}")
    escolha = input("Digite 2 se deseja continuar e 4 se deseja sair: ")

time_comp1 = 0
time_comp2 = 0
while escolha == '3':
    print("Você escolheu Computador vs Computador! ")

    comp1 = random.choice (["pedra", "papel", "tesoura"])
    print(f"Escolha do computador 1: {comp1}")
    comp2 = random.choice (["pedra", "papel", "tesoura"])
    print(f"Escolha do computador 2: {comp2}")

    if comp1 == comp2:
        print("Empate")
        time_comp1 += 0
        time_comp2 += 0

    elif comp1 == "pedra" and comp2 == "tesoura":
        print("Computador 1 ganhou!")
        time_comp1 += 1

    elif comp1 == "pedra" and comp2 == "papel":
        print("Computador 2 ganhou!")
        time_comp2 += 1

    elif comp1 == "papel" and comp2 == "tesoura":
        print("Computador 2 ganhou!")
        time_comp2 += 1

    elif comp1 == "papel" and comp2 == "pedra":
        print("Computador 1 ganhou!")
        time_comp1 += 1

    elif comp1 == "tesoura" and comp2 == "papel":
        print("Computador 1 ganhou!")
        time_comp1 += 1

    elif comp1 == "tesoura" and comp2 == "pedra":
        print("Computador 2 ganhou!")
        time_comp2 += 1

    print(f"---PLACAR--- \nComputador 1: {time_comp1} \nComputador 2: {time_comp2}")
    escolha = input("Digite 3 se deseja continuar e 4 se deseja sair: ")

if escolha == "4":
    print("Você escolheu sair, até a próxima!")
else:
    print("Insira um número válido!")


    
