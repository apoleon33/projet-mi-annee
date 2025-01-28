from enum import Enum


class ItemTypes(Enum):
    """
    Tous les types de cases que l'utilisateur peut créer
    """
    NP = "NP"  # Nom/prénom
    date = "date"  # jj / mm / aaaa
    titre = "Titre"  # titre
    lieu = "lieu"  # place
    dsc = "dsc"  # description
    freq = "Frequ"  # Fréquence
    IMP = "IMP"  # importance(niveau 1 - 2 - 3 - 4)
