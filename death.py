import haunted_house

#death

def dead(why):
    print why, "Play Again? (y/n)"
    again = raw_input("> ")
    if again in ['y','yes']:
        haunted_house.outside()
    else:
   		exit(0)