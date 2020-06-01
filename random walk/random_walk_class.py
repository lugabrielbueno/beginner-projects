import random
import matplotlib.pyplot as plt

class RandomWalk():
    def __init__(self, numpoints,palette_choice):
        # inicia classe random walk
        self.numpoints = numpoints
        self.palette = palette_choice
        self.x_points = [0]
        self.y_points = [0]

    def direction(self):
        stepx = 0
        stepy = 0
        while len(self.x_points) < self.numpoints:
            xdirection = random.choice([-1,1])
            xdistance = random.choice([1,2,3,4])
            stepx += xdirection*xdistance
            
            ydirection = random.choice([-1,1])
            ydistance = random.choice([1,2,3,4])
            stepy += ydirection*ydistance
            if stepx == 0 and stepy == 0:
                continue
        
            self.x_points.append(stepx)
            self.y_points.append(stepy)

    def ploting(self):
        point_numbers = list(range(self.numpoints))
        plt.scatter(self.x_points,self.y_points,c = point_numbers,cmap=self.palette_choice,s=2)
        plt.show()

