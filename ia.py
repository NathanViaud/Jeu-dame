class IA:
    def __init__(self):
        self.cacheEliminations = []
        self.plateau = None

    #* Retourne un tuple sous la forme (Case départ, Case arrivée)
    def play(self, plateau: list,  firstPlayer: bool) -> list:
        player = 0 if firstPlayer else 1
        deplacements = [];
        eliminations = [];
        self.plateau = plateau
        pions = [i for i in range(1, 51) if plateau[i] != None and plateau[i][0] == player]
        for pion in pions:
            deplacementsPossibles = self.deplacementsPossible(pion)
            for deplacement in deplacementsPossibles:
                if(deplacement > pion + 8):
                    eliminations.append((pion, deplacement))
                elif(deplacement < pion - 8):
                    eliminations.append((pion, deplacement))
                else:
                    deplacements.append((pion, deplacement))
        if(len(eliminations) > 0):
            return eliminations[0]
        elif(len(deplacements) > 0):
            #? Voir si on peux importer random
            return deplacements[0]
        else :
            return None
    
    def deplacementBase(self, posPion: int) -> list:
        res = []
        isPairline = (posPion - 1)%10 < 5
        isLeftOutside = posPion%5 == 1 and not isPairline
        isRightOutside = posPion%5 == 0 and isPairline

        isTopOutisde = posPion < 6
        isBottomOutside = posPion > 45

        if(self.plateau[posPion] == None): return res
        
        if(self.plateau[posPion][0] == 1 or self.plateau[posPion][1]):
            #? Right bottom move
            if(not isRightOutside and not isBottomOutside):
                possiblePos = posPion + 6 if isPairline else posPion + 5
                res.append(possiblePos)
            #? Left bottom move
            if(not isLeftOutside and not isBottomOutside):
                possiblePos = posPion + 5 if isPairline else posPion + 4
                res.append(possiblePos)
        if(self.plateau[posPion][0] == 0 or self.plateau[posPion][1]):
            #? Left top move
            if(not isLeftOutside and not isTopOutisde):
                possiblePos = posPion - 5 if isPairline else posPion - 6
                res.append(possiblePos)
            #? Right top move
            if(not isRightOutside and not isTopOutisde):
                possiblePos = posPion - 4 if isPairline else posPion - 5
                res.append(possiblePos)
        return res
    
    def eliminationPossible(self, pos1: int, pos2: int) -> tuple:
        res = None
        if(self.plateau[pos1][0] == self.plateau[pos2][0]): return res
        isPairline = (pos1 - 1)%10 < 5
        isUpward = pos1 > pos2
        isRight = False
        if(isUpward) :
            isRight = pos1 == pos2 + 4 if isPairline else pos1 == pos2 + 5
            if(isRight):
                finalPos = pos1 - 9
                isOutside = finalPos <= 0 or pos2%10 == 5
                if not isOutside and self.plateau[finalPos] == None : return (finalPos, pos2)
            else:
                finalPos = pos1 - 11
                isOutside = finalPos <= 0 or pos2%10 == 6
                if not isOutside and self.plateau[finalPos] == None : return (finalPos, pos2)
        else:
            isRight = pos1 == pos2 - 6 if isPairline else pos1 == pos2 - 5
            if(isRight):
                finalPos = pos1 + 11
                isOutside = finalPos > 50 or pos2%10 == 5
                if not isOutside and self.plateau[finalPos] == None : return (finalPos, pos2)
            else:
                finalPos = pos1 + 9
                isOutside = finalPos > 50 or pos2%10 == 6
                if not isOutside and self.plateau[finalPos] == None : return (finalPos, pos2)
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