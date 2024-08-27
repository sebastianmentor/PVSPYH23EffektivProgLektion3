"""
1. Loggning
Decorators kan användas för att logga när och hur en funktion körs. Detta är särskilt användbart för att felsöka eller övervaka applikationer.
Exempel: Om du har flera funktioner i din applikation och du vill logga när varje funktion anropas, kan du använda en decorator för detta istället 
för att lägga till loggningskod i varje funktion.
"""

def logga(funktion):
    def wrapper(*args, **kwargs):
        print(f"Kör {funktion.__name__} med args: {args} och kwargs: {kwargs}")
        return funktion(*args, **kwargs)
    return wrapper

@logga
def lägg_till(a, b):
    return a + b

lägg_till(5, 7)
