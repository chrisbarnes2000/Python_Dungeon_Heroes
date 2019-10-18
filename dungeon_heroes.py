from hero import Hero
from prompts import prompt_usr

hero = None

def intro():
    #Display for Intro
    print("""
    ******----******----******
    Welcome to Dungeon Heroes!
    ******----******----******
    
    \^~~~~\\   )  (   /~~~~^/
     ) *** \\  {**}  / *** (
      ) *** \\_ ^^ _/ *** (
       ) ****   vv   **** (
        )_****      ****_(
          )*** m  m ***(
    """)

def create_character():
    name = prompt_usr("Enter your hero's name: \t", "string")
    char_class = prompt_usr("What class shall they be, a mighty (W)warrior or cunning (T)thief? \t", "string")
    hero = Hero(name, char_class)
    return hero

def restart():
    print("********")
    print("NEW GAME")
    print("********\n")
    hero = create_character()   # player chooses their player class
    hero.stats()               # tests player and shows us status
    return hero

def load_game():
    response = prompt_usr("Select (N)ew game or (C)ontinue: \t", "string").upper()
    if(response == "C"):
        #try:
            #hero = SaveGame.load("saveGame.txt")
            #print("File Loaded")
        #catch(FileNotFoundException e):
            #print("SaveGame not found")
            #createCharacter(g_input)
        hero = Hero("bill", "warrior")
        return hero
    elif(response == "N"):
        hero = restart()
        print("\nThree months ago, you set out from your village looking for glory and riches.")
        print("After a long journey into the mountains, you came across a cave.")
        print("You hear horrible noises coming from inside.")
        response = prompt_usr("Do you want to (E)enter or (L)leave? \t", "string").upper()
        if (response == "E"):
            return hero
        else:
            print("You Left")
            return
    else:
        print("Not an option, Sorry")
        print("Terminating")

#choice: allows the user to(E)enter next room, (R)est, (S)status or open(I)inventory, (Q)quit game
#@param - -> input A scanner to console input
#@return - -> true when they hit enter... false to leave the game
def choice():
    # prompt user
    print("\nThe room is now safe")
    response = ""
    while(not response == "E"):
        response = prompt_usr("Do you want to (R)est to recover stamina and health, check your(S)status, open your (I)inventory, " +
                            " \n(E)enter the next room, Enter the s(H)op, or save and (Q)uit the game. \t", "string").upper()
        # resting
        if(response == "R"):
            hero.rest()

        # status
        elif(response == "S"):
            hero.stats()

        # open inventory
        elif(response == "I"):
            hero.inventory.handleInventory(hero)

        #elif(response == "H"):
        #    g_store.enterStore(hero)

        # quit game
        elif(response == "Q"):
            return False
            """
            try:
                SaveGame.save(hero, "save_game.txt")
                return False
            except FileNotFoundError:
                print("There was a problem Saving, file not found")
                return False
        """
        return True



if __name__ == "__main__":
    intro()
    
    #load old game or start a new one
    hero = load_game()

    #Main loop to play game
    print()
    game_is_running = True
    while(game_is_running):
        #print("Starting battle")
        if hero != None:
            #hero.fight_monster()
        
            choice()
        
        play = prompt_usr("Play Again? Y or N: \t", "string").upper()
        if play == "N":
            game_is_running = False
        else:
            #resart to play again
            hero = restart()
            pass
