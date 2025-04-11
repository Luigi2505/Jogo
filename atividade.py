import random

print("Vamos jogar pedra papel e tesoura? ")
nome = input("Qual é o seu nome?: ")
print(f"Olá, {nome}! Vamos jogar?")

escolha = "0"

while escolha in ["0", "1", "2", "3", "5"]:
    escolha = input("Escolha o modo de jogo: \n1 - Jogador vs Computador \n2 - Jogador vs Jogador \n3 - Computador vs Computador \n4 - Sair \nDigite seu modo: ")

    if escolha == "1":

        print("Você escolheu Jogador vs Computador")
        time_jogador = 0
        time_computador = 0
        while escolha == "1":

            jogador = input("Escolha entre pedra, papel ou tesoura: ").lower()
            comp = random.choice(["pedra", "papel", "tesoura"])
            print(f"Computador escolheu: {comp}")

            if jogador == comp:
                print("Empate")
                print(f"---PLACAR--- \nJogador: {time_jogador} \nComputador: {time_computador}")
                print("Você deseja continuar jogando?")
                escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

            elif jogador == "pedra" and comp == "tesoura":
                print("Você ganhou!")
                time_jogador += 1
                print(f"---PLACAR--- \nJogador: {time_jogador} \nComputador: {time_computador}")
                print("Você deseja continuar jogando?")
                escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

            elif jogador == "pedra" and comp == "papel":
                print("Você perdeu!")
                time_computador += 1
                print(f"---PLACAR--- \nJogador: {time_jogador} \nComputador: {time_computador}")
                print("Você deseja continuar jogando?")
                escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

            elif jogador == "tesoura" and comp == "papel":
                print("Você ganhou!")
                time_jogador += 1
                print(f"---PLACAR--- \nJogador: {time_jogador} \nComputador: {time_computador}")
                print("Você deseja continuar jogando?")
                escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

            elif jogador == "tesoura" and comp == "pedra":
                print("Você perdeu!")
                time_computador += 1
                print(f"---PLACAR--- \nJogador: {time_jogador} \nComputador: {time_computador}")
                print("Você deseja continuar jogando?")
                escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

            elif jogador == "papel" and comp == "pedra":
                print("Você ganhou!")
                time_jogador += 1
                print(f"---PLACAR--- \nJogador: {time_jogador} \nComputador: {time_computador}")
                print("Você deseja continuar jogando?")
                escolha = input("Digite 5 para continuar ou 4 se deseja sair: ")

            elif jogador == "papel" and comp == "tesoura":
                print("Você perdeu!")
                time_computador += 1
                print(f"---PLACAR--- \nJogador: {time_jogador} \nComputador: {time_computador}")
                print("Você deseja continuar jogando?")
                escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")


    elif escolha == '2':

        print("Você escolheu Jogador vs Jogador")
        nome_jogador2 = input("Insira o nome do jogador 2: ")
        jogador1 = input("Jogador 1, escolha entre pedra, papel, tesoura: ").lower()
        jogador2 = input("Jogador 2, escolha entre pedra, papel, tesoura: ").lower()
        time_jogador1 = 0
        time_jogador2 = 0


        if jogador1 == jogador2:
            print("Empate")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif jogador1 == "pedra" and jogador2 == "tesoura":
            print("Jogador 1 ganhou!")
            time_jogador1 +=1
            print(f"---PLACAR--- \n{nome}: {time_jogador1} \n{nome_jogador2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif jogador1 == "pedra" and jogador2 == "papel":
            print("Jogador 2 ganhou!")
            time_jogador2 += 1
            print(f"---PLACAR--- \n{nome}: {time_jogador1} \n{nome_jogador2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif jogador1 == "papel" and jogador2 == "tesoura":
            print("Jogador 2 ganhou!")
            time_jogador2 += 1
            print(f"---PLACAR--- \n{nome}: {time_jogador1} \n{nome_jogador2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif jogador1 == "papel" and jogador2 == "pedra":
            print("Jogador 1 ganhou!")
            time_jogador1 += 1
            print(f"---PLACAR--- \n{nome}: {time_jogador1} \n{nome_jogador2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif jogador1 == "tesoura" and jogador2 == "papel":
            print("Jogador 1 ganhou!")
            time_jogador1 += 1
            print(f"---PLACAR--- \n{nome}: {time_jogador1} \n{nome_jogador2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif jogador1 == "tesoura" and jogador2 == "pedra":
            print("Jogador 2 ganhou!")
            time_jogador2 += 1
            print(f"---PLACAR--- \n{nome}: {time_jogador1} \n{nome_jogador2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

    elif escolha == '3':
        print("Você escolheu Computador vs Computador! ")
        time_comp1 = 0
        time_comp2 = 0

        comp1 = random.choice (["pedra", "papel", "tesoura"])
        print(f"escolha do computador 1: {comp1}")
        comp2 = random.choice (["pedra", "papel", "tesoura"])
        print(f"escolha do computador 2: {comp2}")

        if comp1 == comp2:
            print("Empate")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif comp1 == "pedra" and comp2 == "tesoura":
            print("Computador 1 ganhou!")
            time_comp1 += 1
            print(f"---PLACAR--- \n{time_comp1}: {time_jogador1} \n{time_comp2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif comp1 == "pedra" and comp2 == "papel":
            print("Computador 2 ganhou!")
            time_comp2 += 1
            print(f"---PLACAR--- \n{time_comp1}: {time_jogador1} \n{time_comp2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif comp1 == "papel" and comp2 == "tesoura":
            print("Computador 2 ganhou!")
            time_comp2 += 1
            print(f"---PLACAR--- \n{time_comp1}: {time_jogador1} \n{time_comp2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif comp1 == "papel" and comp2 == "pedra":
            print("Computador 1 ganhou!")
            time_comp1 += 1
            print(f"---PLACAR--- \n{time_comp1}: {time_jogador1} \n{time_comp2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif comp1 == "tesoura" and comp2 == "papel":
            print("Computador 1 ganhou!")
            time_comp1 += 1
            print(f"---PLACAR--- \n{time_comp1}: {time_jogador1} \n{time_comp2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

        elif comp1 == "tesoura" and comp2 == "pedra":
            print("Computador 2 ganhou!")
            time_comp2 += 1
            print(f"---PLACAR--- \n{time_comp1}: {time_jogador1} \n{time_comp2}: {time_jogador2}")
            escolha = input("Digite 5 se deseja continuar e 4 se deseja sair: ")

if escolha == "4":
    print("Você escolheu sair, até a próxima!")
else:
    print("Insira um número válido!")


    
