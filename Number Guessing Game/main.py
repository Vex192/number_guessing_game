import random
from scipy import stats

counter_win = 0
counter_loss = 0
total_games = 0
all_guesses = []

try:
    while True:
        print("Welcome to the Python Random Number Guessing Game.\n\n")

        start_easy = 1
        end_easy = 5
        start_medium = 1
        end_medium = 10
        start_hard = 1
        end_hard = 20

        random_number_easy = random.randint(start_easy, end_easy)
        random_number_medium = random.randint(start_medium, end_medium)
        random_number_hard = random.randint(start_hard, end_hard)

        difficulty = input("Please select the level difficulty. Enter e for easy, m for medium, and h for hard: ").strip().lower()

        lives_easy = 3
        lives_medium = 4
        lives_hard = 5

        number_of_guess_hard = 0
        number_of_guess_medium = 0
        number_of_guess_easy = 0

        won = False

        total_games += 1

        while True:

            if difficulty == "e":

                user_guess_easy = int(input("Level Difficulty: Easy || Please enter a integer from 1-5: "))
                all_guesses.append(user_guess_easy)

                if user_guess_easy == random_number_easy:
                    number_of_guess_easy += 1
                    print("Congrats you guessed the number. You Won easy level!!\n\n")
                    counter_win += 1
                    won = True
                    break

                elif user_guess_easy > random_number_easy:
                    counter_loss += 1
                    lives_easy -= 1
                    print("Your number is greater than the correct number.\n\n")
                    print(f"You lost a life. You now have {lives_easy} lives remaining.\n\n")

                else:
                    counter_loss += 1
                    lives_easy -= 1
                    print("Your number is less than the correct number.\n\n")
                    print(f"You lost a life. You now have {lives_easy} lives remaining.\n\n")

                if lives_easy == 0:
                    print(f"You lost. The correct answer was {random_number_easy}.\n\n")
                    won = False
                    break


            elif difficulty == "m":

                user_guess_medium = int(input("Level Difficulty: Medium || Please enter a integer from 1-10: "))
                all_guesses.append(user_guess_medium)

                if user_guess_medium == random_number_medium:
                    number_of_guess_medium += 1
                    print("Congrats you guessed the number. You Won medium level!!\n\n")
                    counter_win += 1
                    won = True
                    break

                elif user_guess_medium > random_number_medium:
                    counter_loss += 1
                    lives_medium -= 1
                    print("Your number is greater than the correct number.\n\n")
                    print(f"You lost a life. You now have {lives_medium} lives remaining.\n\n")

                else:
                    counter_loss += 1
                    lives_medium -= 1
                    print("Your number is less than the correct number.\n\n")
                    print(f"You lost a life. You now have {lives_medium} lives remaining.\n\n")

                if lives_medium == 0:
                    print(f"You lost. The correct answer was {random_number_medium}.\n\n")
                    won = False
                    break


            elif difficulty == "h":

                user_guess_hard = int(input("Level Difficulty: Hard || Please enter a integer from 1-20: "))
                all_guesses.append(user_guess_hard)

                if user_guess_hard == random_number_hard:
                    number_of_guess_hard += 1
                    print("Congrats you guessed the number. You Won hard level!!\n\n")
                    counter_win += 1
                    won = True
                    break

                elif user_guess_hard > random_number_hard:
                    counter_loss += 1
                    lives_hard -= 1
                    print("Your number is greater than the correct number.\n\n")
                    print(f"You lost a life. You now have {lives_hard} lives remaining.\n\n")

                else:
                    counter_loss += 1
                    lives_hard -= 1
                    print("Your number is less than the correct number.\n\n")
                    print(f"You lost a life. You now have {lives_hard} lives remaining.\n\n")

                if lives_hard == 0:
                    print(f"You lost. The correct answer was {random_number_hard}.\n\n")
                    won = False
                    break

            else:
                print("Please enter e for easy m for medium and h for hard, not something else. Press run to try again.")
                break

        if True:
            continue_or_quit = input("Would you like to continue or quit? Enter c to continue or q to quit: ").strip().lower()
            
            if continue_or_quit == "c":
                continue
            elif continue_or_quit == "q":
                break
            else:
                print("Please enter c to continue and q to quit, not something else. Press run to try again.")
                break

    print("\n===== Game Statistics =====")
    print(f"Total Games Played: {total_games}")
    print(f"Wins: {counter_win}")
    print(f"Losses: {counter_loss}")

    if total_games > 0:
        winrate = (counter_win / total_games) * 100
        print(f"Winning Percentage: {winrate:.2f}%")

    print(f"All Guesses: {all_guesses}")

    if len(all_guesses) > 0:
        most_guessed_number = stats.mode(all_guesses)
        print(f"Most Guessed Number: {int(most_guessed_number.mode)}")

except ValueError:
    print("ERROR!! Wrong Input!! Please enter an integer.")
