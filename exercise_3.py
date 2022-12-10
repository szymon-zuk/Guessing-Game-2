print("""
Pick a random number in range 1 to 1000 and I will guess it in max. 10 attempts.
Your allowed answers are: 
- Too big
- Too small
- You win """)



def guessing_game():
    """
    This function is an algorhythm which uses users answers to find a number in range (1, 1000) imagined
    by the user.
    :param: string
    """
    min = 0
    max = 1000
    guess = int((max - min) / 2) + min
    print(f"My guess is: {guess}")

    allowed_answers = ["Too big", "Too small", "You win"]
    feedback = input("Is it the right number: ")
    i = 0
    while i < 10:
        if feedback not in allowed_answers:
            print("Your feedback is wrong!")
            feedback = input("Is it the right number: ")
        elif feedback == "You win":
            print("I won!")
            break
        elif feedback == "Too big":
            max = guess
            guess = int((max - min) / 2) + min
            print(f"My guess is: {guess}")
            feedback = input("Is it the right number: ")
            i += 1
        elif feedback == "Too small":
            min = guess
            guess = int((max - min) / 2) + min
            print(f"My guess is: {guess}")
            feedback = input("Is it the right number: ")
            i += 1
        if i == 10 and feedback != allowed_answers[2]:
            print("Dont cheat!")
            print(f"My guess is: {guess}")
            i += 1


if __name__ == '__main__':
    guessing_game()
