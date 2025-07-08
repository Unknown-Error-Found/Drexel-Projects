#Program: hw03_dialogue.py
#Name: Nabilah Jerin
#Date: January 27, 2025
#Description: The program will first show a set of choices between three different characters.
#The user then can interact with the characters and ask a variety of questions or comments about the town,
#the people, and a potential red-haired guy. The program runs like a videogame dialouge.


#Opening Text and Input From User
print("You arrive outside a new town.")
print("There are three people outside the city walls.")
print("Who would you like to talk to?\n")

print("1. Mel - a girl in a flowered dress.")
print("2. Avarie - a traveling witch from a neighboring city.")
print("3. Conner - a knight patrolling the city walls.")

character = int(input("Enter the option number (1-3):"))



#Mel's Path Opening
def mel():
    return mel

if character == 1:
    print("\nMel: Greetings! Welcome to town.")
    print("How do you respond?")
    print("1. I am on a quest.")
    print("2. Hello. How are you today?")
    print("3. Have you seen a red-haired man in town?")
    print("4. Bye.")
    mel = int(input("Enter the option number (1-4):"))

#Responses for Option 1 (Mel, no options)
if mel == 1:
    print("\nMel: Um...you seem weird. I am leaving")

#Responses for option 2 (Mel, two options)
if mel == 2:
    print("\nMel: I didn't sleep well last night. I saw a scary man checking in at the hotel.")
    print("How do you respond?")
    print("1. That sounds terrible! I hope you are doing ok. He will probably leave soon.")
    print("2. I need to go check on something")
    mel_hotel_man = int(input("Enter the option number (1-2):"))

    if mel_hotel_man == 1: 
        print("\nMel: Thanks. It feels better to know people care.")
        print("How do you respond?")
        print("1. I am traveling to try and protect people from that man")
        print("2. I hope you have a nice day")
        mel_feels_better = int(input("Enter the option number (1-2):"))
    
        if mel_feels_better == 1:
            print("\nMel: Really! This is a lucky charm necklace my mother gave me. Take it, it may help you.")
        else:
            print("\nMel: Have a nice day as well.")
    else:
        print("\nMel: You seem to be in a hurry. I won't keep you. Bye.")
    
#Responses for Option 3 (Mel, two options)
if mel == 3:
    print("\nMel: Was he in a black jacket with a backpack?")
    print("How do you respond")
    print("1. Yes!")
    print("2. No.")
    mel_black_jacket = int(input("Enter the option number (1-2):"))
    
    if mel_black_jacket == 1:
        print("\nMel: He stayed in town last night. The hotel manager might know more.")
    else:
        print("\nMel: that was the only stranger I saw. Sorry. Good Luck.")

#Responses for Option 3 (Mel, no options)
if mel == 4:
    print("\nMel: See you later.")




#Conner's Path Opening [Custom Person 2]
def conner():
    return conner

if character == 3:
    print("\nConner: Greetings, traveler. I am Conner, a knight in this town. How can I help you?")
    print("How do you respond?")
    print("1. I am on a quest")
    print("2. How are you feeling?")
    print("3. Have you seen a red haired man in town?")
    print("4. Bye")
    conner = int(input("Enter the option number (1-4):"))


#Responses for Option 1 (Conner, three options)
    #Includes "One additional path with at least 3 options"
    #Includes "One additional path with at least 3 options"

def conner_choice_one():
    return conner_choice_one
def conner_place_info():
    return conner_place_info

if conner == 1: #additional path 3 options
    print("\nConner: Wow, that's awsome! If you need any kind of assistance, let me know.")
    print("How do you respond?")
    print("1. Thank you for the help!")
    print("2. Have you noticed anything weird in this town?")
    print("3. What's this town like?")
    conner_choice_one = int(input("Enter the option number (1-3):"))

    if conner_choice_one == 1: 
        print("\nConner: No problem, take care!")
    
    if conner_choice_one == 2: 
        print("\nConner: Nothing weird, just suspicious people around these parts. But that's normal around here.")

    if conner_choice_one == 3: #includes additional three different paths
        print("\nConner: This town is truly an amazing place, both for the common people and travelers.")
        print("There are two distinct places, the church and the hotel. Do you wanna know more?")
        print("How do you respond?")
        print("1. Tell me about the Church")
        print("2. Tell me about the Hotel")
        print("3. No thank you.")
        conner_place_info = int(input("Enter the option number (1-3):"))
        
        if conner_place_info == 1:
            print("Conner: The Church is the oldest building here. It's where we pray to our god and wish for prosperity.")
        if conner_place_info == 2:
            print("Conner: The Hotel is the most popular place for travelers, but sketchy people also linger there.")
        if conner_place_info == 3:
            print("Conner: That's fine, have a good day.")


#Responses for Option 2 (Conner)
    #Includes Path 3, 2, 2, 4
def conner_raids():
    return conner_raids
def conner_raids_response():
    return conner_raids_response

if conner == 2:
    print("\nConner: I've been feeling a bit tired, especially with the raids going on.")
    print("How do you respond?")
    print("1. That's unfortunate")
    print("2. Raids? What kind of raids have been happening?")
    conner_raids = int(input("Enter the option number (1-2):"))
    
    if conner_raids == 1:
        print("\nConner: Truly. But fear not, I will never stop protecting the city from harm!")
    if conner_raids == 2:
        print("\nConner: It's nothing for a traveler like you to worry about.")
        print("How do you respond?")
        print("1. I see, then I won't worry about it")
        print("2. How can you say that?! I come to this new town only to find out that I'm in danger?!")
        print("3. I'm part of the group of raiders.")
        print("4. Can you tell me more about these raids?")
        conner_raids_response = int(input("Enter the option number (1-4):"))
        
        if conner_raids_response == 1:
            print("\nConner: Good, I hope you enjoy the rest of your stay here")
        if conner_raids_response == 2:
            print("\nConner: Fear not, traveler, no harm will come to your way when I'm around")
        if conner_raids_response == 3:
            print("\nConner: You look too weak to even hold a sword.")
        if conner_raids_response == 4:
            print("\nConner: We have intel that the raids originated from a mysterious traveler, but we don't know what he looks like")


#Responses for Option 3 (Conner, two options)
    #Includes " One additional path with at least 4 options"
def conner_crow():
    return conner_crow
if conner == 3:
    print("\nConner: Hmm...I think so? Maybe a few days ago. Does he have a pet crow?")
    print("How would you respond?")
    print("1. Yes! Do you know where he went?")
    print("2. No....thats not the right person")
    print("3. Who carries a crow around?")
    print("4. That's my twin brother John")
    
    conner_crow = int(input("Enter the option number (1-4):"))
    
    if conner_crow == 1:
        print("\nConner: Yes, he went to the hotel, but I'm not sure if he's still there.")
    if conner_crow == 2:
        print("\nConner: Oh, I'm sorry. I hope you find them soon!")
    if conner_crow == 3:
        print("\nConner: Some weird people...")
    if conner_crow == 4:
        print("\nConner: Oh wow, you guys look nothing alike.")

#Responses for Option 4 (Conner, no options)
    #Includes Path 3, 4
if conner == 4:
    print("\nConner: Goodbye, I hope you have a great day!")




#Avarie's path Opening [Custom Person One]
def avarie():
    return avarie

if character == 2:
    print("\nAvarie: Hello, traveler. Do you want your fortune told at a price?")
    print("How do you respond?")
    print("1. I am on a quest")
    print("2. How are you feeling?")
    print("3. Have you seen a red haired man in town?") 
    print("4. Bye") 
    avarie = int(input("Enter the option number (1-4):"))

#Responses for Option 1(Avarie)
    #One additional path with at least 2 options 
def avarie_danger():
    return avarie_danger

if avarie == 1:
    print("\nAvarie: I see, traveler. I sense great danger in your joureny ahead.")
    print("How do you respond?")
    print("1. You're just a crazy person who reads tea leaves as a career.")
    print("2. What do you mean by this?")
    avarie_danger = int(input("Enter the option number (1-2):"))
    
    if avarie_danger == 1:
        print("\nAvarie: Think what you want, but you'll see value in my wisdom.")
    if avarie_danger == 2:
        print("\nAvarie: If you continue looking for this red-haired person, you will only hurt yourself.")


#Responses for Option 2(Avarie)
    #Includes Path 2, 2,    1, 4,1
    #Includes Path 2, 2,    1, 3, 1
def avarie_potion():
    return avarie_potion
def avarie_dragon_potion():
    return avarie_dragon_potion
def avarie_potion_help():
    return avarie_potion_help
def avarie_immortal():
    return avarie_immortal

if avarie == 2:
    print("\nAvarie: I don't feel that great, I think the potions are making me light headed.")
    print("How do you respond?")
    print("1. What kind of potions?")
    print("2. Taking potions randomly is very stupid")
    avarie_potion = int(input("Enter the option number (1-2):"))
    
    if avarie_potion == 1:
        print("\nAvarie: The Dragon's Mane Potion, a young man with red hair gave it to me.")
        print("How do you respond?")
        print("1. Why would you drink something like that from a random stranger?!")
        print("2. You do realize those are deadly...right?")
        print("3. How long has it been since you last drank the potion?")
        print("4. Do you even know what you just drank?!")
        avarie_dragon_potion = int(input("Enter the option number (1-4):"))
        
        if avarie_dragon_potion == 1:
            print("\nAvarie: It's not a stranger, I saw him in my visions. I trust that there is nothing wrong with it!")
            
        if avarie_dragon_potion == 2:
            print("\nAvarie: Obviously, I'm not an idiot. I took precautionary measures before drinking it.")
            
        if avarie_dragon_potion == 3:
            print("\nAvarie: I think...since two days ago?")
            print("How do you respond")
            print("1. What?! How are you not dead yet??")
            print("2. I'm taking you to a hospital")
            avarie_potion_help = int(input("Enter the option number (1-2):"))
            
            if avarie_potion_help == 1:
                print("\nAvarie: I'm an expert in magic and potions.")
            if avarie_potion_help == 2:
                print("\nAvarie: No need, I already took care of the harmful components in the potion. ")
                
        if avarie_dragon_potion == 4:
            print("\nAvarie: A potion that grants immortality, obviously!")
            print("How do you repsond?")
            print("1. Are you crazy?! That doesn't grant immortality!")
            print("2. Are you sure you're a sane person?")
            avarie_immortal = int(input("Enter the option (1-2):"))
            
            if avarie_immortal == 1:
                print("\nAvarie: I am, that's why I make a living selling people's fortunes")
            if avarie_immortal == 2:
                print("\nAvarie: Nope! That's why I make a living selling people's fortunes")
      
    if avarie_potion == 2:
        print("\nAvarie: It's for my spiritual awakening. I have to connect to the universe with these potions")


#Responses for Option 3(Avarie)
    #Includes "One additional path with at least 3 options "
    #Includes "One additional path with at least 2 options"
def avarie_red_hair_man():
    return avarie_red_hair_man
def avarie_red_hair_man_2():
    return avarie_red_hair_man_2

if avarie == 3:
    print("\nAvarie: A red haired man? Why are you looking for that strange fella?")
    print("How do you respond?")
    print("1. That guy is my twin brother John!")
    print("2. What did he look like?")
    print("3. Do you know where he went?")
    print("4. Why do you call him strange?")
    avarie_red_hair_man = int(input("Enter the option number (1-4)"))
    
    if avarie_red_hair_man == 1:
        print("\nAvarie: I know, I saw it in my vision. You guys are magnets for disaster.")
    
    if avarie_red_hair_man == 2:
        print("\nAvarie: Besides the obvious, he was wearing a black jacket and had a strange backpack.")
        print("How do you respond?")
        print("1. That's not the right person")
        print("2. Yes, that's the man!")
        avarie_red_hair_man_2 = int(input("Enter the option number (1-2):"))
        
        if avarie_red_hair_man_2 == 1:
            print("\nAvarie: Oh, I'm sorry, I hope you can find him soon.")
        if avarie_red_hair_man_2 == 2:
            print("\nAvarie: In that case, you should head to the Hotel, I saw him go there.")
            
    if avarie_red_hair_man == 3:
        print("\nAvarie:He went to the hotel, I believe. You might have luck finding him there")
    
    if avarie_red_hair_man == 4:
        print("\nAvarie: He had a random crow following him everywhere, for some reason.")
        

#Responses for Option 4 (Avarie)
if avarie == 4:
    print("\nAvarie: Bye traveler. If you need a curse or spell, come visit me anytime!")

