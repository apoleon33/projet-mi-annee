from abc import ABC, abstractmethod

from converter.itemTypes import ItemTypes
from read import Cells


class SingleEntry(ABC):
    """
    Équivalent de `Cells`, mais à ma manière
    """
    itemType: ItemTypes
    content: str

    def __init__(self, itemType: ItemTypes, content: str):
        self.itemType = itemType
        self.content = content

    @staticmethod
    def createFromCell(cell: Cells):
        """
        Créé un objet `SingleEntry` à partir d'un objet `Cells`.
        :param cell: la cellule à convertir
        :return: `SingleEntry`
        """
        item_type = None
        for item in ItemTypes:
            if item.value == cell.Type:
                item_type = item
                break

        match item_type:
            case ItemTypes.date:
                return DateEntry(cell.Content)
            case ItemTypes.titre:
                return TitreEntry(cell.Content)
            case ItemTypes.lieu:
                return LieuEntry(cell.Content)
            case ItemTypes.dsc:
                return DscEntry(cell.Content)
            case ItemTypes.freq:
                return FreqEntry(cell.Content)
            case ItemTypes.IMP:
                return IMPEntry(cell.Content)
            case _:
                return NPEntry(cell.Content)

    def __str__(self):
        return f"<SingleEntry {self.itemType} {self.content}>"

    @abstractmethod
    def convertToCode(self) -> str:
        """
        Cette méthode abstraite décrit comment une case devrait être convertit en code
        :return: le code à écrire
        """
        pass

class NPEntry(SingleEntry):
    def __init__(self, content: str):
        super().__init__(ItemTypes.NP, content)

    def convertToCode(self) -> str:
        return f"<h1>{self.content.split(" ")[0]} {self.content.split(" ")[1]}</h1>"

class DateEntry(SingleEntry):
    def __init__(self, content: str):
        super().__init__(ItemTypes.date, content)

    def convertToCode(self) -> str:
        return ""

class TitreEntry(SingleEntry):
    def __init__(self, content: str):
        super().__init__(ItemTypes.titre, content)

    def convertToCode(self) -> str:
        return ""

class LieuEntry(SingleEntry):
    def __init__(self, content: str):
        super().__init__(ItemTypes.lieu, content)

    def convertToCode(self) -> str:
        return ""

class DscEntry(SingleEntry):
    def __init__(self, content: str):
        super().__init__(ItemTypes.dsc, content)

    def convertToCode(self) -> str:
        return ""

class FreqEntry(SingleEntry):
    def __init__(self, content: str):
        super().__init__(ItemTypes.freq, content)

    def convertToCode(self) -> str:
        return ""

class IMPEntry(SingleEntry):
    def __init__(self, content: str):
        super().__init__(ItemTypes.IMP, content)

    def convertToCode(self) -> str:
        return ""