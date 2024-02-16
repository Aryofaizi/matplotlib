from random import randint


class Die:
    """Simulates rolling one die."""
    
    
    def __init__(self, num_side=6):
        """Initialize die sides, defualt is D6."""
        self.num_side = num_side
        
    def roll(self):
        """Rolls the die."""
        return randint(1, self.num_side)
        
        