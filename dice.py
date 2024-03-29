import random

class Dice:
    def __init__(self, quantity, sides):
        self.dices = quantity
        self.sides = sides
        self.last_roll = []
    
    def __str__(self):
        return f'Dices: {self.dices}   Sides: {self.sides}   Last Roll: {self.last_roll}'

    def __repr__(self):
        data = ''
        for x, i in enumerate(self.last_roll):
            if x == len(self.last_roll)-1:
                data += f'{i}'
            else:
                data += f'{i}, '
        return data

    def roll(self):
        rolls = []

        for i in range(self.dices):
            rolls.append(random.randrange(1,self.sides+1))
        
        self.last_roll = rolls
        return rolls

    def roll_index(self, index):
        if index > self.dices:
            print(f'ERR: Not enough dices')
            return -1
        
        if len(self.last_roll) == 0:
            print(f'ERR: No Roll establish, call roll() first')  
            return -2

        self.last_roll[index] = random.randrange(1, self.sides+1)

    def roll_total(self):
        if len(self.last_roll) == 0:
            print(f'ERR: No Roll establish, call roll() first')
            return -2
        
        return sum(self.last_roll)

    def roll_unique(self):
        rolls = []

        if self.dices > self.sides:
            print(f'ERR: Number of Dices is more than Sides, cant create unique rolls')
            return -3

        for i in range(self.dices):
            roll = random.randrange(1, self.sides+1)

            while True:
                if roll not in rolls:
                    rolls.append(roll)
                    break
                else:
                    roll = random.randrange(1, self.sides+1)

        self.last_roll = rolls
        return rolls


if __name__ == '__main__':
    print('Dice Application')
    
    game = Dice(2,20)
    print(game)

    game.roll_index(3)
    print(f'last roll: {game.last_roll}')

    for i in range(10):
        print(f'{i} - {game.roll()}')
    
    print(f'last roll: {game.last_roll}')

    game.roll_index(7)
    print(f'last roll: {game.last_roll}')

    print(f'total roll {game.last_roll} -- {game.roll_total()}')

    game2 = Dice(12, 12)
    print(game2)

    print(f'last roll: {game2.roll_unique()}')
    