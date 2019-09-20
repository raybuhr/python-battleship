from lib.player import Player
from lib.grid import Grid

def print_guesses(guesses):
    top = [[str(i) for i in range(10)]]
    to_print = top + guesses
    for i, row in enumerate(to_print):
        if i == 0:
            left = " "
        else:
            left = i - 1
        print(left, row)


if __name__ == "__main__":
    player = Player()
    player_name = input("Hello! What is your name? ")
    player.set_name(player_name)
    print(f"Welcome {player.name} to this new game!")
    print("To stop playing, type quit")
    player.grid.add_ships()
    guesses = [[" " for i in range(10)] for j in range(10)]

    while player.in_game:
        guess, hit = player.grid.fire_torpedo()
        row, col = guess
        guesses[row][col] = hit
        print("*" * 10, "Enemy Turn", "*" * 10)
        player.grid.receive_fire()
        player.grid.print_grid()
        print(f"You have {player.grid.player_health} hits left.")
        see_guesses = input("Would you like to see your previous guesses? (y/n)\n")
        if see_guesses.lower()[0] != "n":
            print_guesses(guesses)
        # see_computer_grid = input("Would you like to see the computer's board?\n")
        # if see_computer_grid == "y":
        #     for row in player.grid.computer_grid:
        #         print(row)
