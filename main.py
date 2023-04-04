secret_number = 7
guess_counter = 0
guess_limit = 3
player_name = input("Enter player name: ")
print("*******************************")
print("*                             *")
print(f"*       welcome,{player_name[0].upper()}{player_name[1:]}!")
print("*                             *")
print("*******************************")
while guess_counter < guess_limit:
    guessed_number = int(input("Guess a secret number: "))
    guess_counter += 1
    if guessed_number == secret_number:
        print("*********************")
        print("*                   *")
        print("* Congratulations!  *")
        print("*     YOU WON!      *")
        print("*                   *")
        print("*********************")
        break
else:
    print("*********************")
    print("*                   *")
    print("*     GAME OVER     *")
    print("*                   *")
    print("*********************")
    print("Too many Attempts. You failed!")