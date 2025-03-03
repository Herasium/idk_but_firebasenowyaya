from random import *
from math import *
from tools_json import load_data

data = load_data()
coef = data.get("coef", {})


def get_dico():
    data = load_data()
    return {
        list(person.keys())[0].strip().lower(): list(person.values())[0]
        for person in data.get("dico", [])
    }


def compare_proximity(people, person):
    dico = get_dico()
    numerateur = 0
    denominateur = 0

    for caracter in dico[people]["info_perso"].keys():
        if dico[person]["info_perso"].get(caracter) == dico[people]["info_perso"].get(
            caracter
        ):
            numerateur += coef.get(caracter, 0)
        denominateur += coef.get(caracter, 0)
    # if denominateur == 0:
    #     return 0.0
    # return round((numerateur / denominateur) * 100, 1)
    if denominateur == 0:
        return 0.0
    compatibilite = (numerateur / denominateur) * 100
    return round(min(100, compatibilite), 1)


def compare_with_different_person(person):
    dico = get_dico()
    person = person.strip().lower()
    dico_compatibilite = {}
    for people in dico.keys():
        if people != person:
            if people in dico and person in dico:
                moyenne = compare_proximity(people, person)
                dico_compatibilite[people] = moyenne
            else:
                print(f"Erreur : Clé '{people}' ou '{person}' non trouvée dans dico")
    return dico_compatibilite


def list_of_compatibilite(person):
    dico_compatibilite = compare_with_different_person(person)
    return list(dico_compatibilite.values())


def list_of_people(person):
    dico_compatibilite = compare_with_different_person(person)
    return list(dico_compatibilite.keys())


def sort_compatibility_between_users(person):
    sort_number = []
    sort_people = []
    list_number = list_of_compatibilite(person)
    list_person = list_of_people(person)
    while list_number:
        max_value = list_number[0]
        max_index = 0
        for i in range(1, len(list_number)):
            if list_number[i] > max_value:
                max_value = list_number[i]
                max_index = i
        sort_number.append(max_value)
        sort_people.append(list_person[max_index])
        list_person.remove(list_person[max_index])
        del list_number[max_index]
    return sort_number, sort_people


def distance_with_people(person):
    sort_distance = []
    sort_number, _ = sort_compatibility_between_users(person)
    _, sort_people = sort_compatibility_between_users(person)
    for i in range(len(sort_number)):
        distance = 100 - sort_number[i]
        sort_distance.append(distance)
    return sort_distance, sort_people


def dico_distance(person):
    dico_distance_person = {}
    sort_distance, sort_people = distance_with_people(person)
    for i in range(len(sort_people)):
        dico_distance_person[sort_people[i]] = sort_distance[i]
    return dico_distance_person


def representation_person_on_plan(person):
    positions = []
    dico_distance_personne = dico_distance(person)
    angleinter = 360 / len(dico_distance_personne)
    angle = 0
    dico = get_dico()
    for people, distance in dico_distance_personne.items():
        coordonnee_x = cos(radians(angle)) * (50 + 160.0 * distance / 100.0)
        coordonnee_y = sin(radians(angle)) * (50 + 160.0 * distance / 100.0)

        positions.append(
            {
                "name": f"{dico[people]['presentation']['prenom']} {dico[people]['presentation']['nom']}",
                "x": coordonnee_x,
                "y": coordonnee_y,
            }
        )
        angle = angle + angleinter

    print(positions)
    return positions


# print("Compatibilité brute :", compare_with_different_person("person_2"))
# print("Distances et personnes :", distance_with_people("person_2"))
# print("Tri des compatibilités :", sort_compatibility_between_users("person_2"))
# print("Dictionnaire des distances :", dico_distance("person_2"))
