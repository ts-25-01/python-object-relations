# Tier Beispiel mit Vererbungsbeziehung
## Klasse Tier als Elternklasse
class Tier:
    def __init__(self, name):
        self.name = name
    ## Methoden für die Klasse Tier
    ### Funktion, damit das Tier sich mit Namen vorstellt
    def vorstellen(self):
        print(f"Hallo, ich bin {self.name}")
    ### Geräusch machen, wird aber speziell von den Kindklassen nochmal spezieller überschrieben
    def geraeusch_machen(self):
        print("Ein Tiergeräusch")
## Klasse Hund als Kindklasse
class Hund(Tier): # Hey erstelle eine Klasse Hund, die von der Klasse Tier abgeleitet wird 
    def __init__(self, name, fellfarbe):
        super().__init__(name) # Aufruf des Konstruktors der Elternklasse
        self.fellfarbe = fellfarbe
    def geraeusch_machen(self):
        print(f"{self.name} bellt und macht Wuff!")

# class SpeziellerHund(Hund)
    
## Klasse Esel als Kindklasse
class Esel(Tier):
    def __init__(self, name, ohr_laenge):
        super().__init__(name)
        self.ohr_laenge = ohr_laenge

    def geraeusch_machen(self):
        print(f"Mein Esel {self.name} macht IAHH!")

tier_obj = Tier("Allgemeines Tier")
tier_obj.vorstellen()
tier_obj.geraeusch_machen()

hund_obj = Hund("Bello", "grau")
hund_obj.vorstellen()
hund_obj.geraeusch_machen()

esel_obj = Esel("Bernd", "15")
esel_obj.vorstellen()
esel_obj.geraeusch_machen()