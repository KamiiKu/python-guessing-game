def guess_game(x, original_time):
    print(f"\n\nHello! Welcome to guessing game! Enter any number you want to be guessed :)"
          f"Computer has only {original_time} attempts to guess")

    # temporary manual input for testing instead of random number
    secret_number = int(input(f"Enter any number from 1 to {x}: "))

    user_feedback = ' ' #stores user's feedback: 'h','l' or 'c'
    bottom = 1 #minimum number
    top = x # maximum number
    attempts_left = original_time
    if secret_number < 1 or secret_number > x: #check if in the range
        print("Incorrect choice! Start again")
        return


    computer_guess = 0
    while True:
        #check if range is > 1 number
        if bottom < top:
            computer_guess = (bottom+top)//2
        elif bottom > top: #checking for logical error
            print("Logic is broken, let's restart.")
            break
        else:
            computer_guess = bottom

        #asking user if correct
        while True:
            user_feedback = input(f"{attempts_left})Is {computer_guess} correct?\nType 'H' if too high, 'L' if too low, and 'C' if correct: ").lower()
            if user_feedback not in ['h','l','c']:
                print("Invalid input! Try again")
            else:
                break
        attempts_used = original_time - attempts_left
        # breaking the loop if correct
        if user_feedback == 'c':
            print(f"Your number is {computer_guess}, computer guessed it in {attempts_used} attempts!!!")
            break
        #breaking the loop if exceed the attempts
        if attempts_left == 0:
            print("Oops, computer couldn't guess your number :<")
            break
        #reducing TTl
        attempts_left -= 1
        #calculations
        if user_feedback == 'h':
            top = computer_guess - 1
        elif user_feedback == 'l':
            bottom = computer_guess + 1

x = int(input("Enter maximum number: "))
original_time = int(input("Enter number of attempts computer can make: "))
guess_game(x, original_time)