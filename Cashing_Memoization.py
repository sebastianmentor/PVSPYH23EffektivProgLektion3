"""
3. Caching / Memoization
Decorators används ofta för att cacha resultat av dyra funktioner så att de inte behöver beräknas om flera gånger. Detta är användbart i beräkningstunga applikationer eller när du hämtar data från en långsam extern källa.

Exempel: Om du har en funktion som beräknar något som tar lång tid, kan du cacha resultaten för framtida användning:
"""

def cacha(funktion):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        resultat = funktion(*args)
        cache[args] = resultat
        return resultat
    return wrapper

@cacha
def tung_beräkning(n):
    # Simulerar en tung beräkning
    from time import sleep
    sleep(2)
    return n * n

print(tung_beräkning(4))  # Tar tid första gången
print(tung_beräkning(4))  # Snabb andra gång eftersom resultatet är cachat
