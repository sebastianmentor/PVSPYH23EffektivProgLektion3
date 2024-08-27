"""
2. Autentisering och Auktorisering
I webbutveckling är det vanligt att använda decorators för att hantera autentisering och auktorisering. Till exempel kan en decorator kontrollera om en användare är inloggad eller har rätt behörigheter innan en viss funktion körs.
Exempel: Om du har en webbapplikation och vill kontrollera att en användare är inloggad innan hen får åtkomst till en viss sida:
"""

def användare_inloggad(): pass

def kräver_inloggning(funktion):
    def wrapper(*args, **kwargs):
        if not användare_inloggad():
            raise Exception("Du måste vara inloggad för att få åtkomst.")
        return funktion(*args, **kwargs)
    return wrapper

@kräver_inloggning
def visa_konto():
    print("Här är dina kontouppgifter")
