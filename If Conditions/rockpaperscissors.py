import random
computerChoice = random.randint(1 , 3)

rock = 1
paper = 2
scissors = 3
wins = None
choices= {1: "rock", 2: "paper", 3: "scissors"}

print("1 : Rock" + "\n" + "2 : Paper" + "\n" + "3 : Scissors")
player_one = input("Enter your choice player one\n ")
player_two = computerChoice

if player_one and player_two:
    player_one = int(player_one)
    player_two = int(player_two)
    if player_one > 0 and player_two <= 3:
        if player_one == rock and player_two == scissors:
            print("Player One Wins as Rock beats scissors")
        elif player_one == paper and player_two == rock:
            print("Player One Wins as Paper beats Rock")
        elif player_one == scissors and player_two == paper:
            print("Player one Wins as scissors beats paper ")
        elif player_one == rock and player_two == rock:
            print("It's a draw")
        elif player_one == paper and player_two == paper:
            print("It's a Draw!")
        elif player_one == scissors and player_two == scissors:
            print("It's a draw!")
        else:
                print(f"Computer wins as {choices[player_two]} beats {choices[player_one]}")
    else:
        "Not valid in the menu"
else:
    print("That's not a valid choice")
