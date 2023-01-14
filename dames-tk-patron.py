import tkinter as tk
from jeu import Jeu

class Plateau:
    def __init__(self):
        self.jeu = Jeu()
        self.listeRect = []
        # self.casesVertes = []
        self.deplacementsPossible = []
        self.canvas = None
    
    def afficher_plateau(self):
        # Créer une fenêtre tkinter
        fenetre = tk.Tk()
        fenetre.title("Jeu de Dames")

        # Créer un canvas dans la fenêtre pour dessiner le plateau de jeu
        self.canvas = tk.Canvas(fenetre, width=600, height=600)
        self.canvas.pack()

        # Dessiner le plateau de jeu en dessinant des carrés blancs et noirs
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
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="black")
                if(idcase>=31 and idcase % 1 == 0):
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="white")

        self.canvas.bind("<Button-1>", self.pion_clique)

        # Afficher la fenêtre
        fenetre.mainloop()
    
    # Dessiner les pions sur le plateau
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
        # Récupérer les coordonnées du clic de la souris
        x, y = event.x, event.y
        # Calculer la ligne et la colonne du pion sélectionné
        colonne = x // 50
        ligne = y // 50
        idcase = self.get_id_case(ligne, colonne)

        if(idcase % 1 == 0):
            for d in self.deplacementsPossible :
                print('deplacement', d.pos)
            print('clicked', round(idcase))
            for deplacement in self.deplacementsPossible:
                if(deplacement.pos == round(idcase)):
                    self.deplacer(deplacement)
        
        # Effacer les cases vertes existantes
        for case in self.deplacementsPossible:
            colonne = self.get_col(case.pos)
            ligne = self.get_lig(case.pos)
            self.canvas.itemconfig(self.listeRect[int(colonne + 1)*10+int(ligne-1*10)], fill="lightgrey")
        self.deplacementsPossible = []

        
        # Afficher les coordonnées du pion sélectionné
        if(idcase % 1 == 0):
            pion = self.jeu.getPionAtPos(round(idcase))
            if (pion):
                dp = self.jeu.getDeplacementPossibles(pion)
                self.colorie(dp)
                self.selectedPion = pion;


    
    def colorie(self, deplacements):
        for deplacement in deplacements :
            colonne = self.get_col(deplacement.pos)
            ligne = self.get_lig(deplacement.pos)
            self.canvas.itemconfig(self.listeRect[int(colonne + 1)*10+int(ligne-1*10)], fill="green")
            self.deplacementsPossible.append(deplacement)
            # self.casesVertes.append(deplacement.pos)
    
    def deplacer(self, deplacement):
        print('en train de deplacer')
        self.jeu.deplacer(self.selectedPion, deplacement)
        self.selectedPion = None
        #! Now we need to update the canvas and prevent pion_clique from being called

# Exemple d'utilisation
plateau = Plateau()
plateau.afficher_plateau()


