import poke

pd = poke.Pokedex("gib.tsv")
copy = None
while True:
    option = input("""
        Welcome to the Pokedex!
        Please select an option ->
            1) - Search for a Pokemon
            2) - Add a Pokemon
            3) - Delete a Pokemon
            4) - Save a copy of the Pokedex
            5) - Display Pokemon
            6) - Leave""")
    if copy == None:
            selected = pd
    else:
            selected = pd if input("Do you want to use the pokedex or the saved copy? (P for Pokedex, C for copy) > ") == "P" else copy
    match option:
        case "1":
            try:
                pokeFound = selected.binaryTree.search(int(input("Please input the Pokemon's ID>")))
                print("Pokemon Found! \n American Name: " +  str(pokeFound.americanName) + "\n Japanese Name: " + str(pokeFound.japanName) + "\nID: " + str(pokeFound.number))
            except:
                print("ERROR: Pokemon not found!")
                continue
        case "2":
            newPoke = poke.Pokemon(number=int(input("Please give this Pokemon a number ID > ")), americanName = input("Please give this Pokemon an American Name > "), japanName=input("Please give this Pokemon a Japanese Name > "))
            selected.binaryTree.add(newPoke)
        case "3":
            selected.binaryTree.delete(int(input("Please type the number of the Pokemon to delete > ")))
        case "4":
            copy = pd
        case "5":
            selected.binaryTree.display(sortMethod=input("How would you like to display this, pre, in, or post? > "))
        case "6":
            break
