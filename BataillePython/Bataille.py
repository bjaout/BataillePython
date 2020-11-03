from PaquetCartes import *
from Joueur import *

class Bataille:
    # On créé nos deux joueurs et le paquet de cartes initial
    def __init__(self):
        self.joueur1 = Joueur("Toto")
        self.joueur2 = Joueur("Titi")
        self.jeuDeCarte = PaquetCartes()

    # On lance la partie après avoir mélangé et distribuer les cartes
    def Run(self):
        joueurs = []
        joueurs.append(self.joueur1)
        joueurs.append(self.joueur2)
        self.jeuDeCarte.Melanger()
        self.jeuDeCarte.DistribuerCartes(joueurs)
        return self.JouerPartie(joueurs)

    # Méthode permettant de dérouler la partie
    def JouerPartie(self, joueurs):
        jouer = True
        gagnant = 0
        while jouer:
            if len(joueurs[0].Main) == 0:
                jouer = False
                gagnant = 1
            elif len(joueurs[1].Main) == 0:
                jouer = False
                gagnant = 0
            if jouer:
                 pliActuelle=[]
                 batailleActuelle=[]
                 gagnantPli = self.JouerPli(joueurs, pliActuelle, batailleActuelle)
                 for carte in pliActuelle:
                     joueurs[gagnantPli].Main.append(carte)
                 for carte in batailleActuelle:
                     joueurs[gagnantPli].Main.append(carte)
        return joueurs[gagnant].Name

    # Méthode récursive pour jouer des plis jusqu'à ce qu'un pli soit gagné par l'un ou l'autre des joueurs
    def JouerPli(self, joueurs, pliActuelle, batailleActuelle):
        jouer = True
        gagnant = 0
        if len(joueurs[0].Main) == 0:
            jouer = False
            gagnant = 1
        elif len(joueurs[1].Main) == 0:
            jouer = False
            gagnant = 0
        if jouer:
            for joueur in joueurs:
                pliActuelle.append(joueur.Main.pop(0))
            meilleureCarte = None
            index = 0
            for carte in pliActuelle:
                if meilleureCarte is None:
                    meilleureCarte=carte
                else:
                    if meilleureCarte > carte:
                        pass
                    elif meilleureCarte == carte:
                        for carte in pliActuelle:
                            batailleActuelle.append(carte)
                        pliActuelle = []
                        for joueurBat in joueurs:
                            try :
                                batailleActuelle.append(joueurBat.Main.pop(0))
                            except IndexError :
                                pass
                        gagnant = self.JouerPli(joueurs,pliActuelle,batailleActuelle)
                        break
                    else:
                        meilleureCarte = carte
                        gagnant = index
                index+=1
        return gagnant

            
    
