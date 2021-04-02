import numpy as np

WINDOW_SIZE = 50

DIRECTIONS = np.array([
  (0, 1), # UP
  (1, 0), # RIGHT
  (0, -1), # DOWN
  (-1, 0) # LEFT
])

class Snake():
    def __init__(self, brain=None, ai=False):
        self.body = np.array([(24, 2), (24, 1), (24, 0)])
        self.direction = 0
        self.brain = brain
        self.ai = ai
        self.score = 0
        self.fitness = 0
        self.last_closed_dist = float('inf')

        self.total_move = 1
        self.tmp_posivie_move = 0

        self.life_time = 200
    
    def move(self, direction, fruit=None):
        possible_dir = [
            DIRECTIONS[self.direction],             # 현 방향 고수
            DIRECTIONS[(self.direction + 1) % 4],   # 우측 방향
            DIRECTIONS[(self.direction + 3) % 4]    # 좌측 방향
        ]
        if self.ai:
            direction = self.brain.forward(self.observe(fruit.coord))

        old_head = self.body[0]
        movement =  possible_dir[direction] if self.ai else DIRECTIONS[direction]
        new_head = old_head + movement

        if (
            new_head[0] < 0 or 
            new_head[0] > WINDOW_SIZE or
            new_head[1] < 0 or
            new_head[1] > WINDOW_SIZE or
            new_head.tolist() in self.body[:-1, :].tolist()
        ):
            self.fitness += self.tmp_posivie_move / self.total_move
            return False
        
        if np.all(new_head == fruit.coord):
            self.score += 1
            self.life_time += 100
            self.fitness += 10. + (self.tmp_posivie_move / self.total_move)
            self.total_move, self.tmp_posivie_move = 1, 0
            fruit.place_fruit(body_of_snake=self.body)
            self.last_closed_dist = np.linalg.norm(new_head - fruit.coord)
        else:
            self.body = self.body[:-1, :]
            cur_dist = np.linalg.norm(new_head - fruit.coord)
            if cur_dist < self.last_closed_dist:
                self.last_closed_dist = cur_dist
                self.tmp_posivie_move += 1
            else:
                self.fitness -= 0.2
            
        self.body = np.concatenate([[new_head], self.body], axis=0)
        self.direction = direction if not self.ai else self.direction if direction == 0 else (self.direction + 1) % 4 if direction == 1 else (self.direction + 3) % 4

        self.total_move += 1
        self.life_time -= 1
        if self.life_time == 0:
            self.fitness += self.tmp_posivie_move / self.total_move
            return False

        return True
    
    def observe(self, fruit):
        observed_state = [0., 0., 0., 0., 0., 0., 0., 0., 0.]
        possible_dir = [
            DIRECTIONS[self.direction],             # 현 방향 고수
            DIRECTIONS[(self.direction + 1) % 4],   # 우측 방향
            DIRECTIONS[(self.direction + 3) % 4]    # 좌측 방향
        ]

        head = self.body[0]
        for i, p_dir in enumerate(possible_dir):
            for j in range(5):
                observe_point = head + p_dir * (j + 1)
                if (
                    observe_point[0] < 0 or 
                    observe_point[0] > WINDOW_SIZE or
                    observe_point[1] < 0 or
                    observe_point[1] > WINDOW_SIZE or
                    observe_point.tolist() in self.body.tolist()
                ):
                    observed_state[i] = (5 - j) * 0.2
                    break
        
        for i, p_dir in enumerate(possible_dir):
            for j in range(5):
                observe_point = head + p_dir * (j + 1)
                if np.all(observe_point == fruit):
                    observed_state[i + 6] = 1.
                    break

        if np.sum(head * possible_dir[0]) <= np.sum(fruit * possible_dir[0]):
            observed_state[3] = 1

        if np.sum(head * possible_dir[1]) < np.sum(fruit * possible_dir[1]):
            observed_state[4] = 1
        else:
            observed_state[5] = 1
        
        return observed_state
