# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image room = im.Scale("room.jpg", 1920, 1080 )
image Mark = im.Scale("BillClinton.png", 700, 950 )
image elon = im.Scale("Elon.png", 700, 950)
define e = Character("Elon", image="elon")




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show elon

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "suck on deez nuts"


    # This ends the game.

    return
