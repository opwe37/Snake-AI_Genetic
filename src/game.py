import pygame
from fruit import Fruit
from snake import Snake

WINDOW_SIZE = 50

class Game:
    def __init__(self, snake=Snake()):
        self.snake = snake
        self.fruit = Fruit(body_of_snake=self.snake.body)
    
    def run(self):
        pygame.init()
        s = pygame.display.set_mode((WINDOW_SIZE * 10, WINDOW_SIZE * 10))
        #pygame.display.set_caption('Snake')
        appleimage = pygame.Surface((10, 10))
        appleimage.fill((0, 255, 0))
        img = pygame.Surface((10, 10))
        img.fill((255, 0, 0))
        clock = pygame.time.Clock()

        while True:
            pressed_key = self.snake.direction
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()

                if e.type == pygame.KEYDOWN:
                    if self.snake.direction != 2 and e.key == pygame.K_UP:
                        pressed_key = 0
                    elif self.snake.direction != 0 and e.key == pygame.K_DOWN:
                        pressed_key = 2
                    elif self.snake.direction != 1 and e.key == pygame.K_LEFT:
                        pressed_key = 3
                    elif self.snake.direction != 4 and e.key == pygame.K_RIGHT:
                        pressed_key = 1

            if not self.snake.move(pressed_key, self.fruit):
                break

            s.fill((255, 255, 255))
            for bit in self.snake.body:
                s.blit(img, (bit[0] * 10, (WINDOW_SIZE - bit[1] - 1) * 10))
            s.blit(appleimage, (self.fruit.coord[0] * 10, (WINDOW_SIZE - self.fruit.coord[1]-1) * 10))
            clock.tick(240)
            pygame.display.flip()
        
        return self.snake.fitness, self.snake.score

if __name__ == '__main__':
    f, s = Game().run()
    print(f'fitness: {f}, score: {s}')
