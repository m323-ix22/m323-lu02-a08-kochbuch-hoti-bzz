"""Kochbuch"""

import json


def load_recipe(json_string):
    """Lädt ein Rezept aus einem JSON-String und gibt ein Python-Dictionary zurück."""
    return json.loads(json_string)


def adjust_recipe(recp, num_people):
    """Passt die Mengenangaben im Rezept an die gegebene Anzahl von Personen an."""
    factor = num_people / recp['servings']
    adjusted_ingredients = {
        ingredient: round(amount * factor, 2)  # Rundet die Menge auf 2 Dezimalstellen
        for ingredient, amount in recp['ingredients'].items()
    }
    # Erstelle ein neues Rezept-Dictionary mit den angepassten Mengen
    adj_recp = {
        'title': recp['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }
    return adj_recp


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, ' \
                  '"Minced Meat": 500}, "servings": 4} '

    # Rezept laden
    recipe = load_recipe(recipe_json)
    print("Original Recipe:", recipe)

    # Rezept für 2 Personen anpassen
    adjusted_recipe = adjust_recipe(recipe, 2)
    print("Adjusted Recipe for 2 servings:", adjusted_recipe)

    # Rezept für 6 Personen anpassen
    adjusted_recipe = adjust_recipe(recipe, 6)
    print("Adjusted Recipe for 6 servings:", adjusted_recipe)
