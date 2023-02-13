import tkinter as tk
from plateau import Plateau
from ia import IA

import sys

class GraphicPlateau:
    def __init__(self):
        self.plateau = Plateau()
        self.listeRect = []
        self.deplacementsPossibles = []
        self.canvas = None
        self.listePions = []
        self.turn = 0
        self.turnLabel = None
        if(len(sys.argv) > 1):
            if(sys.argv[1] == '1'):
                self.iaPlayer = 0
                print('ia is player 1')
            elif(sys.argv[1] == '2'):
                self.iaPlayer = 1
                print('ia is player 2')
            else:
                self.iaPlayer = None
                print('no ia')
        else: 
            self.iaPlayer = None
            print('no ia')

    def afficher_plateau(self):
        fenetre = tk.Tk()
        fenetre.title("Jeu de Dames")

        self.canvas = tk.Canvas(fenetre, width=600, height=600)
        self.canvas.pack()

        self.turnLabel = tk.Label(fenetre, text="Tour du joueur 1", font=("Arial", 20))
        self.turnLabel.pack()

        for i in range(10):
            for j in range(10):
                couleur = "white" if (i + j) % 2 == 0 else "lightgrey"
                x1, y1 = i * 50, j * 50
                x2, y2 = x1 + 50, y1 + 50
                r = self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")
                self.listeRect.append(r)
        
        for i in range(10):
            for j in range(10):
                idcase = self.get_id_case(i,j)
                if(idcase<=20 and idcase % 1 == 0):
                    p = self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="black")
                    self.listePions.append(p)
                elif(idcase>=31 and idcase % 1 == 0):
                    p = self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="white")
                    self.listePions.append(p)

        self.canvas.bind("<Button-1>", self.pion_clique)

        #? If the player 1 is an IA
        if(self.iaPlayer == 0):
            move = ia.play(self.plateau.plateau, True)
            self.deplacer(move[1], move[0])

        # Afficher la fenêtre
        fenetre.mainloop()

    
    def get_id_case(self, ligne, colonne):
        if(ligne % 2 == 0):
            return 5 * ligne + (colonne + 1) / 2
        else:
            return 5 * ligne + (colonne + 1) / 2 + 0.5
    
    def get_col(self, id):
        match id % 10:
            case 6 : 
                return 0
            case 1:
                return 1
            case 7:
                return 2
            case 2:
                return 3
            case 8:
                return 4
            case 3:
                return 5
            case 9:
                return 6
            case 4:
                return 7
            case 0:
                return 8
            case 5:
                return 9
    
    def get_lig(self, id):
        return int(id*2-1)//10

    def pion_clique(self, event):
        x, y = event.x, event.y

        colonne = x // 50
        ligne = y // 50
        idcase = self.get_id_case(ligne, colonne)

        movement = False

        # verifying before reset deplacementsPossibles

        #! Ici aussi peut être
        if(idcase % 1 == 0):
            for deplacement in self.deplacementsPossibles :
                if(deplacement == idcase):
                    self.deplacer(deplacement)
                    movement = True

        # This erase the green cases

        #! Il faut trouver le bug ici qui return une erreur
        for case in self.deplacementsPossibles:
            colonne = self.get_col(case)
            ligne = self.get_lig(case)
            self.canvas.itemconfig(self.listeRect[ligne + colonne * 10], fill="lightgrey")
        self.deplacementsPossibles = []

        if(idcase % 1 == 0 and movement == False and self.plateau.plateau[round(idcase)][0] == self.turn):
            dp = self.plateau.deplacementsPossible(round(idcase))
            self.colorie(dp)
            self.selectedPion = idcase
    
    def colorie(self, deplacements):
        for deplacement in deplacements:
            colonne = self.get_col(deplacement)
            ligne = self.get_lig(deplacement)

            self.canvas.itemconfig(self.listeRect[ligne + colonne * 10], fill="green")
            self.deplacementsPossibles.append(deplacement)
    
    def deplacer(self, deplacement, initPos = None):
        if self.turn == 0:
            self.turnLabel.config(text="Tour du joueur 2")
            self.turn = 1
        else:
            self.turnLabel.config(text="Tour du joueur 1")
            self.turn = 0

        if(initPos == None):
            initPos = round(self.selectedPion)

        coords = [
            self.get_col(initPos) * 50 + 10,
            self.get_lig(initPos) * 50 + 10,
            self.get_col(initPos) * 50 + 40,
            self.get_lig(initPos) * 50 + 40
        ]

        finalCoords = [
            self.get_col(deplacement) * 50 + 10,
            self.get_lig(deplacement) * 50 + 10,
            self.get_col(deplacement) * 50 + 40,
            self.get_lig(deplacement) * 50 + 40
        ]

        (dame, elimination) = self.plateau.deplacer(initPos, deplacement)

        for pion in self.listePions:
            if(self.canvas.coords(pion) == coords):
                self.canvas.coords(pion, finalCoords)

        if(dame != None):
            coordsDame = [
                self.get_col(dame) * 50 + 10,
                self.get_lig(dame) * 50 + 10,
                self.get_col(dame) * 50 + 40,
                self.get_lig(dame) * 50 + 40
            ]
            for pion in self.listePions:
                if(self.canvas.coords(pion) == coordsDame):
                    self.canvas.itemconfig(pion, outline="red")

        if(elimination != None and type(elimination) != tuple):
            #print('elimnation not null !', elimination)
            coordsElimination = [
                self.get_col(elimination) * 50 + 10,
                self.get_lig(elimination) * 50 + 10,
                self.get_col(elimination) * 50 + 40,
                self.get_lig(elimination) * 50 + 40
            ]
            for pion in self.listePions:
                if(self.canvas.coords(pion) == coordsElimination):
                    self.canvas.delete(pion)

        if(self.iaPlayer != None and self.turn == self.iaPlayer):
            isIAFirstPlayer = False if self.iaPlayer == 1 else True
            move = ia.play(self.plateau.plateau, isIAFirstPlayer)
            if(move == None):
                print('ia ne peut pas jouer')
            else:
                self.deplacer(move[1], move[0])

        if(self.plateau.plateau.count((0, False)) + self.plateau.plateau.count((0, True)) == 0):
            print('joueur 2 a gagné')
            self.turnLabel.config(text="Joueur 2 à gagné")
        elif(self.plateau.plateau.count((1, False)) + self.plateau.plateau.count((1, True)) == 0):
            print('joueur 1 a gagné')
            self.turnLabel.config(text="Joueur 1 à gagné")



ia = IA()
window = GraphicPlateau()
window.afficher_plateau()