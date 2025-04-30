# Bankkonto Beispiel für Vererbungsbeziehung
## Schritt 1: Klasse Konto schreiben
## Konto ist eine Basisklasse (aka Elternklasse)
class Konto:
    ## Konstruktor zum Instanziieren meines Konto-Objektes
    def __init__(self, kontonummer, inhaber, kontostand=0):
        self.kontonummer = kontonummer
        self.inhaber = inhaber
        self.kontostand = kontostand
    ## Methoden
    ### einzahlen-Methode
    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            print(f"{betrag} Euro wurde eingezahlt. Neuer Kontostand: {self.kontostand}")
        else:
            print("Der Betrag zum Einzahlen war ungültig")
    ### abheben-Methode
    def abheben(self, betrag):
        ## Standard: Kein Dispo, kann speziell
        if betrag > 0 and betrag <= self.kontostand:
            self.kontostand -= betrag
            print(f"{betrag} Euro wurde abgehoben. Neuer Kontostand: {self.kontostand}")
        else:
            print("Abhebung nicht möglich, Betrag ungültig")
    def __str__(self):
        return f"Konto mit Kontonummer {self.kontonummer} von {self.inhaber} hat den Kontostand: {self.kontostand} Euro"
    
## Schritt 2: Girokonto erstellen
## Girokonto erbt von der Elternklasse/Basisklasse Konto
class Girokonto(Konto):
    ## Konstruktor für das zu instanziierende Objekt Girokonto
    ## übernimmt die Attribute aus der Basisklasse Konto
    ## fügt aber noch das Attribut dispo hinzu, der standardmäßig auf 0 ist
    def __init__(self, kontonummer, inhaber, kontostand=0, dispo=0):
        super().__init__(kontonummer, inhaber, kontostand)
        self.dispo = dispo
    ## Überschreibe die Funktion abheben
    def abheben(self, betrag):
        if betrag > 0 and betrag <= (self.kontostand + self.dispo):
            self.kontostand -= betrag
            if (self.kontostand < 0):
                print("Achtung: Dispokredit wird in Anspruch genommen")
            print(f"{betrag} Euro wurde abgehoben. Neuer Kontostand: {self.kontostand}")
        else:
            print("Abhebung nicht möglich.")

## Schritt 3: Klasse Sparkonto erstellen
## Sparkonto erbt von der Elternklasse Konto
class Sparkonto(Konto):
    ## Konstruktor für unsere Klasse
    ## mit zusätzlichen Attribut zinssatz
    ## der Rest wird von Oberklasse Konto vererbt
    def __init__(self, kontonummer, inhaber, kontostand=0, zinssatz=0.01):
        super().__init__(kontonummer, inhaber, kontostand)
        self.zinssatz = zinssatz

    ## Spezifische Methode, die wir nur für Sparkonto Klasse implementieren
    def zinsen_gutschreiben(self):
        zinsen += self.kontostand * self.zinssatz
        self.kontostand += zinsen
        print(f"{zinsen} Euro wurden gutgeschrieen. Neuer Kontostand: {self.kontostand}")

konto_obj = Konto(123456, "Mirko", 25)
print(konto_obj)
konto_obj.einzahlen(5)
konto_obj.abheben(2)

giro_obj = Girokonto(456123, "Benjamin", 30, 5)
print(giro_obj)
giro_obj.abheben(30)
giro_obj.abheben(4)
giro_obj.abheben(5)

sparkonto_obj = Sparkonto(333111, "Kai", 40, 0.02)
print(sparkonto_obj)
sparkonto_obj.einzahlen(5)
sparkonto_obj.zinsen_gutschreiben()
sparkonto_obj.abheben(40)