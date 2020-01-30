import hw2_ttt
import hw2_ec1_connect4

gamemenu = """
--------MENU--------\n
[1] Tic tac toe\n
[2] Connect four\n
--------------------
"""

def display_menu(menu = gamemenu):
    print(menu)

def main():
# Whether play a game
    while True:
        print()
        ans = input(f"Do you want to play a game?\nEnter yes or no: ")
        if ans.lower() == "yes":
            display_menu()
            while True:
                num = input("Enter the game number: ")
                try:
                    if int(num) == 1:
                        hw2_ttt.main()
                        break
                    elif int(num) == 2:
                        hw2_ec1_connect4.main()
                        break
                    else:
                        print("Your input is not valid.\nPlease enter the game number")
                except IndexError:
                    print("Your input is not valid.\nPlease enter the game number")

        elif ans.lower() == "no":
            print()
            print("Bye bye!")
            break
        else:
            print("Your input is not valid.\nPlease enter yes or no.")

    
if __name__ == "__main__":
    main()    