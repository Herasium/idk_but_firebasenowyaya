from flask import Flask, render_template, request, redirect, url_for, flash
import json



site = Flask(__name__)
site.secret_key = "secret_key_for_flashing"

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
    # compatibilite = main.compare_with_different_person(personne)
    

    if not all([prenom, nom, age, taille, interet, couleur]):
        flash("Tous les champs doivent être remplis !", "error")
        return redirect(url_for("bonjour"))
    else :
        save_info_in_dico()
        return render_template("submitv2.html") 
    # return render_template("submitv2.html", compatibilite=compatibilite) 


def button_clicked():
    button = site.route('/submit', methods=['POST'])
    if not button.clicked:
        button.clicked = False
    else :
        button.clicked = True
    return button.clicked
    
def save_info (pers):
    pers = {
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
    return pers

def save_info_in_dico ():
    key = request.form.get('nom')
    data = save_info (key)
    to_write = None
    ref = db.reference("/"+key)
    ref.set(data)


if __name__ == '__main__':
    site.run(debug=True)