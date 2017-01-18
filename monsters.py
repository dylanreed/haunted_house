from badthings import *
from goodthings import *


def no_monster():
    print "This room appears to be empty."

def zombies():
	print zombies 

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
	print zombie 

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
	print vampire 

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
	print count_vampire 

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
	print were_wolf 

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
	print slimes

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
	print cultist 

	attack = raw_input("> ").lower()

	if attack == "sneak":
		dead(cultist_death)
	elif attack == "listen":
		dead(cultist_death)
	elif attack == "bash":
		print cultist_success
	else:
		dead(cultist_death)

def dead(why):
    print why, "Good Job!!"
    exit(0)
