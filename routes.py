from flask import Flask, render_template, request, redirect, url_for, flash
from tools_json import load_data, save_data
from compare_proximity import sort_compatibility_between_users, get_dico, representation_person_on_plan

site = Flask(__name__)
site.secret_key = "secret_key_for_flashing"

FILE_PATH = 'data.json'

@site.route("/")
def bonjour():
    plat = 4
    return render_template("index.html", plat=plat)

@site.route("/submit", methods=["POST", "GET"])
def submit_and_verify():
    prenom = request.form.get("prenom")
    nom = request.form.get("nom")
    age = request.form.get("age")
    taille = request.form.get("taille")
    interet = request.form.get("interet")
    couleur = request.form.get("couleur")
    matiere = request.form.get("matiere")
    plat = request.form.get("plat")

   
    sliders = {
        "interet": int(request.form.get("slider_value_interet", 5) or 5),
        "age": int(request.form.get("slider_value_age", 5) or 5),
        "taille": int(request.form.get("slider_value_taille", 5) or 5),
        "couleur": int(request.form.get("slider_value_couleur", 5) or 5),
        "matiere": int(request.form.get("slider_value_matiere", 5) or 5),
        "plat": int(request.form.get("slider_value_plat", 5) or 5)
    }

   
    if not all([prenom, nom, age, taille, interet, couleur, matiere, plat]):
        flash("Tous les champs doivent être remplis !", "error")
        return redirect(url_for("bonjour"))

    
    update_coef(sliders)
    save_info_in_dico(prenom, nom, age, taille, interet, couleur, matiere, plat)

   
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

def save_info_in_dico(prenom, nom, age, taille, interet, couleur, matiere, plat):
    data_dict = load_data()
    
    if "dico" not in data_dict:
        data_dict["dico"] = []

    person_id = nom.strip().lower()

    
    for person in data_dict["dico"]:
        if person_id in person:
            print(f"🔄 Mise à jour de {prenom} {nom} déjà existant dans la base de données.")
            person[person_id] = {
                "presentation": {"prenom": prenom, "nom": nom},
                "info_perso": {
                    "age": age, "taille": taille, "interet": interet,
                    "couleur": couleur, "matiere": matiere, "plat": plat
                }
            }
            save_data(data_dict)
            return

    
    print(f"✅ Ajout de {prenom} {nom} dans la base de données.")
    data_dict["dico"].append({
        person_id: {
            "presentation": {"prenom": prenom, "nom": nom},
            "info_perso": {
                "age": age, "taille": taille, "interet": interet,
                "couleur": couleur, "matiere": matiere, "plat": plat
            }
        }
    })

    save_data(data_dict)

def update_coef(sliders):
    data_dict = load_data()
    
    if "coef" not in data_dict:
        data_dict["coef"] = {}

    for key, value in sliders.items():
        data_dict["coef"][key] = value
    
    print(f"📊 Mise à jour des coefficients: {data_dict['coef']}")
    save_data(data_dict)

if __name__ == '__main__':
    site.run(debug=True)
