"""
4. Tidtagning av Funktioner
För prestandaanalys kan en decorator användas för att mäta hur lång tid en funktion tar att köra. Detta är mycket användbart när du optimerar kod.

Exempel: Om du vill veta hur lång tid vissa funktioner tar:
"""

import time

def tidtagning(funktion):
    def wrapper(*args, **kwargs):
        start = time.time()
        resultat = funktion(*args, **kwargs)
        slut = time.time()
        print(f"Funktionen {funktion.__name__} tog {slut - start:.4f} sekunder.")
        return resultat
    return wrapper

@tidtagning
def långsam_funktion():
    time.sleep(2)
    print("Klar!")

långsam_funktion()
