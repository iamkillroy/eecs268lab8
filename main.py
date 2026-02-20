import poke

pd = poke.Pokedex("gib.tsv")
pd.binaryTree.display("pre")

a = pd.binaryTree.search(127)
print(a.japanName)
b = pd.binaryTree.delete(128)
