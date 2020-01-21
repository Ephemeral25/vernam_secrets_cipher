#_____________________________________________________________________
#-----------------------VERNAM CIPHER in Python-----------------------
#----------author: Clément Demolliere---------------------------------
# Based on secrets module, designed to be Python’s de facto module for
# generating secure random numbers, bytes, and strings
#_____________________________________________________________________
#____________________________DEPENDENCIES_____________________________
#_____________________________________________________________________

import secrets
import string
from time import sleep

#_____________________________________________________________________
#_____________________________FUNCTIONS_______________________________
#_____________________________________________________________________


#Comme son nom l'indique, un dormeur :)
def sleeper():
    for i in range(1, 6):
        print(str(i) + "...")
        sleep(1)


#Transforme une lettre uppercase ascii en sa position dans l'alphabet
def ascii_to_alphabet_int(value):
    return ord(value) - 64


#_____________________________________________________________________
#______________________________SCRIPT_________________________________
#_____________________________________________________________________

info = False
key = []
cipher = []
#Création de l'instance de la classe SystemRandom du module 'secrets'
secretsGenerator = secrets.SystemRandom()
#Création de notre alphabet
alphabet = list(string.ascii_uppercase)

print(
    "Utiliser Ctrl+C afin d'activer le mode [INFO] pour suivre le processus de chiffrement. Sinon attendez 5sec..."
)
try:
    sleeper()
except KeyboardInterrupt:
    info = True
    print('\n\nLe mode [INFO] a été activé!\n\n')

#On converti l'input attendu en majuscule et on la nettoie
stringToCipher = input("Entrez votre message à chiffrer :\n").upper().replace(
    " ", "")
if (info):
    print("Chaîne de caractères nettoyé :\n", *stringToCipher)

#Création de notre clé
while (len(key) != len(stringToCipher)):
    #On mélange notre alphabet
    secretsGenerator.shuffle(alphabet)
    #On choisit aléatoirement notre lettre
    key.append(secretsGenerator.choice(alphabet))
    if (info):
        print("\n", len(key), " iteration.\Après shuffle: ")
        print(*alphabet)
        print(key[len(key) - 1], " sera un élément de la clé!\n")

#Création de notre cipher
for i in range(len(key)):
    a = ascii_to_alphabet_int(stringToCipher[i])
    b = ascii_to_alphabet_int(key[i])
    cipher.append(chr((a + b) % 26 + 64))
    if (info):
        print(stringToCipher[i], " ", key[i], " ", cipher[i])
        print(
            ascii_to_alphabet_int(stringToCipher[i]), " ",
            ascii_to_alphabet_int(key[i]), " ", cipher[i])

#Fin de traitement - affichage de la clé et du cipher
print("\n\nCipher: ", *cipher)
print("Key: ", *key)
