import sqlite3
class Kitap():
    def __init__(self,donem,yazar,tur,eser):      
        self.yazar = yazar
        self.eser=eser
        self.tur = tur
        self.donem=donem 
class Kutuphane():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("kkutupkane.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists kitaplar (donem TEXT,yazar TEXT,tur TEXT,eser TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def kitap_ekle(self,kitap):
        sorgu = "Insert into kitaplar Values(?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.donem,kitap.yazar,kitap.tur,kitap.eser))
        self.baglanti.commit()
kutuphane=Kutuphane()    
with open("troman.txt","r",encoding="utf-8") as file:
    for i in file:
        i = i[:-1]
        i=i.split(",")
        yazar=i[0]
        eser=i[1]
        tur="roman"
        donem="Tanzimat"
        yeni_kitap = Kitap(donem,yazar,tur,eser)
        kutuphane.kitap_ekle(yeni_kitap)
with open("tşiir.txt","r",encoding="utf-8") as file2:
    for i in file2:
        i = i[:-1]
        i=i.split(",")
        yazar=i[0]
        eser=i[1]
        tur="siir"
        donem="Tanzimat"
        yeni_kitap = Kitap(donem,yazar,tur,eser)
        kutuphane.kitap_ekle(yeni_kitap)
with open("croman.txt","r",encoding="utf-8") as file3:
    for i in file3:
        i = i[:-1]
        i=i.split(",")
        yazar=i[0]
        eser=i[1]
        tur="roman"
        donem="Cumhuriyet"
        yeni_kitap = Kitap(donem,yazar,tur,eser)
        kutuphane.kitap_ekle(yeni_kitap)
with open("chikaye.txt","r",encoding="utf-8") as file4:
    for i in file4:
        i = i[:-1]
        i=i.split(",")
        yazar=i[0]
        eser=i[1]
        tur="Hikaye"
        donem="Cumhuriyet"
        yeni_kitap = Kitap(donem,yazar,tur,eser)
        kutuphane.kitap_ekle(yeni_kitap)