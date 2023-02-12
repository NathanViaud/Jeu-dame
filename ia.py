from plateau import Plateau

class IA:

    #* Retourne un tuple sous la forme (Case départ, Case arrivée)
    def play(self, plateau: Plateau,  firstPlayer: bool) -> list:
        player = 0 if firstPlayer else 1
        deplacements = [];
        eliminations = [];
        pions = [i for i in range(1, 51) if plateau.plateau[i] != None and plateau.plateau[i][0] == player]
        for pion in pions:
            deplacementsPossibles = plateau.deplacementsPossible(pion)
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