from random import *
from math import *
from tools_json import load_data

# Charger les données initiales et les coefficients
data = load_data()
coef = data.get("coef", {})


# Fonction pour récupérer le dictionnaire des personnes
def get_dico():
    data = load_data()
    return {
        list(person.keys())[0].strip().lower(): list(person.values())[0]
        for person in data.get("dico", [])
    }


# Comparer la proximité de deux personnes selon leurs caractéristiques personnelles
def compare_proximity(people, person):
    dico = get_dico()
    numerateur = 0
    denominateur = 0

    # Pour chaque caractéristique personnelle, comparer les valeurs et ajouter à la somme selon le coefficient
    for caracter in dico[people]["info_perso"].keys():
        if dico[person]["info_perso"].get(caracter) == dico[people]["info_perso"].get(caracter):
            numerateur += coef.get(caracter, 0)
        denominateur += coef.get(caracter, 0)

    if denominateur == 0:
        return 0.0
    # Calculer la compatibilité sous forme de pourcentage
    compatibilite = (numerateur / denominateur) * 100
    return round(min(100, compatibilite), 1)


# Comparer la compatibilité entre une personne et toutes les autres
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


# Retourne la liste des compatibilités d'une personne avec toutes les autres
def list_of_compatibilite(person):
    dico_compatibilite = compare_with_different_person(person)
    return list(dico_compatibilite.values())


# Retourne la liste des noms des autres personnes avec lesquelles une comparaison a été effectuée
def list_of_people(person):
    dico_compatibilite = compare_with_different_person(person)
    return list(dico_compatibilite.keys())


# Trier les personnes par compatibilité avec une personne donnée
def sort_compatibility_between_users(person):
    sort_number = []
    sort_people = []
    list_number = list_of_compatibilite(person)
    list_person = list_of_people(person)

    # Tri des compatibilités par ordre décroissant
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


# Calculer la "distance" (l'inverse de la compatibilité) entre une personne et toutes les autres
def distance_with_people(person):
    sort_distance = []
    sort_number, _ = sort_compatibility_between_users(person)
    _, sort_people = sort_compatibility_between_users(person)

    # Calculer la distance en soustrayant la compatibilité de 100
    for i in range(len(sort_number)):
        distance = 100 - sort_number[i]
        sort_distance.append(distance)

    return sort_distance, sort_people


# Créer un dictionnaire des distances entre une personne et les autres
def dico_distance(person):
    dico_distance_person = {}
    sort_distance, sort_people = distance_with_people(person)

    # Associer chaque personne à sa distance calculée
    for i in range(len(sort_people)):
        dico_distance_person[sort_people[i]] = sort_distance[i]

    return dico_distance_person


# Représenter la position d'une personne sur un plan en fonction de ses distances avec les autres
def representation_person_on_plan(person):
    positions = []
    dico_distance_personne = dico_distance(person)
    angleinter = 360 / len(dico_distance_personne)
    angle = 0
    dico = get_dico()

    # Calculer les coordonnées x, y de chaque personne sur le plan en fonction de la distance
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

<<<<<<< HEAD
    print(positions) 
    return positions

=======
    
    return positions
>>>>>>> cf05df3594fdfd0aa35e67234ef9b8d2a1b6b563
