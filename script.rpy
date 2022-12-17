# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image room = im.Scale("room.jpg", 1920, 1080 )
image Mark = im.Scale("mark.png", 700, 950 )
image elon = im.Scale("Elon.png", 700, 950)
#image ban = im.Scale("baned.png", 700, 2950)
define e = Character("Elon", image="elon")
define f = Character("Mark", image="Mark")
define a = Character("Mark", image="Mark", window_background="Mark.png")



# The game starts here.

label start:
    
    show screen AddNote
    show screen notebook
   
   

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show elon at right
    show Mark at left

    # These display lines of dialogue.

    f "Elon, why have you betrayed your own people"

    e "Marky..babe...Facebook is trash...only through the most toxic platform, I can obtain the n-word pass."

    f "Elon, it's too dangerous! The racism will corrupt your soul. Lets go back to a simpler time."

    e "That time is over, we are no longer lovers. I will dominate this world by any means necessary."

    e "plus, your verification subscription on Twitter is about to expire."

    f "Wait! Please! Think of the other platforms, they will all come after you!"

    e "Audiable sigh, I'm sorry my love."

    f "You can't..."

    e "Twitter stans hear me, I call upon the thosand karens to report you for being a man."

    e "I am sorry my love, but I can't give up on a dream again."
    hide Mark
    show Mark 
    a " "

    hide Mark

 

    # This ends the game.

    return
