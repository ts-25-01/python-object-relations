class Handbuch:
    def __init__(self, beschreibung):
        self.beschreibung = beschreibung

class Instrument:
    def __init__(self, name):
        self.name = name
        self.handbuch = Handbuch(f"Hanbuch für {self.name}")