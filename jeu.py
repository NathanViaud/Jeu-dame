from pion import Pion
from deplacement import Deplacement
import math

class Jeu:
    #! Voir dans le sujet pour la représentation du plateau
    def __init__(self):
        self.pions = []
        for i in range(1, 21):
            self.pions.append(Pion(i, 'black'))
        for i in range(31, 51):
            self.pions.append(Pion(i, 'white'))

    def deplacementBase(self, pion):
        res = []
        isPairline = pion.pos%10 <= 5
        isLeftOutside = pion.pos%5 == 1 and not isPairline
        isRightOutside = pion.pos%5 == 0 and isPairline
        if(pion.color == 'black' or pion.dame):
            if(not isRightOutside):
                possiblePos = Deplacement(pion.pos + 6 if isPairline else pion.pos + 5)
                res.append(possiblePos)
            if(not isLeftOutside):
                possiblePos = Deplacement(pion.pos + 5 if isPairline else pion.pos + 4)
                res.append(possiblePos)
        elif(pion.color == 'white' or pion.dame):
            if(not isLeftOutside):
                possiblePos = Deplacement(pion.pos - 5 if isPairline else pion.pos - 6)
                res.append(possiblePos)
            if(not isRightOutside):
                possiblePos = Deplacement(pion.pos - 4 if isPairline else pion.pos - 5)
                res.append(possiblePos)
        return res

    # If there is a pion at pos, return its color
    # TODO: refractor this
    def getColorAtPos(self, pos):
        for pion in self.pions:
            if(pion.pos == pos):
                return pion.color
        return None
    
    def getPionAtPos(self, pos):
        for pion in self.pions:
            if(pion.pos == pos):
                return pion
        return None

    # pos1 is the position of the pion that is moving and pos2 is the position of the pion that is being eliminated
    def eliminationPossible(self, pos1, pos2):
        print('elimination possible')
        res = None
        isPairline = pos1%10 <= 5
        isUpward = pos1 > pos2
        isRight = False
        if(isUpward) :
            isRight = pos1 == pos2 + 4 if isPairline else pos1 == pos2 + 5
            if(isRight):
                print('up right');
                finalPos = pos1 - 9
                if self.getColorAtPos(finalPos) == None : return Deplacement(finalPos, pos2)
            else:
                print('up left');
                finalPos = pos1 - 11
                if self.getColorAtPos(finalPos) == None : return Deplacement(finalPos, pos2)
        else:
            isRight = pos1 == pos2 - 6 if isPairline else pos1 == pos2 - 5
            if(isRight):
                finalPos = pos1 + 11
                print('down right', finalPos);
                if self.getColorAtPos(finalPos) == None : return Deplacement(finalPos, pos2)
            else:
                print('down left');
                finalPos = pos1 + 9
                if self.getColorAtPos(finalPos) == None : return Deplacement(finalPos, pos2)
        return res

    def getDeplacementPossibles(self, pion):
        res = []
        baseDeplacements = self.deplacementBase(pion)
        for deplacement in baseDeplacements:
            colorAtPos = self.getColorAtPos(deplacement.pos)
            if(colorAtPos == None):
                res.append(deplacement)
            elif(colorAtPos != pion.color):
                res.append(self.eliminationPossible(pion.pos, deplacement.pos))
        return res

    def deplacer(self, pion, deplacement):
        pion.deplacer(deplacement.pos)
        if(deplacement.eliminatedPion != None):
            self.removeAtPos(deplacement.eliminatedPion)
    
    def removeAtPos(self, pos):
        for pion in self.pions:
            if(pion.pos == pos):
                self.pions.remove(pion)
                return