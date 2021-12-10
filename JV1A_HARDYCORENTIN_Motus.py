#Début du setup et des importations

import random
from colorama import init
init()
from colorama import Fore, Back, Style
print(Style.RESET_ALL)
#Fin du setup et des importations

wordlist = ["banane","algues","bandit","cheval","diurne","danois","zapper","sucrer","valide","robots"]

#Le mot a deviné est choisi au hasard parmis les dix mots disponible.
wordtoguess = wordlist [random.randint(0,9)] 

#Le/La joueur/joueuse n'a que 8 chance pour deviné le mot.
maxchances=8
Defeat = False

#On prépare la variable interactive pour plus tard.
playertry = "0"

#Si le/la joueur/joueuse devine le mot, il/elle gagne.
Victory = playertry == wordtoguess

#Affichage du nombre de lettre du mot
for i in range (len(wordtoguess)):
    print("_",end=" ")
    i= i+1
print("")

#Boucle principale du jeu
while Victory == False and Defeat == False : 
    playertry = input("Try to guess the word knowing that it is the number of underscore's long. ") #Le/La joueur/joueuse essaye de deviner le mot.
    #Vérification du mot donner. On utiliseras wortoguess comme longueur de référence au cas où le/la joueur/joueuse décide de mettre un mot plus long que le mot a deviné. 
    for j in range (len(wordtoguess)) :
        #Calcul de la défaite ou de la victoire
        if playertry == wordtoguess :
            Victory = True
        if maxchances == 0 :
            Defeat = True
        #Si la lettre est dans le mot et bien placée elle s'affichera en rouge.
        if playertry[j] == wordtoguess[j] :
            print(Fore.RED + playertry[j], end="")
            
        
        
        #Si la lettre apparait bien dans le mot, mais est au mauvais endroit, cette dernière s'affichera en jaune.
        elif playertry[j] == wordtoguess[0] or playertry[j] == wordtoguess[1] or playertry[j] == wordtoguess[2] or playertry[j] == wordtoguess[3] or playertry[j] == wordtoguess[4] or playertry[j] == wordtoguess[5] and playertry[j]!= wordtoguess[j] :
            print(Fore.YELLOW + playertry[j],end="")
            
        


        #Si la lettre n'existe pas dans le mot elle sera écrit en bleu.
        elif playertry[j] != wordtoguess[0] or playertry[j] != wordtoguess[1] or playertry[j] != wordtoguess[2] or playertry[j] != wordtoguess[3] or playertry[j] != wordtoguess[4] or playertry[j] != wordtoguess[5]:
            print(Fore.BLUE + playertry[j],end="")
        
        print(Style.RESET_ALL, end="") #On remet la couleur du texte par défaut, pour éviter la confusion du/de la joueur/joueuse.
        maxchances = maxchances - 1
    print("")


#Si le/la joueur/joueuse gagne cela lui sera déclaré. Même chose si le résultat est un échec, cela lui sera déclaré aussi.
if Victory == True :
    print("Well done !")
elif Defeat == True :
    print ("Nice try. Better luck next time !")
                
