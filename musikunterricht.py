class Handbuch:
    def __init__(self, beschreibung):
        self.beschreibung = beschreibung

class Instrument:
    def __init__(self, name):
        self.name = name
        self.handbuch = Handbuch(f"Handbuch für {self.name}")

class Schueler:
    def __init__(self, name):
        self.name = name
        self.instrumente = []

    def add_instrument(self, instrument: Instrument):
        self.instrumente.append(instrument)
    
    def show_instruments(self):
        print(f"Der Schüler {self.name} hat folgende Instrumente:")
        for instrument in self.instrumente:
            print(instrument.name)

class Unterrichtsstunde:
    def __init__(self, schueler, instrument):
        self.schueler = schueler
        self.instrument = instrument

    def starten(self):
        print(f"{self.schueler.name} übt gerade auf dem Instrument {self.instrument.name}")        

trompete = Instrument("Trompete")
schueler_lisa = Schueler("Lisa")
schueler_lisa.show_instruments()

schueler_lisa.add_instrument(trompete)
schueler_lisa.show_instruments()
lisas_trompetenunterricht = Unterrichtsstunde(schueler_lisa, trompete)
lisas_trompetenunterricht.starten()