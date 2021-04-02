import numpy as np

WINDOW_SIZE = 50

class Fruit:
    def __init__(self, body_of_snake):
        self.place_fruit(body_of_snake=body_of_snake)
    
    def place_fruit(self, coord=None, body_of_snake=None):
        if coord:
            self.corrd = coord
            return

        while True:
            x = np.random.randint(WINDOW_SIZE - 1)
            y = np.random.randint(WINDOW_SIZE - 1)
            if list([x, y]) not in body_of_snake.tolist():
                self.coord = np.array([x, y])
                return
                
