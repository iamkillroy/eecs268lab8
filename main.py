import poke

pd = poke.Pokedex("gib.tsv")

while True:
    option = input("""
        Welcome to the Pokedex!
        Please select an option ->
            1) - Search for a Pokemon
            2) - Add a Pokemon
            3) - Delete a Pokemon
            4) - Save a copy of the Pokedex
            5) - Remove a Pokemon
            7) - Display Pokemon
            8) - Leave""")
    match option:
        case "1":
            try:
                pokeFound = pd.binaryTree.search(int(input("Please input the Pokemon's ID>")))
                print("Pokemon Found! \n American Name: " +  str(pokeFound.americanName) + "\n Japanese Name: " + str(pokeFound.japanName) + "\nID: " + str(pokeFound.number))
            except:
                print("ERROR: Pokemon not found!")
                continue
        case "2":
            newPoke = poke.Pokemon(number=int(input("Please give this Pokemon a number ID > ")), americanName = input("Please give this Pokemon an American Name > "), japanName=input("Please give this Pokemon a Japanese Name > "))
            pd.binaryTree.add(newPoke)
        case "3":
            pd.binaryTree.delete(int(input("Please type the number of the Pokemon to delete > ")))
        case "7":
            pd.binaryTree.display(sortMethod=input("How would you like to display this, pre, in, or post? > "))
