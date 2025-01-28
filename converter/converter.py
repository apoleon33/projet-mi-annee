from typing import TextIO

from converter.singleEntry import SingleEntry


class Converter:
    """
    La classe `Converter` est celle qui va faire le gros du travail de conversion entre son entrée et sa sortie en code.
    """

    def __init__(self, entries: list[SingleEntry]):
        self.entries = entries
        self.code = Code()

    def convert(self) -> None:
        # On aura la logique ici
        pass


class Code:
    """
    La classe `Code` contient le code qui sera sortit par le programme.
    """

    def __init__(self) -> None:
        self.code = ""

    def addLine(self, line: str) -> None:
        self.code += line
        self.code += "\n"

    def addMultipleLine(self, lines: list[str]) -> None:
        for line in lines:
            self.addLine(line)

    def writeToFile(self, file: TextIO) -> None:
        file.write(self.code)
