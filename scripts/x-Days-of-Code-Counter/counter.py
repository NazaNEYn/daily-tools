class CounterUp:

    def __init__(self, num_up):
        self.num_up = num_up

    def count_up(self, user_max_day):
        self.num_up += 1

        if self.num_up == 1:
            print(f"{self.num_up} day down!")
        else:
            print(f"{self.num_up} days down!")

        if self.num_up == user_max_day:
            print("You've reached your goal! Great job! 🎉")
            return False
        else:
            return True


class CounterDown:

    def __init__(self, num_down):
        self.num_down = num_down

    def count_down(self):
        self.num_down -= 1

        if self.num_down == 0:
            return False
        else:
            print(f"{self.num_down} more to go!")
            return True
