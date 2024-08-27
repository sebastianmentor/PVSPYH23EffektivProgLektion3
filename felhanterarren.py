"""
5. Automatisk Felhantering
Du kan använda en decorator för att fånga och hantera fel i flera funktioner utan att behöva skriva try-except-block i varje funktion.

Exempel: En decorator som fångar undantag och loggar dem:
"""
def fånga_undantag(funktion):
    def wrapper(*args, **kwargs):
        try:
            return funktion(*args, **kwargs)
        except Exception as e:
            print(f"Fel inträffade: {e}")
    return wrapper

@fånga_undantag
def division(a, b):
    return a / b

print(division(10, 0))  # Kommer att fånga division med noll
