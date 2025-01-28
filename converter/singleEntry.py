from converter.itemTypes import ItemTypes
from read import Cells


class SingleEntry:
    """
    Équivalent de `Cells`, mais à ma manière
    """
    def __init__(self, itemType: ItemTypes):
        self.itemType = itemType

    @staticmethod
    def createFromCell(cell: Cells):
        """
        Créé un objet `SingleEntry` à partir d'un objet `Cells`.
        :param cell: la cellule à convertir
        :return: `SingleEntry`
        """
        for item in ItemTypes:
            if item == cell.Type: return SingleEntry(item)