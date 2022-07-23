import sqlite3
con = sqlite3.connect("kkutupkane.db")
cursor = con.cursor()
def verileri_al():
    cursor.execute("Select * From kitaplar") 
    data = cursor.fetchall() 
    cursor.execute("Select * From sorular") 
    data1 = cursor.fetchall() 
    for i in data:
        donem=i[0]
        yazar=i[1]
        tur=i[2]
        eser=i[3]
        pass
    for i in data1:
        tur=i[0]
        soru=i[1]
        pass       
def verileri_al2():
    cursor.execute("select İsim,Yazar From kitaplık")
    liste=cursor.fetchall()
    print("kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)          
def soru_uret(satr): 
    satr = satr[:-1]
    liste = satr.split(",")
    isim = liste[0]  
    return isim +" adlı yazarın özgürlük alayışınedir?.Bir eserinden yola çıkarak anlatınız."+ "\n"
with open("chikaye.txt","r",encoding= "utf-8") as file:
    eklenecekler_listesi = []
    for i in file:
        eklenecekler_listesi.append(soru_uret(i))
        with open("son.txt","w",encoding="utf-8") as file2:
            for i in eklenecekler_listesi:
                file2.write(i)              
verileri_al2()