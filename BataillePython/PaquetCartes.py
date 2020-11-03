from random import *
from Carte import *
from PuissanceCarte import *

### Classe PaquetCarte héritant de list
### cette classe sera utilisé pour stocker le paquet initial avant distribution
class PaquetCartes(list):
    ### Créateur initialisant un paquet de carte standard
    def __init__(self):
        puissance = PuissanceCarte()
        for i in range(13):
            self.append(Carte(i,"Coeur",puissance.Standard))
            self.append(Carte(i,"Trefle",puissance.Standard))
            self.append(Carte(i,"Carreau",puissance.Standard))
            self.append(Carte(i,"Pique",puissance.Standard))

    ### Méthode permettant de mélanger le paquet de carte
    def Melanger(self):
        listeMelangee = []
        while len(self) > 0: 
            listeMelangee.append(self.pop(randint(0,len(self)-1))) # Réalise à la fois la suppression d'une carte du paquet d'origine et son ajout dans le nouveau paquet mélangé
        self.extend(listeMelangee)

    ### Méthode permettant de distribuer les cartes aux joueurs comme on le ferait autour d'une table de jeu
    def DistribuerCartes(self, joueurs):
        while len(self) > 0:
            for joueur in joueurs:
                joueur.Main.append(self.pop(0))
