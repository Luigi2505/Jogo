import random
print("Vamos jogar pedra papel e tesoura? ")
nome = input("Qual é o seu nome? ")
print(f"Olá {nome}! Vamos jogar?")
escolha = input("Escolha o modo de jogo: \n1 - jogar contra computador \n2 - jogar contra jogador \n3 - computador contra computador \n4 - sair \nDigite seu modo: ")
if escolha == "1":
    print("Você escolheu jogador contra computador")
    time_jogador = 0
    time_computador = 0
    while escolha == "1":
        contador_rodadas = 0
        soma = 0
        jogador = input("Escolha entre pedra, papel ou tesoura: ")
        comp = random.choice(["pedra", "papel", "tesoura"])
        print(f"Computador escolheu: {comp}")
        if jogador == comp:
            print("empate")
        elif jogador == "pedra" and comp == "tesoura":
            print("Você ganhou!")
            time_jogador += 1
            print(f"o Placar está Jogador: {time_jogador} \nComputador: {time_computador}")
        elif jogador == "pedra" and comp == "papel":
            print("Você perdeu!")
            time_computador += 1
            print(f"o Placar está Jogador: {time_jogador} \nComputador:{time_computador}")
        elif jogador == "tesoura" and comp == "papel":
            print("Você ganhou!")
            time_jogador += 1
            print(f"o Placar está Jogador: {time_jogador} \nComputador:{time_computador}")
        elif jogador == "tesoura" and comp == "pedra":
            print("Você perdeu!")
            time_computador += 1
            print(f"o Placar está Jogador: {time_jogador} \nComputador:{time_computador}")
        elif jogador == "papel" and comp == "pedra":
            print("Você ganhou!")
            time_jogador += 1
            print(f"o Placar está Jogador: {time_jogador} \nComputador:{time_computador}")
        elif jogador == "papel" and comp == "tesoura":
            print("Você perdeu!")
            time_computador += 1
            print(f"o Placar está Jogador: {time_jogador} \nComputador:{time_computador}")
        break
elif escolha == '2':
    print("Você escolheu jogador contra jogador")
    jogador1 = input("Jogador 1, escolha entre pedra, papel, tesoura: ")
    jogador2 = input("Jogador 2, escolha entre pedra, papel, tesoura: ")
    if jogador1 == jogador2:
        print("Empate")
    elif jogador1 == "pedra" and jogador2 == "tesoura":
        print("Jogador 1 ganhou!")
    elif jogador1 == "pedra" and jogador2 == "papel":
        print("Jogador 2 ganhou!")
    elif jogador1 == "papel" and jogador2 == "tesoura":
        print("Jogador 2 ganhou!")
    elif jogador1 == "papel" and jogador2 == "pedra":
        print("Jogador 2 ganhou!")
    elif jogador1 == "tesoura" and jogador2 == "papel":
        print("Jogador 1 ganhou!")
    elif jogador1 == "tesoura" and jogador2 == "pedra":
        print("Jogador 2 ganhou!")
elif escolha == '3':
    print("Você escolheu computador contra computador! ")
    comp1 = random.choice (["pedra", "papel", "tesoura"])
    print(f"escolha do computador 1: {comp1}")
    comp2 = random.choice (["pedra", "papel", "tesoura"])    
    print(f"escolha do computador 2: {comp2}")
    if comp1 == comp2:
        print("Empate")
    elif comp1 == "pedra" and comp2 == "tesoura":
        print("computador 1 ganhou!")
    elif comp1 == "pedra" and comp2 == "papel":
        print("computador 2 ganhou!")
    elif comp1 == "papel" and comp2 == "tesoura":
        print("Computador 2 ganhou!")
    elif comp1 == "papel" and comp2 == "pedra":
        print("Computador 1 ganhou!")
    elif comp1 == "tesoura" and comp2 == "papel":
        print("computador 1 ganhou!")
    elif comp1 == "tesoura" and comp2 == "pedra":
        print("computador 2 ganhou!")

    
