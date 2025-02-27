import unittest
from unittest.mock import patch
from compare_proximity import (
    get_dico,
    compare_proximity,
    compare_with_different_person,
    list_of_compatibilite,
    list_of_people,
    sort_compatibility_between_users,
    distance_with_people,
    dico_distance,
    representation_person_on_plan,
)
from tools_json import load_data, save_data  # Import save_data

class TestCompareProximity(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.sample_data = {
            "coef": {"age": 10, "taille": 5, "interet": 15, "couleur": 20},
            "dico": [
                {"person_1": {"presentation": {"prenom": "Alice", "nom": "Dupont"}, "info_perso": {"age": "25", "taille": "170", "interet": "sport", "couleur": "bleu"}}},
                {"person_2": {"presentation": {"prenom": "Bob", "nom": "Martin"}, "info_perso": {"age": "30", "taille": "180", "interet": "lecture", "couleur": "vert"}}},
                {"person_3": {"presentation": {"prenom": "Charlie", "nom": "Durant"}, "info_perso": {"age": "25", "taille": "175", "interet": "sport", "couleur": "rouge"}}},
                {"person_4": {"presentation": {"prenom": "David", "nom": "Bernard"}, "info_perso": {"age": "30", "taille": "185", "interet": "voyage", "couleur": "vert"}}},
            ],
        }
        self.original_data = load_data()
        save_data(self.sample_data)

    def tearDown(self):
        save_data(self.original_data)

    @patch("compare_proximity.load_data")
    def test_get_dico(self, mock_load_data):
        mock_load_data.return_value = self.sample_data
        expected_dico = {
            "person_1": {"presentation": {"prenom": "Alice", "nom": "Dupont"}, "info_perso": {"age": "25", "taille": "170", "interet": "sport", "couleur": "bleu"}},
            "person_2": {"presentation": {"prenom": "Bob", "nom": "Martin"}, "info_perso": {"age": "30", "taille": "180", "interet": "lecture", "couleur": "vert"}},
            "person_3": {"presentation": {"prenom": "Charlie", "nom": "Durant"}, "info_perso": {"age": "25", "taille": "175", "interet": "sport", "couleur": "rouge"}},
            "person_4": {"presentation": {"prenom": "David", "nom": "Bernard"}, "info_perso": {"age": "30", "taille": "185", "interet": "voyage", "couleur": "vert"}},
        }
        self.assertEqual(get_dico(), expected_dico)

    @patch("compare_proximity.get_dico")
    def test_compare_proximity(self, mock_get_dico):
        mock_get_dico.return_value = self.sample_data["dico"]
        dico_test_compare_proximity = {
                "person_1": {"presentation": {"prenom": "Alice", "nom": "Dupont"}, "info_perso": {"age": "25", "taille": "170", "interet": "sport", "couleur": "bleu"}},
                "person_2": {"presentation": {"prenom": "Bob", "nom": "Martin"}, "info_perso": {"age": "30", "taille": "180", "interet": "lecture", "couleur": "vert"}},
                "person_3": {"presentation": {"prenom": "Charlie", "nom": "Durant"}, "info_perso": {"age": "25", "taille": "175", "interet": "sport", "couleur": "rouge"}},
                "person_4": {"presentation": {"prenom": "David", "nom": "Bernard"}, "info_perso": {"age": "30", "taille": "185", "interet": "voyage", "couleur": "vert"}},
            }
        mock_get_dico.return_value = dico_test_compare_proximity
        self.assertEqual(compare_proximity("person_1", "person_1"), 100.0)  #same person
        self.assertEqual(compare_proximity("person_1", "person_2"), 0.0)  #no similarity
        self.assertEqual(compare_proximity("person_1", "person_3"), round(((10+15)/ (10 + 5 + 15+ 20))*100, 1)) #same age, same interet
        self.assertEqual(compare_proximity("person_2", "person_4"), round(((10+20)/ (10 + 5 + 15+ 20))*100, 1)) #same age, same couleur

    @patch("compare_proximity.get_dico")
    def test_compare_with_different_person(self, mock_get_dico):
        mock_get_dico.return_value = {
                "person_1": {"presentation": {"prenom": "Alice", "nom": "Dupont"}, "info_perso": {"age": "25", "taille": "170", "interet": "sport", "couleur": "bleu"}},
                "person_2": {"presentation": {"prenom": "Bob", "nom": "Martin"}, "info_perso": {"age": "30", "taille": "180", "interet": "lecture", "couleur": "vert"}},
                "person_3": {"presentation": {"prenom": "Charlie", "nom": "Durant"}, "info_perso": {"age": "25", "taille": "175", "interet": "sport", "couleur": "rouge"}},
                "person_4": {"presentation": {"prenom": "David", "nom": "Bernard"}, "info_perso": {"age": "30", "taille": "185", "interet": "voyage", "couleur": "vert"}},
        }

        result = compare_with_different_person("person_1")
        self.assertIsInstance(result, dict)
        self.assertIn("person_2", result)
        self.assertIn("person_3", result)
        self.assertIn("person_4", result)
        self.assertNotIn("person_1", result)

    @patch("compare_proximity.compare_with_different_person")
    def test_list_of_compatibilite(self, mock_compare_with_different_person):
        mock_compare_with_different_person.return_value = {"person_2": 50.0, "person_3": 75.0}
        self.assertEqual(list_of_compatibilite("person_1"), [50.0, 75.0])

    @patch("compare_proximity.compare_with_different_person")
    def test_list_of_people(self, mock_compare_with_different_person):
        mock_compare_with_different_person.return_value = {"person_2": 50.0, "person_3": 75.0}
        self.assertEqual(list_of_people("person_1"), ["person_2", "person_3"])

    @patch("compare_proximity.list_of_compatibilite")
    @patch("compare_proximity.list_of_people")
    def test_sort_compatibility_between_users(self, mock_list_of_people, mock_list_of_compatibilite):
        mock_list_of_compatibilite.return_value = [50.0, 75.0, 25.0]
        mock_list_of_people.return_value = ["person_2", "person_3", "person_4"]
        sort_number, sort_people = sort_compatibility_between_users("person_1")
        self.assertEqual(sort_number, [75.0, 50.0, 25.0])
        self.assertEqual(sort_people, ["person_3", "person_2", "person_4"])

    @patch("compare_proximity.sort_compatibility_between_users")
    def test_distance_with_people(self, mock_sort_compatibility_between_users):
        mock_sort_compatibility_between_users.return_value = ([75.0, 50.0, 25.0], ["person_3", "person_2", "person_4"])
        sort_distance, sort_people = distance_with_people("person_1")
        self.assertEqual(sort_distance, [25.0, 50.0, 75.0])
        self.assertEqual(sort_people, ["person_3", "person_2", "person_4"])

    @patch("compare_proximity.distance_with_people")
    def test_dico_distance(self, mock_distance_with_people):
        mock_distance_with_people.return_value = ([25.0, 50.0], ["person_3", "person_2"])
        dico = dico_distance("person_1")
        self.assertEqual(dico, {"person_3": 25.0, "person_2": 50.0})

    @patch("compare_proximity.get_dico")
    @patch("compare_proximity.dico_distance")
    def test_representation_person_on_plan(self, mock_dico_distance, mock_get_dico):
        mock_dico_distance.return_value = {"person_2": 50.0, "person_3": 25.0}
        mock_get_dico.return_value = {
            "person_2": {"presentation": {"prenom": "Bob", "nom": "Martin"}},
            "person_3": {"presentation": {"prenom": "Charlie", "nom": "Durant"}},
        }
        result = representation_person_on_plan("person_1")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(isinstance(item, dict) for item in result))
        self.assertTrue(all("name" in item and "x" in item and "y" in item for item in result))

if __name__ == "__main__":
    unittest.main()
