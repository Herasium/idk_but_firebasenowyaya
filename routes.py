from flask import Flask, render_template, request, redirect, url_for, flash
import json
from tools_json import load_data, save_data
from compare_proximity import compare_with_different_person

site = Flask(__name__)
site.secret_key = "secret_key_for_flashing"
 

FILE_PATH = 'data.json'

@site.route("/")
def bonjour() : 
    return render_template("index.html")

@site.route("/submit", methods=["POST", "GET"])

def submit_and_verify():
    prenom = request.form.get("prenom")
    nom = request.form.get("nom")
    age = request.form.get("age")
    taille = request.form.get("taille")
    interet = request.form.get("interet")
    couleur = request.form.get("couleur")
    personne = "person_2"

    

    if not all([prenom, nom, age, taille, interet, couleur]):
        flash("Tous les champs doivent être remplis !", "error")
        return redirect(url_for("bonjour"))
    else :
        save_info_in_dico()
        compatibilite = compare_with_different_person(nom)
        return render_template("submitv2.html", compatibilite=compatibilite) 
  

def button_clicked():
    button = site.route('/submit', methods=['POST'])
    if not button.clicked:
        button.clicked = False
    else :
        button.clicked = True
    return button.clicked
    
def save_info ():
    return {
        "presentation" : {
            "prenom": request.form.get('prenom'),
            "nom": request.form.get('nom')
        },
        "info_perso" : {
            "age" : request.form.get('age'),
            "taille" : request.form.get('taille'),
            "interet" : request.form.get('interet'),
            "couleur" : request.form.get('couleur')
        }
    }
    
def save_info_in_dico():
    data = save_info()
    data_dict = load_data()
    
    if "dico" not in data_dict:
        data_dict["dico"] = []
    
    person_id = request.form.get("nom")
    data_dict["dico"].append({
            person_id: data
        })
    save_data(data_dict)




if __name__ == '__main__':
    site.run(debug=True)