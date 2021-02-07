from geometry.bangunruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l

    def info(self):
        return f'ini adalah object dari persegi panjang dengan panjang = {self.panjang} dan lebar = {self.lebar}'

    def hitung_luas(self):
        return self.panjang * self.lebar