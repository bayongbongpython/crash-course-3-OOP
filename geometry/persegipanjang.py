class PersegiPanjang():
    def__init__(self, p, l):
    #fungsi yang dipanggil per tama kali saat object diciptakan
        self.p = p
        self.l = l

    def info(self):
         return f'Modul menghitung rumus-rumus tentang persegipanjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l