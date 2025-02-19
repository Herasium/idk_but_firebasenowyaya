# 2024_2025__p04_projet2_g11 
Louise Christophe, Eudocie de Khovrine, Marine Fraboulet et Wael Belhaddad

## Outil de Proximité


### Description  
Ce projet est un outil permettant de comparer les éléves entre eux selon leurs informations personnelles. 


### Structure du Projet
**main.py** :
**tools.py** :
**data.py** :
**structure_de_données.py** : 
**index.html** :
**submit.html** :


### Fonctionnalités
Vérifie les entrées valides pour les formats binaire, décimal et hexadécimal.
Convertit les nombres entre :  
- **Binaire** (base "binaire")  
- **Décimal** (base "décimal")  
- **Hexadécimal** (base "hexadécimal")
  
Prise en main simple avec des inputs pour faciliter l’utilisation.


### Prérequis
Python 3.x


### Installation
1. Clonez le repository :   
```
git clone https://github.com/Eudo08/2024_2025__p04_projet1_gp10.git  
cd 2024_2025__p04_projet1_gp10-main
```
2. Assurez-vous que Python est installé. Vous pouvez le télécharger depuis [python.org](python.org).


### Utilisation
1. Lancez le script :  
```
python main.py
```
2. Suivez les instructions pour entrer le nombre initial et sa base, puis choisissez la base souhaité pour la conversion.


### Modules et fonctions
#### data.py :
``bin_dec_hex_valid_text`` : Liste de chaînes de texte indiquant les bases acceptées.  
``bin_valid_chars``, ``dec_valid_chars``, ``hex_valid_chars`` : Listes de caractères valides pour chaque base, utilisées pour la validation des nombres.  
#### tools.py :
Contient les fonctions de conversion, telles que :
``dec_to_bin``, ``dec_to_hex``, ``bin_to_dec``, etc.
Chaque fonction convertit un nombre d'une base à une autre.  
#### main.py :
- **validity_text_base(text)** : Vérifie si le texte saisi correspond à un type de base valide (binaire, décimal ou hexadécimal).

- **are_valid_characters(number, valid_chars)** : Vérifie si chaque caractère du nombre est valide pour la base spécifiée.

- **ask_for_the_init_base()** : Demande à l’utilisateur d’entrer la base du nombre initial (binaire, décimal ou hexadécimal) et vérifie sa validité.

- **ask_for_the_init_number(init_base)** : Demande à l’utilisateur d’entrer le nombre à convertir dans la base initiale. La fonction valide le nombre en fonction des caractères acceptables pour la base sélectionnée.

- **ask_for_the_target_base()** : Demande à l’utilisateur d’entrer la base cible de conversion (binaire, décimal ou hexadécimal) et vérifie sa validité.

- **bin_dec_hex__to__bin_dec_hex(init_number, init_base, target_base)** : Convertit le nombre de la base initiale vers la base cible. En fonction des bases choisies, cette fonction utilise des sous-fonctions telles que dec_to_bin, dec_to_hex, hex_to_bin, etc., pour effectuer la conversion.

- **do_the_job()** : Fonction principale qui gère l'ensemble du processus, depuis la saisie des données jusqu'à la conversion finale et l'affichage du résultat.


### Exemple
Pour convertir le nombre binaire 101 en décimal :

1. Entrez ``101`` lorsqu’on vous demande le nombre initial.
2. Sélectionnez ``2`` comme base initiale (binaire).
3. Sélectionnez ``10`` comme base cible (décimal).
4. Le résultat sera ``5``.


### Contribution
**[M. Pioche](https://github.com/jimpioche)**  : Conception du squelette de base du projet et test de validation.  
**[Louise Christophe](https://github.com/louisechristophe), [Eudocie de Khovrine](https://github.com/Eudo08), [Marine Fraboulet](https://github.com/MAMARINEEE)** : Développement et ajout des fonctionnalités, des validations et des conversions entre bases, ainsi que l'amélioration de la structure générale.  
**ChatGPT** : Assistance pour les corrections de code et structuration du README.

### Licence
Ce projet est sous licence MIT.
