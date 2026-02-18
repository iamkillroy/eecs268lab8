import btree

class Pokemon:
    def __init__(self, number: int, americanName: str, japanName:str) -> None:
        """Creates a Pokemon onto this planet"""
        self.number = number
        self.americanName = americanName
        self.japanName = japanName
    def __ge__(self, other):
        return self.number >= other.number
    def __le__(self, other):
        return self.number <= other.number
    def __gt__(self, other):
        return self.number > other.number
    def __lt__(self, other):
        return self.number < other.number
    def __eq__(self, other):
        return self.number == other.number
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

