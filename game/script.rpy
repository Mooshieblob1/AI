# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init -1 python:
    config.has_autosave = False
    config.has_quicksave = False
define a = Character("Annabelle", images='annabelle')
define b = Character("Emma", images='emma')
image annabelle = im.Scale("Annabelle.png", 667, 1000)
image bg extbeach = "bg1.png"
image bg extstreet = "bg2.png"

# The game starts here.

transform walk_from_left_to_right:
    xalign 0.0 yalign 1.0
    ease 1.0 xalign 1.0 yalign 1.0

transform walk_and_fade:
    xalign 1.0 yalign 1.0
    parallel:
        linear 0.5 xalign 0.5
    parallel:
        linear 0.5 xalign 0.0
        linear 0.5 alpha 0.0 


label start:



    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg extbeach
    $ renpy.music.set_volume(0.5)
    play music "beach.mp3" fadein 2.0 # Replace "bgm_track.ogg" with your BGM filename

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show annabelle at left with dissolve
    a "It sure is hot out here..."

    "Annabelle looks around, and notices everyone else is also visibly sweating and hot."

    show annabelle at walk_from_left_to_right
    $ renpy.pause(1.0, hard=True)

    a "I wonder where everyone else went..."

    show annabelle at walk_and_fade

    "Annabelle proceeds to look for the others."

    scene bg extstreet

    "Meanwhile..."

    # This ends the game.

    return
