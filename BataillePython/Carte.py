from functools import *

### Classe carte qui représente une carte
@total_ordering # Evite de devoir écrire les 6 méthodes de comparaison
class Carte:
    def __init__(self,valeur,couleur,dicType):
        self.valeur=valeur
        self.couleur=couleur
        self.dicType=dicType
    
    # Implémentation des trois fonctions de conversion en chaine de caractères
    def __str__(self):
        return dicType[self.valeur] + " de " + self.couleur

    def __unicode__(self):
        return u(dicType[self.valeur] + " de " + self.couleur)

    def __repr__(self):
        return self.dicType[self.valeur] + " de " + self.couleur

    # Implémentation de deux fonctions de comparaison les autres étant déduite grace à @total_ordering
    def __lt__(self,other):
        return self.valeur < other.valeur

    def __eq__(self,other):
        return self.valeur == other.valeur

    # Défini si il est possible d'utiliser un opérateur spécifique. Ici oui si l'autre object a bien un attribut valeur (en gros si c'est aussi une Carte)
    def _is_valid_operand(self,other):
        return(hasattr(other,"valeur"))
