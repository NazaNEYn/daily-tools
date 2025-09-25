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
