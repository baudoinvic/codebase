
import random

# here is the Function i used to display start message
def start_message():
    print("Welcome to Rock-Paper-Scissors Game!")

# then here is the Function to get player's choice
def get_player():
    while True:
        try:
            player_choice = int(input("Input your hand\n0: rock, 1: scissors, 2: paper: "))
            if is_hand(player_choice):
                return player_choice
            else:
                print("Invalid input. Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#  here is the Function to get computer's choice
def get_computer():
    return random.randint(0, 2)

# here is the Function to map hand number to hand name
def get_hand_name(hand_number):
    hands = ['rock', 'scissors', 'paper']
    return hands[hand_number]

# here is the  Function to display hands
def view_hand(player, computer):
    print(f"My hand is {get_hand_name(player)}")
    print(f"Rival's hand is {get_hand_name(computer)}")

# here is the  Function to determine the result
 
 
def get_result(hand_diff):
    if hand_diff == 0:
        return 'draw'
    elif hand_diff == -1 or hand_diff == 2:
        return 'win'
    else:
        return 'lose'

def view_result(result):
    print(result)



# here is the Function to validate hand choice
def is_hand(number):
    return number in [0, 1, 2]

# and this one is Main game loop
def main():
    start_message()

    while True:
        print("Start 'rock-paper-scissors'")
        player_choice = get_player()
        computer_choice = get_computer()
        view_hand(player_choice, computer_choice)

        result = get_result(player_choice, computer_choice)
        print(result)

        if result != 'draw':
            break

if __name__ == "__main__":
    main()
