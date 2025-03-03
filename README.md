# lndb_proximite_sans_firebase
# 2024_2025__p04_projet2_g11
Louise Christophe, Eudocie de Khovrine, Marine Fraboulet et Wael Belhaddad

## __Outil de Proximité__


### Description  
Ce projet est un outil permettant de comparer les éléves entre eux selon leurs informations personnelles. 


### Structure du Projet
**styleprincipalv3.css** : Fichier portant sur le style de la page du site.  
**index.html** : Ficher portant sur la structure de la première page du site.  
**submit.html** : Ficher portant sur la structure de la seconde page du site. 
**data.json** : Fichier contennant les informations de l'utilisateur.  
**routes.py** : Fichier enregistrant les donées rentrée par l'utilisateur.  
**compare_proximity.py** : Fichier contennant toutes les fonctions qui permettent de comparer par des calculs les données d'un utilisateur.


### Fonctionnalités
Récupère les données d'un utilisateur.  
Les regroupe avec celles de d'autres utilisateurs enregistrées précedemment.  
Compare les utilisateur entre eux selon leurs informations.


### Prérequis
Python 3.x  
Flask


### Installation
1. Clonez le repository :   
```
https://github.com/Eudo08/2024_2025__lndb_proximite.git
```
2. Assurez-vous que Python est installé. Vous pouvez le télécharger depuis [python.org](python.org).

3. Installez à partir du terminal Flask et Firebase admin.


### Utilisation
1. Ouvrez le site en lançant :
```
python interface_quest_actual_version.py
```
2. Vous pouvez ainsi acceder au site à partir du lien se trouvant dans le terminal.
3. Suivez les instructions, rentrez et envoyez vos données afin d'obtenir le classement.


### Modules et fonctions
#### interface_quest_actual_version.py :
``save_info`` : Enregistre les données de l'utilisateur dans la base de données firebase.
``submit_and_verify`` : Vérifie que l'utilisateur ait bien rempli tous les champs du site.  
#### main.py :
``get_nom``, ``get_prenom``, ``get_info_perso``... : Récupère les informations de la base de données pour les fonctions de comparaison. 
``compare_proximity`` : Récupère les données de deux utilisateurs afin d'obtenir un chiffre selon leur point cummun.


### Exemple
1. Répondez aux questions du site. ``couleur préférée : rouge``
2. Choisissez les informations qui sont pour les plus pertinantes lors de la comparaison avec les autres utilisateurs. ``Plus vous avancez le curceur, plus cette caractéristique est importante pour le classement``
3. Envoyez vos données, appuyez sur ``Envoyer``
4. Vous obtenez un classement des personnes les plus proches de vous ainsi qu'une carte afin de visualiser le résultat des calculs. ``Plus la personne se trouve proche de vous, plus vous avez des caractéristiques en commun.``

### Contribution
**[Louise Christophe](https://github.com/louisechristophe), [Eudocie de Khovrine](https://github.com/Eudo08), [Marine Fraboulet](https://github.com/MAMARINEEE), [Wael Belhaddad](https://github.com/WaelBELHADDAD)** : Développement du projet, création des fonctions et de l'interface sous forme de site hebergé sur l'ordinateur.  
**ChatGPT** : Assistance pour les corrections de code.

### Licence
Ce projet est sous licence MIT.
