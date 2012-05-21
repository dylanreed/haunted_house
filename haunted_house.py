from sys import exit
from rooms import *

def generic_room():
    print genericroom

    next = raw_input("> ").lower()

    if next in ['n','north']:
        north()
    elif next in ['e','east']:
        east()
    elif next in ['s','south']:
        south()
    elif next in ['w','west']:
        west()    
    else:
        dead("You stumble around the room until you starve.")


#First Floor Rooms

def entrance_hall():
    print entrancehall

    next = raw_input("> ").lower()

    if next in ['n','north']:
        foyer()
    elif next in ['e','east']:
        charred_room()
    elif next in ['s','south']:
        outside()
    elif next in ['w','west']:
        creeky_hall()    
    else:
        dead("You stumble around the room until you starve.")

def foyer():
    print foyerdesc

    next = raw_input("> ").lower()

    if next in ['n','north']:
        grand_stairs()
    elif next in ['e','east']:
        dusty_hall()
    elif next in ['s','south']:
        entrance_hall()
    elif next in ['w','west']:
        grave_yard()    
    else:
        dead("You stumble around the room until you starve.")

def grand_stairs():
    print grandstairs

    next = raw_input("> ").lower()

    if next in ['y','yes']:
        landing()
    else: 
        foyer()

def dusty_hall():
    print dustyhall

    next = raw_input("> ").lower()

    if next in ['n','north']:
        patio()
    elif next in ['e','east']:
        abandoned_room()
    elif next in ['s','south']:
        charred_room()
    elif next in ['w','west']:
        foyer()    
    else:
        dead("You stumble around the room until you starve.")

def abandoned_room():
    print abandonedroom

    next = raw_input("> ").lower()

    if next in ['n','north']:
        kitchen()
    elif next in ['s','south']:
        garden()
    elif next in ['w','west']:
        dusty_hall()    
    else:
        dead("You stumble around the room until you starve.")

def kitchen():
    print kitchendesc

    next = raw_input("> ").lower()

    if next in ['s','south']:
        abandoned_room()
    elif next in ['w','west']:
        patio()  
    else:
        dead("You stumble around the room until you starve.")

def patio():
    print patiodesc

    next = raw_input("> ").lower()

    if next in ['e','east']:
        kitchen()
    elif next in ['s','south']:
        dusty_hall()
    else:
        dead("You stumble around the room until you starve.")

def grave_yard():
    print graveyard

    next = raw_input("> ").lower()

    if next in ['e','east']:
        foyer() 
    else:
        dead("You stumble around the room until you starve.")

def charred_room():
    print charredroom

    next = raw_input("> ").lower()

    if next in ['n','north']:
        dusty_hall()
    elif next in ['w','west']:
        entrance_hall()
    elif next in ['s','south']:
        dining_room()
    elif next in ['e','east']:
        garden()    
    else:
        dead("You stumble around the room until you starve.")

def garden():
    print gardendesc

    next = raw_input("> ").lower()

    if next in ['n','north']:
        abandoned_room()
    elif next in ['s','south']:
        game_room()
    elif next in ['e','east']:
        charred_room()    
    else:
        dead("You stumble around the room until you starve.")

def game_room():
    print gameroom

    next = raw_input("> ").lower()

    if next in ['n','north']:
        garden()
    elif next in ['e','east']:
        conservatory()
    elif next in ['w','west']:
        dining_room()    
    else:
        dead("You stumble around the room until you starve.")

def conservatory():
    print conservatorydesc

    next = raw_input("> ").lower()

    if next in ['w','west']:
        game_room() 
    else:
        dead("You stumble around the room until you starve.")

def dining_room():
    print diningroom

    next = raw_input("> ").lower()

    if next in ['n','north']:
        charred_room()
    elif next in ['e','east']:
        game_room()
    else:
        dead("You stumble around the room until you starve.")

def creeky_hall():
    print creekyhall

    next = raw_input("> ").lower()

    if next in ['w','west']:
        ball_room()
    elif next in ['e','east']:
        entrance_hall() 
    else:
        dead("You stumble around the room until you starve.")

def ball_room():
    print ballroom

    next = raw_input("> ").lower()

    if next in ['s','south']:
        coal_chute()
    elif next in ['e','east']:
        creeky_hall() 
    else:
        dead("You stumble around the room until you starve.")

def coal_chute():
    print coalchute

    basement_landing()

def outside():
    print outsidedesc

    next = raw_input("> ").lower()

    if next in ['y','yes']:
        entrance_hall()
    else: 
        dead("The werewolf catches you and eats you.")

# Second Floor Rooms

def landing():
    print landingdesc

    next = raw_input("> ").lower()

    if next in ['n','north']:
        research_lab()
    elif next in ['e','east']:
        junk_room()
    elif next in ['s','south']:
        foyer() 
    elif next in ['w','west']:
        bloody_room()    
    else:
        dead("You stumble around the room until you starve.")

# Basement Rooms

def basement_landing():
    print basementlanding

    next = raw_input("> ").lower()

    if next in ['n','north']:
        chasm()
    elif next in ['e','east']:
        larder()
    elif next in ['s','south']:
        operating_room()
    elif next in ['w','west']:
        gym()    
    else:
        dead("You stumble around the room until you starve.")
print intro
raw_input ("> ")
outside()
