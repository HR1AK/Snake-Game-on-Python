class SnakeBlock:
    x = None
    y = None
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y 
    
    def IsInside(self, size_block):
        return True if self.x < size_block and self.x > -1 and self.y < size_block and self.y > -1 else False 

