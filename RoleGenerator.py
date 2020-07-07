import math
import random
uniqueRoles = ["Jailor", "Mayor", "Retributionist", "Veteran", "Godfather", "Mafioso", "Ambusher", "Juggernaut", "Plaguebearer", "Pestilence", "Pirate", "Werewolf", "Coven Leader", "Necromancer", "Medusa", "Posioner", "Hex Master", "Potion Master"]

dlcRoles = ["Ambusher", "Hypnotist", "Coven Leader", "Hex Master", "Medusa", "Necromancer", "Posioner", "Potion Master", "Guardian Angel", "Juggernaut", "Pirate", "Plaguebearer", "Crusader", "Tracker", "Trapper"]

townInv = ["Investigator", "Lookout", "Psychic", "Sheriff", "Spy", "Tracker"]
townKill = ["Jailor", "Vampire Hunter", "Veteran", "Vigilante"]
townProt = ["Bodyguard", "Doctor", "Crusader", "Trapper"]
townSupp = ["Escort", "Mayor", "Medium", "Retributionist", "Transporter"]
neutBen = ["Amnesiac", "Guardian Angel", "Survivor"]
neutChao = ["Pirate", "Plaguebearer", "Vampire"]
neuEvil = ["Executioner", "Jester", "Witch"]
neuKill = ["Arsonist", "Juggernaut", "Serial Killer", "Werewolf"]
mafDec = ["Disguiser", "Forger", "Framer", "Hypnotist", "Janitor"]
mafKill = ["Ambusher", "Godfather", "Mafioso"]
mafSupp = ["Blackmailer", "Consiglier", "Consort"]
covenRoles = ["Coven Leader", "Hex Master", "Medusa", "Necromancer", "Posioner", "Potion Master"]
randomTownie = ["Escort", "Mayor", "Medium", "Retributionist", "Transporter", "Bodyguard", "Doctor", "Crusader", "Trapper","Jailor", "Vampire Hunter", "Veteran", "Vigilante", "Investigator", "Lookout", "Psychic", "Sheriff", "Spy", "Tracker" ]
randomMafia = ["Blackmailer", "Consiglier", "Consort","Ambusher", "Godfather", "Mafioso", "Disguiser", "Forger", "Framer", "Hypnotist", "Janitor"]
roleCategories = ["Town Investigative", "Town Killing", "Town Protective", "Town Support", "Neutral Benign", "Neutral Chaos", "Neutral Evil", "Neutral Killing", "Mafia Deception", "Mafia Killing", "Mafia Support", "Coven Roles" ]





rPreset = ["Jailor","Town Investigative", "Town Investigative", "Town Protective", "Town Killing", "Town Support", "Random Town", "Random Town", "Random Town", "Godfather", "Mafioso", "Random Mafia", "Random Mafia", "Neutral Evil", "Neutral Killing"]
roleList = rPreset




def rolelistgeneration(roleList):
    finalRoles = [] ## find relevant list and put it through function roll
    for count in range(15):
        chosenCategory = roleList[(count - 1)]
        if chosenCategory == "Town Investigative" or chosenCategory == 1:
            finalRoles = roll(townInv, finalRoles)
        elif chosenCategory == "Town Protective":
            finalRoles = roll(townProt, finalRoles)
        elif chosenCategory == "Town Support":
            finalRoles = roll(townSupp, finalRoles)    
        elif chosenCategory == "Town Killing":
            finalRoles = roll(townKill, finalRoles)  
        elif chosenCategory == "Neutral Benign":
            finalRoles = roll(neutBen, finalRoles)        
        elif chosenCategory == "Neutral Evil":
            finalRoles = roll(neuEvil, finalRoles)       
        elif chosenCategory == "Neutral Killing":
            finalRoles = roll(neuKill, finalRoles)
        elif chosenCategory == "Neutral Chaos":
            finalRoles = roll(townProt, finalRoles)       
        elif chosenCategory == "Mafia Deception":
            finalRoles = roll(mafDec, finalRoles)  
        elif chosenCategory == "Mafia Killing":
            finalRoles = roll(mafKill, finalRoles)  
        elif chosenCategory == "Mafia Support":
            finalRoles = roll(mafSupp, finalRoles)  
        elif chosenCategory == "Coven":
            finalRoles = roll(covenRoles, finalRoles) 
        elif chosenCategory == "Random Town":
            finalRoles = roll(randomTownie, finalRoles)
        elif chosenCategory == "Random Mafia":
            finalRoles = roll(randomMafia, finalRoles)
        else:
            if (chosenCategory in finalRoles ) and (chosenCategory in uniqueRoles):
                if chosenCategory in randomTownie:
                    finalRoles = roll(randomTownie, finalRoles)
                    print("Replaced " + str(chosenCategory) + "with a random town role as it is unique but already in the list!")
                if chosenCategory in randomMafia:
                    finalRoles = roll(randomMafia, finalRoles)
                    print("Replaced " + str(chosenCategory) + "with a random mafia role as it is unique but already in the list!")
            else:
                finalRoles.append(chosenCategory)
    ##Loop
    return finalRoles

    


def roll(chosenCategory, finalRoles):
    validRole = False

    while validRole == False:
        proposedRole = random.choice(chosenCategory)

        if (proposedRole in finalRoles) and (proposedRole in uniqueRoles):
            validRole = False
        else:
            validRole = True
        
    finalRoles.append(proposedRole)
    return finalRoles

finalRoles = rolelistgeneration(rPreset)
print (finalRoles)
random.shuffle(finalRoles)

print (finalRoles)
print ("End of program")