
author ='''
projekt_1.py: první projekt do Engeto Online Python Akademie
Martin Blahuš
martinkuf@gmail.com
'''
import string

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#prevedeni textu na casti a vycisteni textu od interpunkce
part_1 = TEXTS[0]
part_1 = [slovo.strip(string.punctuation) for slovo in TEXTS[0].split()]

part_2 = TEXTS[1]
part_2 = [slovo.strip(string.punctuation) for slovo in TEXTS[1].split()]

part_3 = TEXTS[2]
part_3 = [slovo.strip(string.punctuation) for slovo in TEXTS[2].split()]

cara = 40 * '-'
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
    }
#vyzadani uzivatelskeho jmena a hesla plus jeho kontrola
def login():
    username = input('Enter username \n').lower()
    if not username in users: #pokud login nesedi, opakuje zadani loginu
        print('Wrong login')
        return login()
    password = input('Enter Password \n').lower()
    if users[username] == password: # pokud sedi vse, prechazime k vyberu textu
        print(f'Welcome to the app {username}')
        print(cara)
        return choose_text()
    else: #pokud nesedi heslo, opakuje zadani loginu
        print('Wrong password')
        return login()

chosen_text = '' #prazdny list do ktereho pridam vyber uzivatele pro dalsi praci s textem

#vyber textu a vypsani jeho casti
def choose_text():
    print('We have 3 texts to be analyzed.')
    part_chose = input('Enter a number from 1 to 3 to choose a text \n')
    #print(cara)

    if part_chose == '1':
        return part_1
    elif part_chose == '2':
        return part_2
    elif part_chose == '3':
        return part_3
    else:
        print(f'{part_chose} is not correct answer, repeat you choice') #pri spatnem zadani opakuje volbu
        return choose_text()

chosen_text = login()  # uložení vybraného textu po přihlášení a výběru textu

#promenne dat v grafu
pocet_slov = []
prvni_velke = []
cele_velke = []
cele_male = []
pocet_cisel = []


#vyber dat a pridani do prazdnych listu
for word in chosen_text:
    if word.isalpha() or any(char.isdigit() for char in word):
        pocet_slov.append(word)

    if word.istitle():
        prvni_velke.append(word)

    if word.isupper() and word.isalpha():
        cele_velke.append(word)

    if word.islower():
        cele_male.append(word)

    if word.isdigit():
        pocet_cisel.append(int(word))

#soucet cisel        
suma_sumarum = sum(pocet_cisel)

pocet_slov = len(pocet_slov)
prvni_velke = len(prvni_velke)
cele_velke = len(cele_velke)
cele_male = len(cele_male)
pocet_cisel = len(pocet_cisel)

hvezdy_pocet = pocet_slov * '*'
hvezdy_velke = prvni_velke * '*'
hvezdy_VELKE = cele_velke * '*'
hvezdy_male = cele_male * '*'
hvezdy_cisla = pocet_cisel * '*'

print(f'''
{cara}
1. There are {pocet_slov} words in the selected text.
2. There are {prvni_velke} titlecase words.
3. There are {cele_velke} uppercase words.
4. There are {cele_male} lowercase words.
5. There are {pocet_cisel} numeric strings.
The sum of all the numbers {suma_sumarum}.
{cara}
NR.|  OCCURENCES  |LEN
{cara}
  1|{hvezdy_pocet}|{pocet_slov}     
  2|{hvezdy_velke}|{prvni_velke}
  3|{hvezdy_VELKE}|{cele_velke}
  4|{hvezdy_male} |{cele_male}
  5|{hvezdy_cisla}|{pocet_cisel}
''')
