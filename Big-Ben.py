#  Importing Colorama Package
 
from colorama import init
init()

# Importing Main File

from Main import Main

# Importing Minding File

from Minding import Minding

# Importing Teacher_Id_View File

from Teacher_Id_View import Id_View

loop = True

while loop:

    print("\033[2J")
    print("")
    print("                       Big Ben")
    print("")
    print("")
    print("Service Provoided By Big Ben :-")
    print("")
    print("")
    print("     1. Time Table Shedule")
    print("")
    print("     2. Minding")
    print("")
    print("     3. Teacher's Id Viewer")
    print("")
    print("")

    Service = int(input("Please Enter The Service You Needed [ 1 / 2 / 3 ] : "))
    print("")

    if Service == 1:
        Main()

    if Service == 2:
        Minding()

    if Service == 3:
        Id_View()

    else :
        print("! ! ! !   Please Enter Valid Number ! ! ! ! ")
        print("")

    controller = input("Do You Want To Continue  [ Yes / No ] : ").lower()
    print("")
    
    if controller == "yes":
        loop = True

    else :
        loop = False