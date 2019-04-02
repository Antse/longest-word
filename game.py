import string
import random


class Game():

    def __init__(self):
        alphabet = string.ascii_uppercase
        self.grid = []

        for _ in range(9):
            random.randint(0, 25)
            indice = random.randint(0, 25)
            self.grid.append(alphabet[indice])

    def is_valid(self, word):
        temp_grid = self.grid

        for letter in word:
            if letter in temp_grid:
                temp_grid.remove(letter)
            else:
                return False
        if word == "":
            return False
        if set(word) != set(self.grid):
            return False
        else:
            return True
