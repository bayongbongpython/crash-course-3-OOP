class SegiTiga():
    def __init__(self, alas, tinggi):
        # fungsi yang dipanggil per tama kali saat object diciptakan
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'Ini adalah object dari Segitiga dengan alas = {self.alas} dan tinggi = {self.tinggi}'

    def hitung_luas(self):
        return self.alas * self.tinggi /2

