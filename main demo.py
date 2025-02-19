
from  random import *
from math import *
import json
from interface.interface_quest_actual_version import *

data = load_data()

dico = data['dico']
coef = data['coef']
dico_compatibilite = {}

def compare_proximity (people, person):
    numerateur = 0
    denominateur = 0
    if dico [people]["info_perso"] == dico[person]["info_perso"]:
        pass
    else:
        for caracter in dico[people]["info_perso"].keys ():
            if dico [person]['info_perso'][caracter] == dico [people]['info_perso'][caracter]:
                numerateur = numerateur + coef[caracter]
            denominateur = denominateur + coef[caracter]
        moyenne = round ((numerateur/denominateur)*100,1)
    return moyenne



def compare_with_different_person (person):
    dico_compatibilite [person] = {}
    for people in dico.keys() :
        if dico [people]["info_perso"] == dico[person]["info_perso"]:
            pass
        else:
            moyenne = compare_proximity (people,person)
            dico_compatibilite [person][people] = moyenne
    return dico_compatibilite


def list_of_compatibilite (person):
    list_compatibility_number = []
    dico_compatibilite = compare_with_different_person (person)
    for values in dico_compatibilite[person].keys ():
        compatibility = dico_compatibilite[person][values]
        list_compatibility_number. append (compatibility)
    return list_compatibility_number



def list_of_people (person):
    list_compatibility_person = []
    dico_compatibilite = compare_with_different_person (person)
    for values in dico_compatibilite[person].keys ():
        list_compatibility_person. append (values)
    return list_compatibility_person



def sort_compatibility_between_users (person):
    sort_number = []
    sort_people = []
    list_number = list_of_compatibilite (person)
    list_person = list_of_people (person)
    while list_number:
        max_value = list_number[0] 
        max_index = 0 
        for i in range(1, len(list_number)):
            if list_number[i] > max_value:
                max_value = list_number[i]
                max_index = i
        sort_number.append(max_value)
        sort_people. append (list_person[max_index])
        list_person.remove (list_person[max_index])
        del list_number[max_index]
    return sort_number, sort_people



def distance_with_people (person):
    sort_distance = []
    sort_number, _ = sort_compatibility_between_users (person)
    _ , sort_people = sort_compatibility_between_users (person)
    for i in range (len(sort_number)):
        distance = 100 - sort_number[i]
        sort_distance.append (distance)
    return sort_distance, sort_people



def dico_distance (person):
    dico_distance_person = {}
    sort_distance, sort_people = distance_with_people (person)
    for i in range (len(sort_people)):
        dico_distance_person [sort_people[i]] = sort_distance [i]
    return dico_distance_person


def representation_person_on_plan (person):
    dico_distance_personne = dico_distance (person)
    for people in dico_distance_personne.keys():
        hypothenuse = dico_distance_personne[people]
        angle = randint(0,90)
        quadrant = randint (1,4)
        coordonnee_x = (cos (angle))*(hypothenuse)

representation_person_on_plan("person_2")

print(dico_compatibilite)
print(distance_with_people("person_2"))
print(sort_compatibility_between_users("person_2"))
print(dico_distance("person_2"))

# coefficiant pr chaque parametre
# l'eleve choisi combien compte chaque coefficiant
# il y a des profils avec des coeff determinés
# calcul de distance