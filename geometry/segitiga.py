from geometry.bangunruang import BangunRuang


class Segitiga(BangunRuang):
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

    def info(self):
        return f'ini adalah object dari segitiga dengan alas = {self.alas} dan tinggi = {self.tinggi}'

    def hitung_luas(self):
        return (self.alas * self.tinggi) / 2