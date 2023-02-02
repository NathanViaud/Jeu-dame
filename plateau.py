class Plateau:
    def __init__(self):
        self.cacheEliminations = []
        self.plateau = [None] * 51
        for i in range(1, 21):
            self.plateau[i] = (0, False)
        for i in range(31, 51):
            self.plateau[i] = (1, False)

    def __str__(self) -> str:
        return str(self.plateau)
    
    def deplacementBase(self, posPion: int) -> list:
        res = []
        isPairline = posPion%10 <= 5
        isLeftOutside = posPion%5 == 1 and not isPairline
        isRightOutside = posPion%5 == 0 and isPairline
        if(self.plateau[posPion][0] == 0 or self.plateau[posPion][1]):
            if(not isRightOutside):
                possiblePos = posPion + 6 if isPairline else posPion + 5
                res.append(possiblePos)
            if(not isLeftOutside):
                possiblePos = posPion + 5 if isPairline else posPion + 4
                res.append(possiblePos)
        if(self.plateau[posPion][0] == 1 or self.plateau[posPion][1]):
            if(not isLeftOutside):
                possiblePos = posPion - 5 if isPairline else posPion - 6
                res.append(possiblePos)
            if(not isRightOutside):
                possiblePos = posPion - 4 if isPairline else posPion - 5
                res.append(possiblePos)
        return res
    
    def eliminationPossible(self, pos1: int, pos2: int) -> tuple:
        res = None
        isPairline = pos1%10 <= 5
        isUpward = pos1 > pos2
        isRight = False
        if(isUpward) :
            isRight = pos1 == pos2 + 4 if isPairline else pos1 == pos2 + 5
            if(isRight):
                finalPos = pos1 - 9
                if self.plateau[finalPos] == None : return (finalPos, pos2)
            else:
                finalPos = pos1 - 11
                if self.plateau[finalPos] == None : return (finalPos, pos2)
        else:
            isRight = pos1 == pos2 - 5 if isPairline else pos1 == pos2 - 4
            if(isRight):
                finalPos = pos1 + 11
                if self.plateau[finalPos] == None : return (finalPos, pos2)
            else:
                finalPos = pos1 + 9
                if self.plateau[finalPos] == None : return (finalPos, pos2)
        return res
    
    def deplacementsPossible(self, posPion: int) -> list:
        res = []
        self.cacheEliminations = []
        baseDeplacements = self.deplacementBase(posPion)
        for deplacement in baseDeplacements:
            if self.plateau[deplacement] == None:
                res.append(deplacement)
            else:
                elimination = self.eliminationPossible(posPion, deplacement)
                if elimination != None:
                    self.cacheEliminations.append(elimination)
                    res.append(elimination[0])
        return res
    
    def deplacer(self, posPion: int, newPos: int):
        if newPos in self.deplacementsPossible(posPion):
            self.plateau[newPos] = self.plateau[posPion]
            self.plateau[posPion] = None

            #? Elimination
            for elimination in self.cacheEliminations:
                if elimination[0] == newPos:
                    self.plateau[elimination[1]] = None
                    return elimination[1]
            return None
