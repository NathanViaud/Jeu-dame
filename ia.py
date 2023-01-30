class IA:
    #* plateau est un plateau de tuple ou None
    #* plateau[i] == None si la case est vide
    #* plateau[i] == (0, False) si pion normal joueur 1
    #* plateau[i] == (0, True) si dame joueur 1
    #* plateau[i] == (1, False) si pion normal joueur 2
    #* plateau[i] == (1, True) si dame joueur 2

    #? Je sais pas si le constructeur est nécessaire

    #* Retourne un tuple sous la forme (Case départ, Case arrivée)
    def play(plateau: list, firstPlayer: bool) -> list(int, int):
        pass