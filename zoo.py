# Zoo-Verwaltung
## Klasse Art
class Art:
    def __init__(self, name):
        self.name = name
## Klasse Tier
class Tier:
    def __init__(self, name, art_name):
        self.name = name
        ## Achtung Kompositionsbeziehung zu Art
        self.art = Art(art_name)
## Klasse Pfleger
class Pfleger:
    def __init__(self, name):
        self.name = name
        self.tiere = []
    
    ## Funktion, um dem Pfleger Tiere zuzuordnen
    def tier_hinzufuegen(self, tier):
        self.tiere.append(tier)
        print(f"Das Tier {tier.name} von der Art {tier.art.name} wurde dem Pfleger {self.name} erfolgreich zugeordnet")

    def tiere_anzeigen(self):
        print(f"Pfleger {self.name} kümmert sich um: ")
        for tier in self.tiere:
            print(f"- {tier.name} der Art {tier.art.name}")

## Klasse Fütterung
class Fuetterung:
    def __init__(self, pfleger, tier):
        self.pfleger = pfleger
        self.tier = tier

    def starten(self):
        print(f"Pfleger {self.pfleger.name} fütter das Tier {self.tier.name} der Art {self.tier.art.name}")


## Objekte erstellen
tier_obj_simba = Tier("Simba", "Löwe")
tier_obj_melman = Tier("Melman", "Giraffe")
pfleger_obj_tom = Pfleger("Tom")
pfleger_obj_tom.tier_hinzufuegen(tier_obj_simba)
pfleger_obj_tom.tier_hinzufuegen(tier_obj_melman)
pfleger_obj_tom.tiere_anzeigen()
futterrunde_obj = Fuetterung(pfleger_obj_tom, tier_obj_simba)
futterrunde_obj.starten()