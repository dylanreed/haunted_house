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

def research_lab():
    print researchlab

    next = raw_input("> ").lower()

    if next in ['n','north']:
        vault()
    elif next in ['s','south']:
        landing()   
    else:
        dead("You stumble around the room until you starve.")

def vault():
    print vaultdesc

    next = raw_input("> ").lower()

    if next in ['s','south']:
        research_lab()   
    else:
        dead("You stumble around the room until you starve.")

def junk_room():
    print junkroom

    next = raw_input("> ").lower()

    if next in ['n','north']:
        bedroom()
    elif next in ['e','east']:
        collapsed_room()
    elif next in ['w','west']:
        landing()    
    else:
        dead("You stumble around the room until you starve.")

def collapsed_room():
    print collapsedroom

    next = raw_input("> ").lower()

    if next in ['n','north']:
        balcony()
    elif next in ['w','west']:
        junk_room()  
    else:
        dead("You stumble around the room until you starve.")

def balcony():
    print balconydesc

    next = raw_input("> ").lower()

    if next in ['s','south']:
        collapsed_room()
    else:
        dead("You stumble around the room until you starve.")

def bedroom():
    print bedroomdesc

    next = raw_input("> ").lower()

    if next in ['n','north']:
        attic()
    elif next in ['s','south']:
        junk_room()  
    else:
        dead("You stumble around the room until you starve.")

def attic():
    print atticdesc

    next = raw_input("> ").lower()

    if next in ['s','south']:
        bedroom()  
    else:
        dead("You stumble around the room until you starve.")

def bloody_room():
    print bloodyroom

    next = raw_input("> ").lower()

    if next in ['n','north']:
        tower()
    elif next in ['e','east']:
        landing()
    elif next in ['w','west']:
        library()    
    else:
        dead("You stumble around the room until you starve.")

def library():
    print librarydesc

    next = raw_input("> ").lower()

    if next in ['n','north']:
        gallery()
    elif next in ['e','east']:
        bloody_room() 
    else:
        dead("You stumble around the room until you starve.")

def gallery():
    print gallerydesc

    next = raw_input("> ").lower()

    if next in ['n','north']:
        master_bedroom()
    elif next in ['s','south']:
        library()   
    else:
        dead("You stumble around the room until you starve.")

def master_bedroom():
    print masterbedroom

    next = raw_input("> ").lower()

    if next in ['s','south']:
        library()   
    else:
        dead("You stumble around the room until you starve.")

def tower():
    print towerdesc

    next = raw_input("> ").lower()

    if next in ['n','north']:
        chapel()
    elif next in ['s','south']:
        bloody_room()  
    else:
        dead("You stumble around the room until you starve.")

def chapel():
    print chapeldesc

    next = raw_input("> ").lower()

    if next in ['s','south']:
        tower()  
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

def gym():
    print gymdesc

    next = raw_input("> ").lower()


    if next in ['e','east']:
        basement_landing()
    elif next in ['s','south']:
        furnace_room() 
    else:
        dead("You stumble around the room until you starve.")
        
def furnace_room():
    print furnaceroom

    next = raw_input("> ").lower()


    if next in ['e','east']:
        operating_room()
    elif next in ['n','north']:
        gym() 
    elif next in ['w','west']:
        wine_celler()
    else:
        dead("You stumble around the room until you starve.")  

def wine_celler():
    print wineceller

    next = raw_input("> ").lower()


    if next in ['e','east']:
        furnace_room()
    elif next in ['w','west']:
        servants_quarters() 
    else:
        dead("You stumble around the room until you starve.") 

def servants_quarters():
    print servantsquarters

    next = raw_input("> ").lower()

    if next in ['n','north']:
        statuary_hall()
    elif next in ['e','east']:
        wine_celler()
    elif next in ['s','south']:
        mystic_elevator()
    elif next in ['w','west']:
        pentagram_chamber()    
    else:
        dead("You stumble around the room until you starve.")

def mystic_elevator(): # will teleport player to a random room eventually
    print mysticelevator

    next = raw_input("> ").lower()

    if next in ['n','north']:
        servants_quarters()
    else:
        dead("You stumble around the room until you starve.")

def pentagram_chamber():
    print pentagramchamber

    next = raw_input("> ").lower()

    if next in ['e','east']:
        servants_quarters()
    else:
        dead("You stumble around the room until you starve.")

def statuary_hall():
    print statuaryhall

    next = raw_input("> ").lower()

    if next in ['n','north']:
        underground_lake()
    elif next in ['s','south']:
        servants_quarters()   
    else:
        dead("You stumble around the room until you starve.") 

def underground_lake():
    print undergroundlake

    next = raw_input("> ").lower()

    if next in ['e','east']:
        stairs_to_foyer()
    elif next in ['s','south']:
        statuary_hall()   
    else:
        dead("You stumble around the room until you starve.") 

def stairs_to_foyer():
    print stairstofoyer

    next = raw_input("> ").lower()

    if next in ['y','yes']:
        foyer()
    else: 
        underground_lake()

def chasm():
    print chasmdesc

    next = raw_input("> ").lower()

    if next in ['n','north']:
        organ_room()
    elif next in ['s','south']:
        basement_landing()  
    else:
        dead("You stumble around the room until you starve.")

def organ_room():
    print organroom

    next = raw_input("> ").lower()

    if next in ['w','west']:
        store_room()
    elif next in ['s','south']:
        chasm()
    else:
        dead("You stumble around the room until you starve.")

def store_room():
    print storeroom

    next = raw_input("> ").lower()

    if next in ['e','east']:
        organ_room()
    else:
        dead("You stumble around the room until you starve.")

def operating_room():
    print operatingroom

    next = raw_input("> ").lower()

    if next in ['n','north']:
        basement_landing()
    elif next in ['w','west']:
        furnace_room()    
    else:
        dead("You stumble around the room until you starve.")

def larder():
    print larderdesc

    next = raw_input("> ").lower()

    if next in ['w','west']:
        basement_landing()
    elif next in ['e','east']:
        catacombs()
    else:
        dead("You stumble around the room until you starve.")

def catacombs():
    print catacombsdesc

    next = raw_input("> ").lower()

    if next in ['w','west']:
        larder()
    elif next in ['e','east']:
        crypt()
    else:
        dead("You stumble around the room until you starve.")

def crypt():
    print cryptdesc

    next = raw_input("> ").lower()

    if next in ['w','west']:
        catacombs()
    else:
        dead("You stumble around the room until you starve.")

#death
def dead(why):
    print why, "Good Job!!"
    exit(0)

#actual gameplay starts here
#print logo

print intro
raw_input ("> ")
outside()
