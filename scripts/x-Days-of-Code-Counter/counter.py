class CounterUp:
    """Class to handle counting up the days completed."""

    def __init__(self, num_up):
        """Initialize with the starting number of days completed."""
        self.num_up = num_up

    def count_up(self, user_max_day):
        """Increment the count and print progress message."""
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
    """Class to handle counting down the remaining days."""

    def __init__(self, num_down):
        """Initialize with the total number of days remaining."""
        self.num_down = num_down

    def count_down(self):
        """Decrement the count and print remaining days."""
        self.num_down -= 1

        if self.num_down == 0:
            return False
        else:
            print(f"{self.num_down} more to go!")
            return True
