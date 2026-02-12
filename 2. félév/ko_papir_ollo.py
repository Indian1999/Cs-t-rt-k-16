import random

def rock_paper_scissors(player = True):
    if player:
        player_choice = int(input("Kő(1), papír(2) vagy olló(3)?\n"))
    else:
        player_choice = random.randint(1, 3)
    comp_choice = random.randint(1, 3)
    winner = -1    # 1 - player nyert, 0 - döntetlen -1 - szg. nyert
    if (player_choice == 1 and comp_choice == 3) or (player_choice == 2 and comp_choice == 1) or (player_choice == 3 and comp_choice == 2):
        winner = 1
    elif player_choice == comp_choice:
        winner = 0
    return winner

wins = 0
losses = 0
ties = 0
for i in range(1000):
    result = rock_paper_scissors(False)
    if result == 1:
        wins +=1
        print("Nyerél!")
    if result == 0:
        ties += 1
        print("Döntetlen!")
    if result == -1:
        losses += 1
        print("Vesztettél!")

print(f"Győzelmek: {wins}\nDöntetlenek: {ties}\nVereségek: {losses}")

import matplotlib.pyplot as plt # pip install matplotlib

def show_results_barplot():
    plt.bar(["Győzelmek", "Döntetlenek", "Vereségek"], [wins, ties, losses])
    plt.xlabel("Kimenetel")
    plt.ylabel("Gyakoriság")
    plt.title("A kő papír olló bajnokság eredményei")
    plt.ylim((300, 370))
    plt.show()

show_results_barplot()