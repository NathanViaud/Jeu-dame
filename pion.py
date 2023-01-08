class Pion:
    
    def __init__(self, pos, color) -> None:
        self.pos = pos
        self.dame = False
        self.color = color

    def deplacer(self, pos):
        self.pos = pos
    
    def set_dame(self, dame):
        self.dame = dame
