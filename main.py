import poke

pd = poke.Pokedex("gib.tsv")
#pd.binaryTree.display("pre")

a = pd.binaryTree.search(9)
print(a)
