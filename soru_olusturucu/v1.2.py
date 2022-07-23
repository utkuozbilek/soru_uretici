import sqlite3
class Kitap():
    def __init__(self,donem,yazar,tur,eser):     
        self.yazar = yazar
        self.eser=eser
        self.tur = tur
        self.donem=donem
class Soru():
    def __init__(self,soru,tur): 
        self.soru=soru
        self.tur = tur
class Kutuphane():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("kkutupkane.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists kitaplar (donem TEXT,yazar TEXT,tur TEXT,eser TEXT)"
        sorgu1 = "Create Table If not exists sorular (soru1 TEXT,tur TEXT)"
        self.cursor.execute(sorgu)
        self.cursor.execute(sorgu1)
        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def kitap_ekle(self,kitap):
        sorgu = "Insert into kitaplar Values(?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.donem,kitap.yazar,kitap.tur,kitap.eser))
        self.baglanti.commit()
    def soru_ekle(self,soru1):
        sorgu1 = "Insert into sorular Values(?,?)"
        self.cursor.execute(sorgu1,(soru1.tur,soru1.soru))
        self.baglanti.commit()
    def verileri_al(self):
        self.cursor.execute("Select * From kitaplar")
        liste=self.cursor.fetchall()
        print("kitaplık tablosunun bilgileri...")
        for i in liste:
            print(i)
Kutuphane=Kutuphane()  
Kutuphane.baglanti_olustur()
Kutuphane.verileri_al()