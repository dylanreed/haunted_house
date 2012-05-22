from badthings import *
from goodthings import *
import start 



def no_monster():
    print "This room appears to be empty."

def zombies():
	print """"BRAAIIINNSSS!! Oh crap, it is a group of three zombies.
You can RUN around them, SNEAK around them or BASH their heads in.What 
do you do?"""

	attack = raw_input("> ").lower()

	if attack == "sneak":
	    print zombies_success
	elif attack == "run":
	    dead(zombies_death)
	elif attack == "bash":
	    dead(zombies_death)
	else:
		dead(zombies_death)

def zombie():
	print """BRAAIIINSSS!! A single zombie blocks your path. 
You can RUN around him, SNEAK around him or BASH his head. What 
do you do?"""

	attack = raw_input("> ").lower()

	if attack == "sneak":
	    dead(zombie_death)
	elif attack == "run":
	    dead(zombie_death)
	elif attack == "bash":
		print zombie_success
	else:
		dead(zombie_death)

def vampire():
	print """There is a man standing in your way. He turns towards you 
and you notice a red gleam in his eyes and that his teeth are pointy. 
It's a Vampire. Do you stab him with a STAKE, use your CROSS or RUN away?"""

	attack = raw_input("> ").lower()

	if attack == "stake":
		dead(vampire_death)
	elif attack == "run":
		dead(vampire_death)
	elif attack == "cross":
		print vampire_success
	else:
		dead(vampire_death)

def count_vampire():
	print """There is a man standing in this room. Is he wearing a cape? 
Oh man, it's the Count. You can stab him with your STAKE, use your CROSS,
RUN away or use BOTH your cross and stake. What do you do?"""

	attack = raw_input("> ").lower()

	if attack == "stake":
		dead(count_vampire_death)
	elif attack == "run":
		dead(count_vampire_death)
	elif attack == "cross":
		dead(count_vampire_death)    
	elif attack == "both":
		print count_vampire_success
	else:
		dead(count_vampire_death)

def were_wolf():
	print """You hear growling as you enter the room and quickly notice 
that you are not alone. You wouldn't say that it is a wolf... but it 
also isn't a man. It's a werewolf. You can SHOOT him with a silver 
bullet, RUN away, try to SNEAK by or BASH him in the head. What do you do?"""

	attack = raw_input("> ").lower()

	if attack == "shoot":
		dead(were_wolf_gun_death)
	elif attack == "run":
		dead(were_wolf_death)
	elif attack == "sneak":
		dead(were_wolf_death)    
	elif attack == "bash":
		print were_wolf_success
	else:
		dead(were_wolf_death)

def slimes():
	print """Ewwwwwwww!!! Is that jello? Nope it is a group of slimes. 
Don't let them touch you. Do you STEP on them, SMASH them or AVOID them?"""

	attack = raw_input("> ").lower()

	if attack == "step":
		dead(slimes_death)
	elif attack == "smash":
		dead(slimes_death)
	elif attack == "avoid":
		print slimes_success
	else:
		dead(slimes_death)

def cultist():
	print """This room has a dude in a robe who is chanting some gibberish. 
Is that a knife in his hand? You can SNEAK past him, LISTEN to him or 
BASH him in the head. What do you do?"""

	attack = raw_input("> ").lower()

	if attack == "sneak":
		dead(cultist_death)
	elif attack == "listen":
		dead(cultist_death)
	elif attack == "bash":
		print cultist_success
	else:
		dead(cultist_death)

#death

def dead(why):
    print why, "Play Again? (y/n)"
    again = raw_input("> ")
    if again in ['y','yes']:
    	print"monkies"
        start.start()
    else:
   		exit(0)

    
