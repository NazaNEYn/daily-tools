import time
import os
from functions import generate_hourglass

<<<<<<< HEAD

if __name__ == "__main__":
    while True:
        try:
            user_max_day = int(input("How many days of code are you doing?\n"))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"Awesome! You're committed to a {user_max_day}-day challenge.")
    print("----------------------------------------")
    print("\n")

    counter_up = CounterUp(0)

    counter_down = CounterDown(user_max_day)

    is_counting = True
    while is_counting:
        user_input = input("Press ENTER to count!\n")

        if user_input == "":
            up_result = counter_up.count_up(user_max_day)
            down_result = counter_down.count_down()

            is_counting = up_result and down_result

            display_hourglass(counter_up.num_up, user_max_day)
            print(f"#{user_max_day}DaysOfCode")
        else:
            print("Invalid input. Try Again!")
=======
if __name__ == "__main__":
    try:
        num = int(input("Number of days of code (0-100): "))
        if num < 0 or num > 100:
            print("Number must be between 0 and 100.")
        else:
            bottom_grains = (num * 14) // 100
            for i in range(bottom_grains + 1):
                os.system("clear")
                current_top = 33 - (i * 33 // 14) if bottom_grains > 0 else 33
                print(generate_hourglass(current_top, i))
                time.sleep(0.5)
            print(f"\nDays of Code: {num}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

>>>>>>> 989cad87bf2a4395762b5582f56083db170311ac
