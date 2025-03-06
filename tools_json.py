import json
import firebase_admin
from firebase_admin import credentials, db

# Chemin du fichier de données JSON
FILE_PATH = 'data.json'
DB_URL = "https://matchthingdemo-default-rtdb.firebaseio.com/" #A changer pour la vraie db
KEY_PATH = "firebase.json"

#Connection a la base de donnée
cred = credentials.Certificate(KEY_PATH)
firebase_admin.initialize_app(cred, {
    'databaseURL': DB_URL
})

#reference de la base de donnée
ref = db.reference('/')



# Fonction pour charger les données depuis le fichier JSON
#def load_data():
#    try:
#        with open(FILE_PATH, 'r') as file:
#            return json.load(file)
#    except (FileNotFoundError, json.JSONDecodeError):
#        return {}
def load_data():
    return ref.get() or{}

# Fonction pour sauvegarder les données dans le fichier JSON
#def save_data(data):
#    with open(FILE_PATH, 'w') as file:
#       json.dump(data, file, indent=4)
def save_data(data):
    ref.set(data)