import time

print(
    "Welcome! To view this game in the best way,\nmake sure your window is tall enough.\nThis game requires input to "
    "continue \nHope you enjoy it!\n\n")
player = input("Enter player name: ")


def divider():
    for i in range(2):
        print("║", " " * 57, "║", sep='')


def div_top(pause):
    print("╔", "═" * 57, "╗", sep='')
    divider()
    time.sleep(pause)


def div_bottom(pause):
    divider()
    print("╚", "═" * 57, "╝", sep='')
    time.sleep(pause)


def intro():
    print(f"{player}! It's time to go home! We're done for today")
    div_top(0.1)
    print(mono_intro_1)
    div_bottom(3)
    div_top(0.1)
    print(mono_intro_2)
    div_bottom(3)
    div_top(0.1)
    print(mono_intro_3)
    div_bottom(5)


def choose_path():
    print(intersection)
    div_top(1)
    print(mono_intersection)
    div_bottom(1)
    global path
    path = input("Which path will you choose? \nLeft or right? (l/r):")
    if path == "l":
        shark_chase()
    elif path == "r":
        crocodile_chase()
    else:
        print("Invalid input")
        choose_path()
    return path


def shark_chase():
    global choice
    print(chase_shark)
    print(shark_story)
    choice = input("Do you want be friends with the shark or try to kill it?\nFriend or kill? (f/k):")
    if choice == 'f':
        print(shark_friend)
    elif choice == 'k':
        print(shark_kill)
        restart()
    else:
        print("Invalid input")
        shark_chase()
    return choice


def crocodile_chase():
    global choice
    print(chase_crocodile)
    print(crocodile_story)
    choice = input("Do you want to be friends with this crocodile or try to kill it?\nFriend or kill? (f/k):")
    if choice == 'f' or choice == 'k':
        print(crocodile_kill)
    else:
        print("Invalid input")
        crocodile_chase()
    return choice


def restart():
    global play_again
    play_again = input("Would you like to play again? Yes or no? (y/n)")
    if play_again == 'n':
        print("Thanks's for playing!")
        quit()
    elif play_again != 'y':
        restart()
    while play_again == 'y':
        print("Restarting game")
        main()


def main():
    intro()
    choose_path()
    restart()


# High tech graphics were made with the help of "ASCII Art Studio"

mono_intro_1 = """║  On your way home after a rough 12 hour shift at work   ║
║  ...you suddenly hear music coming from the sewers.     ║"""
mono_intro_2 = """║  Even though you're tired and can't think of anything   ║
║  but that cold beer waiting in your refrigerator        ║
║  You decide to investigate these wonderful tunes        ║"""
mono_intro_3 = """║  You lift the manhole cover and climb down....          ║"""
mono_intersection = """║  You approach an intersection                           ║
║  You can spot a shark fin at the end of the left path   ║
║  and at the end of the other one...                     ║
║  ...you can spot a crocodile tail                       ║"""
intersection = """╔════════════════════════════╦════════════════════════════╗
║░░█                     █░░░║░░░█                     █░░║ 
║░█      ██▀▀▄▄           █░░║░░█      █>               █░║ 
║░█      ▀█    █▄         █░░║░░█     █ █>              █░║ 
║█        █      █▄        █░║░█      █  █>              █║ 
║█         █       █▄      █░║░█       █  ▀▀█▄           █║ 
║█         █         █     █░║░█        █▄    ▀▄         █║ 
║█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█░║░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█║
╚════════════════════════════╩════════════════════════════╝ """
chase_shark = """╔═════════════════════════════════════════════════════════╗
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▀▀██░░░║
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░░█▀░░░║
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░░░░█░░░░║
║░░░░░░░░░░░░█████░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░░░░░█░░░░░║
║░░░████░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░█░░░░░║
║▓▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
║▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
║▓▓▓▓▓█████▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
╚═════════════════════════════════════════════════════════╝"""
shark_story = """
As you approach the shark, it begins to chase you
Your instinct is to swim away...
But after a while, you decide to stop and turn around
"""
shark_kill = """╔═════════════════════════════════════════════════════════╗
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░░░░░░░▄▄▀▀██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░░░░░▄█    █▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░░░▄█      █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░▄█       █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░█         █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓██▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓║
╚═════════════════════════════════════════════════════════╝

Sharks are friends! Not enemies. It devours you
"""
shark_friend = """╔═════════════════════════════════════════════════════════╗
║          ♫                                              ║
║             ♪             ▄▄▄▄▄▄▄▄▄         ▄    ▄      ║
║       ▄      ♫           █..       █▄    ▄  █▄  ▄█      ║
║      ███       ♪      '&` █       0  █  ▀█  ▀████▀      ║
║      ███               #   █▄▄▄▄▄▄    ▄▀ █   █  █       ║
║      ▄█▄      ♪       _#_     vvvv█    ▄ █   █  █       ║
║     █ █ █            ( # )    █^^^^  ==   █▄▀   █       ║
║       █              / 0 \     ▀█▄   ===    ▄   █       ║
║       █             ( === )    █ █▀▄   ▄ █      █       ║
║      █ █             `---'     █▀   ▀▄  ▀█      ▀       ║
║▓▓▓▓▓█▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀▄▄▄▄▄▄▄▄▀▓▓▓▓▓▓▓▓║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
╚═════════════════════════════════════════════════════════╝

Well done! You found the source of the music!

Thank's for playing!
"""
chase_crocodile = """╔═════════════════════════════════════════════════════════╗ 
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║ 
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░<█░░░░░░░║ 
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░<█ █░░░░░░║ 
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░<█  █░░░░░░║ 
║░░░░░░░░░░░░█████░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀▀  █░░░░░░░║ 
║░░░████░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▀    ▄█░░░░░░░░║ 
║▓▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║ 
║▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║ 
║▓▓▓▓▓█████▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║ 
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║ 
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║ 
╚═════════════════════════════════════════════════════════╝"""
crocodile_story = """
As you approach the crocodile, it begins to chase you
Your instinct is to swim away...
But after a while, you decide to stop and turn around
"""
crocodile_kill = """╔═════════════════════════════════════════════════════════╗
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░░░░░░░░░░<█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░░░░░░░░░<█ █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░░░░░░░░<█  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░░░░░▄█▀▀  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░░░▄▀    ▄█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓██▓▓▓█████▓▓▓▓▓▓▓▓▓▓▓║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓███████▓▓▓▓▓▓▓▓▓▓║
╚═════════════════════════════════════════════════════════╝

This crocodile was not friendly. It devours you
"""
if __name__ == '__main__':
    main()
