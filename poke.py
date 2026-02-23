import btree

class Pokemon:
    def __init__(self, number: int, americanName: str, japanName:str) -> None:
        """Creates a Pokemon onto this planet"""
        self.number = number
        self.americanName = americanName
        self.japanName = japanName
    def __ge__(self, other):
        if type(other) == type(self):
            return self.number >= other.number
        elif type(other) == type(1):
            return self.number >= other
    def __le__(self, other):
        if type(other) == type(self):
                return self.number <= other.number
        elif type(other) == type(1):
            return self.number <= other
    def __gt__(self, other):
        if type(other) == type(self):
            return self.number > other.number
        elif type(other) == type(1):
            return self.number > other
    def __lt__(self, other):
        if type(other) == type(self):
                return self.number < other.number
        elif type(other) == type(1):
            return self.number < other
    def __eq__(self, other):
        if type(other) == type(self):
                return self.number == other.number
        if type(other) == type(1):
                return self.number == other
class Pokedex:
    def __init__(self, fileName: str) -> None:
        """Creates a Pokedex"""
        self.binaryTree = btree.BinaryTree()
        self.fileText = open(fileName, "r").read()

        for line in self.fileText.split("\n"):
            if len(line) == 0: continue
            tabSplitLine = line.split("\t")

            newPokemon = Pokemon(number=int(tabSplitLine[1]), americanName=tabSplitLine[0], japanName = tabSplitLine[2])
            self.binaryTree.add(newPokemon)
