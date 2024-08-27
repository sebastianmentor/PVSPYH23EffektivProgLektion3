"""
6. Modifiera API-svar
Decorators används ofta för att paketera eller modifiera API-svar i webbutveckling. Exempelvis kan du formatera ett svar som JSON innan det skickas tillbaka till en klient.
"""

import json

def till_json(funktion):
    def wrapper(*args, **kwargs):
        resultat = funktion(*args, **kwargs)
        return json.dumps(resultat)
    return wrapper

@till_json
def hämta_data():
    return {"namn": "Anna", "ålder": 28}

print(hämta_data())  # Resultatet returneras som en JSON-sträng
