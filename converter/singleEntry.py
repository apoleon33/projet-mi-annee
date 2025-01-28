from converter.itemTypes import ItemTypes
from read import Cells


class SingleEntry:
    def __init__(self, itemType: ItemTypes):
        self.itemType = itemType

    @staticmethod
    def createFromCell(cell: Cells):
        for item in ItemTypes:
            if item == cell.Type: return SingleEntry(item)