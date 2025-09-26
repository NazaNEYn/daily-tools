import time
import os
from functions import generate_hourglass

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

