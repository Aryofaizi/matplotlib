from random import choice
class RandomWalk:
    """a class to simulate a random walk."""
    
    def __init__(self, num_points):
        """initialize attributes."""
        self.num_points = num_points
        
        self.x_value = [0]
        self.y_value = [0]
        
    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_value) < self.num_points:
            
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4,])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step
            
            self.x_value.append(x)
            self.y_value.append(y)
        
        