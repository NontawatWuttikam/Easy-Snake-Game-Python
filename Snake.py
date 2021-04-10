import numpy as np
import matplotlib.pyplot as plt
import random

class Snake:

    def __init__(self,map_size = 20, speed = 0.15, theme = 'pale'):
        self.map_size = map_size
        self.gmap = np.zeros((self.map_size,self.map_size,3))
        self.speed = speed
        self.food = [random.randint(1,self.map_size-1),random.randint(1,self.map_size-1)]
        self.eat_food = False
        self.snake_queue = [[4,4],[4,3],[4,2]]
        self.fig, self.ax = plt.subplots()
        self.dir = 'R'
        self.score = 0
        self.theme = {'pale':[[0,255,0],
                            [255,90,90],
                            [90,90,90],
                            [140,140,140]],
                      'hi_con':[[0,255,0],
                            [255,0,0],
                            [0,0,0],
                            [0,0,255]],
                      'fallout':[[26,255,128],
                            [26,255,128],
                            [1,20,9],
                            [26,255,128]]}
        self.fsmb_color = self.theme[theme]
        status = 1
        while status != 0:
            status = self.render(None,None)
            print(self.dir)
    
    def render(self,food,snake):
        self.gmap = np.full((self.map_size,self.map_size,3),self.fsmb_color[2])
        self.gmap[0] = self.gmap[-1] = self.gmap[:,0] = self.gmap[:,-1] = self.fsmb_color[3]
        for i in self.snake_queue:
            self.gmap[i[0]][i[1]] = self.fsmb_color[1]
        if self.eat_food == True:
            while True:
                self.food = [random.randint(2,self.map_size-2),random.randint(2,self.map_size-2)]
                if self.food not in self.snake_queue:
                    break
        self.gmap[self.food[0],self.food[1]] = self.fsmb_color[0]
        head = self.snake_queue[0]
        if head == self.food:
            self.gmap[self.food[0],self.food[1]] = self.fsmb_color[1]
            self.score += 1
            self.eat_food = True
        else: 
            self.eat_food = False
        if self.dir == 'R':
            dir = [head[0],head[1]+1]
            stat = self.check_death(dir)
        elif self.dir == 'L':
            dir = [head[0],head[1] - 1]
            stat = self.check_death(dir)
        elif self.dir == 'U':
            dir = [head[0]-1,head[1]]
            stat = self.check_death(dir)
        elif self.dir == 'D':
            dir = [head[0]+1,head[1]]
            stat = self.check_death(dir)
        if stat == 0: return stat
        self.walk(dir,self.eat_food)
        self.ax.imshow(self.gmap)
        self.fig.canvas.mpl_connect('key_press_event', self.on_press)
        plt.pause(self.speed)
        plt.cla()

    def walk(self,dir,eat_food):
        self.snake_queue.insert(0,dir)
        if not eat_food:
            self.snake_queue.pop()

    def check_death(self,dir):
        if any([f >= self.map_size or f < 0 for f in dir]):
            print('Game over')
            print('Score : ',self.score)
            plt.close()
            return 0

    def on_press(self,event):
        if event.key == 'w':
            if self.dir != 'D':self.dir = 'U'
        elif event.key == 'a':
            if self.dir != 'R':self.dir = 'L'
        elif event.key == 'x':
            if self.dir != 'U':self.dir = 'D'
        elif event.key == 'd':
            if self.dir != 'L':self.dir = 'R'
            
Snake(theme='pale')
