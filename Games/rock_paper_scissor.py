from termcolor import colored


comps_play = ["ROCK", "PAPER", "SCISSOR"]



def instruct(instructions):
    print("There are only three choices in the game :-")
    for i in instructions:
        print(i)
    print("\nYou have to select one value out of the there every time its your turn")
    print("\nSpecific instructions")
    print("\n---------------------------------")

    print("\tROCK vs SCISSOR    ---->  ROCK WINS")
    print("\tROCK vs PAPER      ---->  PAPER WINS")
    print("\tROCK vs ROCK       ---->  it's a TIE")

    print("\n---------------------------------")

    print("\tPAPER vs ROCK      ---->  PAPER WINS")
    print("\tPAPER vs SCISSOR   ---->  SCISSOR WINS")
    print("\tPAPER va PAPER     ---->  it's a TIE")

    print("\n---------------------------------")

    print("\tSCISSOR vs ROCK    ---->   ROCK WINS")
    print("\tSCISSOR vs PAPER   ---->   SCISSOR WINS")
    print("\tSCISSOR vs SCISSOR ---->  it's a TIE")
    print("\n\n\t\t LETS START!")


instruct(comps_play)

print("\n\n\t\tI play first :P...")

print(comps_play[0])
s1 = input("\n your turn ")

if s1 == comps_play[0]:
    print("Its a TIE")
elif s1 == comps_play[1]:
    print(colored("YOU WIN!!!!..", 'green', attrs=['bold']))
elif s1 == comps_play[2]:
    print(colored("Nooooo!.. YOU LOST", 'red', attrs=['bold']))


