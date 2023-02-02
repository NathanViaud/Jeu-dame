import tkinter as tk
from plateau import Plateau

class GraphicPlateau:
    def __init__(self):
        self.plateau = Plateau()
        self.listeRect = []
        self.deplacementsPossibles = []
        self.canvas = None
        self.listePions = []

    def afficher_plateau(self):
        fenetre = tk.Tk()
        fenetre.title("Jeu de Dames")

        self.canvas = tk.Canvas(fenetre, width=600, height=600)
        self.canvas.pack()

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
        if(idcase % 1 == 0):
            for deplacement in self.deplacementsPossibles :
                if(deplacement == idcase):
                    self.deplacer(deplacement)
                    movement = True
        
        for case in self.deplacementsPossibles:
            colonne = self.get_col(case)
            ligne = self.get_lig(case)
            self.canvas.itemconfig(self.listeRect[ligne + colonne * 10], fill="lightgrey")
        self.deplacementsPossibles = []

        if(idcase % 1 == 0 and movement == False):
            dp = self.plateau.deplacementsPossible(round(idcase))
            self.colorie(dp)
            self.selectedPion = idcase
    
    def colorie(self, deplacements):
        for deplacement in deplacements:
            colonne = self.get_col(deplacement)
            ligne = self.get_lig(deplacement)

            self.canvas.itemconfig(self.listeRect[ligne + colonne * 10], fill="green")
            self.deplacementsPossibles.append(deplacement)
    
    def deplacer(self, deplacement):
        print('selected pion', round(self.selectedPion))
        print('deplacement', deplacement)

        coords = [
            self.get_col(self.selectedPion) * 50 + 10,
            self.get_lig(self.selectedPion) * 50 + 10,
            self.get_col(self.selectedPion) * 50 + 40,
            self.get_lig(self.selectedPion) * 50 + 40
        ]

        finalCoords = [
            self.get_col(deplacement) * 50 + 10,
            self.get_lig(deplacement) * 50 + 10,
            self.get_col(deplacement) * 50 + 40,
            self.get_lig(deplacement) * 50 + 40
        ]

        for pion in self.listePions:
            if(self.canvas.coords(pion) == coords):
                self.canvas.coords(pion, finalCoords)

        elimination = self.plateau.deplacer(round(self.selectedPion), deplacement)

        if(elimination != None):
            coordsElimination = [
                self.get_col(elimination) * 50 + 10,
                self.get_lig(elimination) * 50 + 10,
                self.get_col(elimination) * 50 + 40,
                self.get_lig(elimination) * 50 + 40
            ]
            for pion in self.listePions:
                if(self.canvas.coords(pion) == coordsElimination):
                    self.canvas.delete(pion)

    
window = GraphicPlateau()
window.afficher_plateau()