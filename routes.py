from flask import Flask, render_template, request, redirect, url_for, flash
from tools_json import load_data, save_data
from compare_proximity import sort_compatibility_between_users, get_dico, representation_person_on_plan


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
    matiere = request.form.get("matiere")

    

    if not all([prenom, nom, age, taille, interet, couleur, matiere]):
        flash("Tous les champs doivent être remplis !", "error")
        return redirect(url_for("bonjour"))
    else :
        save_info_in_dico()
        current_person = nom.strip().lower()
        sort_number, sort_people = sort_compatibility_between_users(current_person)
        dico = get_dico()
        sort_people_display = [
        f"{dico[person]['presentation']['prenom']} {dico[person]['presentation']['nom']}"
        if person in dico else person 
        for person in sort_people
        ]
        positions = representation_person_on_plan(current_person)
        return render_template("submitv2.html", sort_number=sort_number, sort_people=sort_people_display, positions=positions) 
  

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
            "couleur" : request.form.get('couleur'),
            "matiere" : request.form.get('matiere')
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