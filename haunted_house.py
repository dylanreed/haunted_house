import random
from sys import exit
from rooms import *
from badthings import *
from goodthings import *
import monsters

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
        monsters.dead("You stumble around the room until you starve.")

# Creatures

def monster(type):
    type = random.choice([zombies,no_monster, zombie,no_monster, vampire,no_monster, count_vampire,no_monster, were_wolf,no_monster, slimes, no_monster, cultist])
    #print random.choice(monster)
    #random.choice(type)
    if type == zombies:
        monsters.zombies()
    elif type == zombie:
        monsters.zombie()
    elif type == vampire:
        monsters.vampire()
    elif type == count_vampire:
        monsters.count_vampire()
    elif type == were_wolf:
        monsters.were_wolf()
    elif type == slimes:
        monsters.slimes()
    elif type == cultist:
        monsters.cultist()
    else:
        monsters.no_monster()


#First Floor Rooms

def entrance_hall():
    print entrancehall
    monster(type)

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
        monsters.dead(entrance_hall_death)

def foyer():
    print foyerdesc
    monster(type)
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
        monsters.dead(foyer_death)

def grand_stairs():
    print grandstairs

    next = raw_input("> ").lower()

    if next in ['y','yes']:
        landing()
    else: 
        foyer()

def dusty_hall():
    print dustyhall
    monster(type)
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
        monsters.dead(dusty_hall_death)

def abandoned_room():
    print abandonedroom
    monster(type)
    next = raw_input("> ").lower()

    if next in ['n','north']:
        kitchen()
    elif next in ['s','south']:
        garden()
    elif next in ['w','west']:
        dusty_hall()    
    else:
        monsters.dead(abandoned_room_death)

def kitchen():
    print kitchendesc
    monster(type)
    next = raw_input("> ").lower()

    if next in ['s','south']:
        abandoned_room()
    elif next in ['w','west']:
        patio()  
    else:
        monsters.dead(kitchen_death)

def patio():
    print patiodesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['e','east']:
        kitchen()
    elif next in ['s','south']:
        dusty_hall()
    else:
        monsters.dead(patio_death)

def grave_yard():
    print graveyard
    monster(type)

    next = raw_input("> ").lower()

    if next in ['e','east']:
        foyer() 
    else:
        monsters.dead(grave_yard_death)

def charred_room():
    print charredroom
    monster(type)

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
        monsters.dead(charred_room_death)

def garden():
    print gardendesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        abandoned_room()
    elif next in ['s','south']:
        game_room()
    elif next in ['e','east']:
        charred_room()    
    else:
        monsters.dead(garden_death)

def game_room():
    print gameroom
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        garden()
    elif next in ['e','east']:
        conservatory()
    elif next in ['w','west']:
        dining_room()    
    else:
        monsters.dead(game_room_death)

def conservatory():
    print conservatorydesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['w','west']:
        game_room() 
    else:
        monsters.dead(conservatory_death)

def dining_room():
    print diningroom
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        charred_room()
    elif next in ['e','east']:
        game_room()
    else:
        monsters.dead(dining_room_death)

def creeky_hall():
    print creekyhall
    monster(type)

    next = raw_input("> ").lower()

    if next in ['w','west']:
        ball_room()
    elif next in ['e','east']:
        entrance_hall() 
    else:
        monsters.dead(creeky_hall_death)

def ball_room():
    print ballroom
    monster(type)

    next = raw_input("> ").lower()

    if next in ['s','south']:
        coal_chute()
    elif next in ['e','east']:
        creeky_hall() 
    else:
        monsters.dead(ball_room_death)

def coal_chute():
    print coalchute

    basement_landing()

def outside():
    print outsidedesc

    next = raw_input("> ").lower()

    if next in ['y','yes']:
        entrance_hall()
    else: 
        monsters.dead(outside_death)

# Second Floor Rooms

def landing():
    print landingdesc
    monster(type)

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
        monsters.dead(landing_death)

def research_lab():
    print researchlab
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        vault()
    elif next in ['s','south']:
        landing()   
    else:
        monsters.dead(research_lab_death)

def vault():
    print vaultdesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['s','south']:
        research_lab()   
    else:
        monsters.dead(vault_death)

def junk_room():
    print junkroom
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        bedroom()
    elif next in ['e','east']:
        collapsed_room()
    elif next in ['w','west']:
        landing()    
    else:
        monsters.dead(junk_room_death)

def collapsed_room():
    print collapsedroom
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        balcony()
    elif next in ['w','west']:
        junk_room()  
    else:
        monsters.dead(collapsed_room_death)

def balcony():
    print balconydesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['s','south']:
        collapsed_room()
    else:
        monsters.dead(balcony_death)

def bedroom():
    print bedroomdesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        attic()
    elif next in ['s','south']:
        junk_room()  
    else:
        monsters.dead(bedroom_death)

def attic():
    print atticdesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['s','south']:
        bedroom()  
    else:
        monsters.dead(attic_death)

def bloody_room():
    print bloodyroom
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        tower()
    elif next in ['e','east']:
        landing()
    elif next in ['w','west']:
        library()    
    else:
        monsters.dead(bloody_room)

def library():
    print librarydesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        gallery()
    elif next in ['e','east']:
        bloody_room() 
    else:
        monsters.dead(library_death)

def gallery():
    print gallerydesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        master_bedroom()
    elif next in ['s','south']:
        library()   
    else:
        monsters.dead(gallery_death)

def master_bedroom():
    print masterbedroom
    monster(type)

    next = raw_input("> ").lower()

    if next in ['s','south']:
        library()   
    else:
        monsters.dead(master_bedroom_death)

def tower():
    print towerdesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        chapel()
    elif next in ['s','south']:
        bloody_room()  
    else:
        monsters.dead(tower_death)

def chapel():
    print chapeldesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['s','south']:
        tower()  
    else:
        monsters.dead(chapel_death)

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
        monsters.dead(basement_landing_death)

def gym():
    print gymdesc
    monster(type)

    next = raw_input("> ").lower()


    if next in ['e','east']:
        basement_landing()
    elif next in ['s','south']:
        furnace_room() 
    else:
        monsters.dead(gym_death)
        
def furnace_room():
    print furnaceroom
    monster(type)

    next = raw_input("> ").lower()


    if next in ['e','east']:
        operating_room()
    elif next in ['n','north']:
        gym() 
    elif next in ['w','west']:
        wine_celler()
    else:
        monsters.dead(furnace_room_death)  

def wine_celler():
    print wineceller
    monster(type)

    next = raw_input("> ").lower()


    if next in ['e','east']:
        furnace_room()
    elif next in ['w','west']:
        servants_quarters() 
    else:
        monsters.dead(wine_celler_death) 

def servants_quarters():
    print servantsquarters
    monster(type)

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
        monsters.dead(servants_quarters_death)

def mystic_elevator(): # will teleport player to a random room eventually
    print mysticelevator

    next = raw_input("> ").lower()

    if next in ['n','north']:
        servants_quarters()
    else:
        monsters.dead("You stumble around the room until you starve.")

def pentagram_chamber():
    print pentagramchamber
    monster(type)

    next = raw_input("> ").lower()

    if next in ['e','east']:
        servants_quarters()
    else:
        monsters.dead(pentagram_chamber_death)

def statuary_hall():
    print statuaryhall
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        underground_lake()
    elif next in ['s','south']:
        servants_quarters()   
    else:
        monsters.dead(statuary_hall_death) 

def underground_lake():
    print undergroundlake
    monster(type)

    next = raw_input("> ").lower()

    if next in ['e','east']:
        stairs_to_foyer()
    elif next in ['s','south']:
        statuary_hall()   
    else:
        monsters.dead(underground_lake_death) 

def stairs_to_foyer():
    print stairstofoyer

    next = raw_input("> ").lower()

    if next in ['y','yes']:
        foyer()
    else: 
        underground_lake()

def chasm():
    print chasmdesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        organ_room()
    elif next in ['s','south']:
        basement_landing()  
    else:
        monsters.dead(chasm_death)

def organ_room():
    print organroom
    monster(type)

    next = raw_input("> ").lower()

    if next in ['w','west']:
        store_room()
    elif next in ['s','south']:
        chasm()
    else:
        monsters.dead(organ_room_death)

def store_room():
    print storeroom
    monster(type)

    next = raw_input("> ").lower()

    if next in ['e','east']:
        organ_room()
    else:
        monsters.dead(store_room_death)

def operating_room():
    print operatingroom
    monster(type)

    next = raw_input("> ").lower()

    if next in ['n','north']:
        basement_landing()
    elif next in ['w','west']:
        furnace_room()    
    else:
        monsters.dead(operating_room_death)

def larder():
    print larderdesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['w','west']:
        basement_landing()
    elif next in ['e','east']:
        catacombs()
    else:
        monsters.dead(larder_death)

def catacombs():
    print catacombsdesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['w','west']:
        larder()
    elif next in ['e','east']:
        crypt()
    else:
        monsters.dead(catacombs_death)

def crypt():
    print cryptdesc
    monster(type)

    next = raw_input("> ").lower()

    if next in ['w','west']:
        catacombs()
    else:
        monsters.dead(crypt_death)

def intro():
    print introtext
    raw_input("<Press enter to continue>")
    outside()

#actual gameplay starts here
intro()

