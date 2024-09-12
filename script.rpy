# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Adi = Character("Adi") 
define Developer = Character("Dev")

image adi happy = "images/adi happy.png"
image adi why = "images/adi why.png"
image adi gay = "images/adi-astolfo.png"
image adi scare = "images/adi scared.png"
image pateu = "images/pateu.png"
image Dev a= "images/Dev.png"
image sticla = "images/sticla.png"

image bg bucatarie = "images/bucatarie/main.png"
image bg masa = "images/bucatarie/masa.png"
image bg frigider = "images/bucatarie/frigider.png"
image bg balcon = "images/bucatarie/balcon.png"
image bg room = "images/camera.png"
image bg scari = "images/scari.png"





# The game starts here.
label start:
    jump skip
label skip: 
    stop music fadeout 5.0
    "Continuare la Adi the game 1"
    "lil bro tot nu a platit nimic..."
    "Capitol I"
    "Inceputul"
    show bg room
    show adi happy at Position(xalign=0.2, yalign=0.4)
    Adi "Ahhh, ce zi minunata!"
    show adi why at Position(xalign=0.2, yalign=0.4)
    Adi "DE CE ARAT ASA?!"
    show Dev a at Position(xalign=0.95, yalign=0.4)
    Developer "(Vlad) nu am bani. asa ca taci."
    show adi happy 
    Adi "a ok"
    hide Dev
    Adi "...Ce zi e?"
    "*vocile*" "luni."
    Adi "..."
    "*vocile*" "septembrie"
    Adi "Nu inteleg..."
    "*vocile*" "A INCEPUT SCOALA PROSTULE"
    show adi scare at Position(xalign=0.2, yalign=0.4)
    Adi "ohh no"
    show bg masa
    show adi happy at Position(xalign=0.7, yalign=0.4)
    Adi "Hmm.. eu... foame.."
    show pateu at truecenter
    show adi scare
    Adi "uau! Pateu"
    show adi happy
    Adi "De ce e asa pixelat 💀"
    "*vocile*" "Taci si manca ca mai ai 15 minute si trebuie sa ajungi la scoala sclavule 🗣️"
    show adi why at Position(xalign=0.7, yalign=0.4)
    Adi "Bine."
    show adi happy at Position(xalign=0.7, yalign=0.4)
    pause 4
    hide pateu
    Adi "Hai sa beau si apa si plec."
    hide adi happy
    show bg balcon
    show adi happy at Position(xalign=0.44, yalign=0.5)
    show sticla at truecenter
    Adi "Ahh... apa."
    hide sticla
    Adi "Ahhh, ce buna a fost acea apa!"
    show bg scari
    show adi happy at Position(xalign=0.475, yalign=0.5)
    Adi "Hai sa ma grabesc sa prind autobuz."

    ""
    


    return
