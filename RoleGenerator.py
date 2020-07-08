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
mafSupp = ["Blackmailer", "Consigliere", "Consort"]
covenEvil = ["Coven Leader", "Hex Master", "Medusa", "Necromancer", "Posioner", "Potion Master"]
randomTownie = ["Escort", "Mayor", "Medium", "Retributionist", "Transporter", "Bodyguard", "Doctor", "Crusader", "Trapper","Jailor", "Vampire Hunter", "Veteran", "Vigilante", "Investigator", "Lookout", "Psychic", "Sheriff", "Spy", "Tracker" ]
randomMafia = ["Blackmailer", "Consigliere", "Consort","Ambusher", "Godfather", "Mafioso", "Disguiser", "Forger", "Framer", "Hypnotist", "Janitor"]
roleCategories = ["Town Investigative", "Town Killing", "Town Protective", "Town Support", "Neutral Benign", "Neutral Chaos", "Neutral Evil", "Neutral Killing", "Mafia Deception", "Mafia Killing", "Mafia Support", "Coven Roles" ]
rPreset = ["Jailor","Town Investigative", "Town Investigative", "Town Protective", "Town Killing", "Town Support", "Random Town", "Random Town", "Random Town", "Godfather", "Mafioso", "Random Mafia", "Random Mafia", "Neutral Evil", "Neutral Killing"]


def rolelistgeneration(roleList):
    finalRoles = [] ## find relevant list and put it through function roll
    count = 1
    for count in range(len(roleList)):
        chosenCategory = roleList[(count - 1)]
        if chosenCategory == "Town Investigative" or chosenCategory == "1":
            finalRoles = roll(townInv, finalRoles)
        elif chosenCategory == "Town Protective" or chosenCategory == "3":
            finalRoles = roll(townProt, finalRoles)
        elif chosenCategory == "Town Support" or chosenCategory == "4":
            finalRoles = roll(townSupp, finalRoles)    
        elif chosenCategory == "Town Killing" or chosenCategory == "2":
            finalRoles = roll(townKill, finalRoles)  
        elif chosenCategory == "Neutral Benign" or chosenCategory == "5":
            finalRoles = roll(neutBen, finalRoles)        
        elif chosenCategory == "Neutral Evil" or chosenCategory == "7":
            finalRoles = roll(neuEvil, finalRoles)       
        elif chosenCategory == "Neutral Killing" or chosenCategory == "8":
            finalRoles = roll(neuKill, finalRoles)
        elif chosenCategory == "Neutral Chaos" or chosenCategory == "6":
            finalRoles = roll(townProt, finalRoles)       
        elif chosenCategory == "Mafia Deception" or chosenCategory == "9":
            finalRoles = roll(mafDec, finalRoles)  
        elif chosenCategory == "Mafia Killing" or chosenCategory == "10":
            finalRoles = roll(mafKill, finalRoles)  
        elif chosenCategory == "Mafia Support" or chosenCategory == "11":
            finalRoles = roll(mafSupp, finalRoles)  
        elif chosenCategory == "Coven" or chosenCategory == "12":
            finalRoles = roll(covenEvil, finalRoles) 
        elif chosenCategory == "Random Town" or chosenCategory == "13":
            finalRoles = roll(randomTownie, finalRoles)
        elif chosenCategory == "Random Mafia" or chosenCategory == "14":
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
            if (covenGame == False) and (proposedRole == ("Psychic")):
                validRole = False
            else:
                if proposedRole in dlcRoles or proposedRole == "Vampire Hunter":
                    validRole = False
                else: 
                    validRole = True

        
        
    finalRoles.append(proposedRole)
    return finalRoles





print (" Welcome to the Role Generator!")
print (" Currently, this version only works with 15 players.")
print (" Please type a number/letter that corresponds to an option, or type in a Role you would like specifically. If you make a typo, you can remove the last item on the list: ")
print ("1. Town Investigative")
print ("2. Town Killing")
print ("3. Town Protective")
print ("4. Town Support")
print ("5. Neutral Benign")
print ("6. Neutral Chaos")
print ("7. Neutral Evil")
print ("8. Neutral Killing")
print ("9. Mafia Deception")
print ("10. Mafia Killing")
print ("11. Mafia Support")
print ("12. Coven Evil")
print ("13. Random Town")
print ("14. Random Mafia")
print ("enter d if you are done, x to remove the last item from the list, RP for the ranked preset list, and status if you would like to be told the list currently")
print ("IT IS CASE SENSITIVE")
choice = ""
count = 1
roleList = []
numberOfCoven = 0
covenGame = False

while choice != "d" and (count != 15):
    choice = input()
    if choice == "x":
        if roleList == []:
            print ("List is already empty.")
        else:
            del roleList[-1]
            print ("Removed!")
            if choice == "12" or  (choice in covenEvil):
                numberOfCoven == numberOfCoven - 1
                if numberOfCoven == 0:
                    covenGame = False
    elif choice == "RP" or choice == "rp":
        
        roleList = rPreset
        choice = "d"
    elif choice == "status":
        print (roleList)
    elif choice == "d":
        break
    else:
        if choice == "12" or  (choice in covenEvil):
            if numberOfCoven == 5:
                print ("Too many Coven, please pick a different role!")
            else: 
                numberOfCoven = numberOfCoven + 1
                covenGame = True
        
        roleList.append(choice)
        print("Choice added, type d if you are done!")
        count = count + 1


finalRoles = rolelistgeneration(roleList)
print (finalRoles)
random.shuffle(finalRoles)
count = 0
for count in range(len(finalRoles)):
    print (str(count + 1) + ". " + finalRoles[(count - 1)])
print ("End of program")