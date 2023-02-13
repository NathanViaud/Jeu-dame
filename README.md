# Jeu de dame

## Règles
- L'IA joue en position précisée par le chiffre 1 ou 2 dans la commande de lancement
- Chacun leurs tours les joueurs peuvent avancer un pion en diagonale
- Ils peuvent manger un pion adverse en passant par dessus
- Lorsqu'un pion atteint le camp adverse, il devient une dame et peu alors reculer ou avancer
- Un joueur gagner la partie lorsque son adversaire n'a plus de pions sur le plateau
  
## Interface graphique:
- Les cases vertes représentent les déplacements possible du pion selectionné
- Les pions avec une bordure rouge représentent les dames
## Setup
```bash
#Lancer le jeu en mode 2 joueurs
python tk-window.py

# Lancer le jeu contre l'ia en tant que joueur 1
python tk-window.py 1

# Lancer le jeu contre l'ia en tant que joueur 2
python tk-window.py 2

```

### Authors
Nathan VIAUD
Mathis ENRICI
Carlos CEREN
Manuel HERNANDEZ
