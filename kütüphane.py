import sqlite3
import time

class kitaplık():

    def __init__(self,isim,yazar,yayın,tür,baskı):
        self.isim=isim
        self.yazar=yazar
        self.yayın=yayın
        self.tür=tür
        self.baskı=baskı

    def __str__(self):
        return "kitap ismi:{}\n,yazarı:{}\n,yayını:{}\n,türü:{}\n,baskısı:{}\n".format(self.isim,self.yazar,self.yayın,self.tür,self.baskı)


class kütüphane():
    def __init__(self):
        self.bağlantıolustur()

    def bağlantıolustur(self):
        self.bağlantı=sqlite3.connect("kütüphane.db")
        self.cursor=self.bağlantı.cursor()

        sorgu="CREATE TABLE IF NOT EXISTS kitaplar(isim TEXT,yazar TEXT,yayın TEXT,tür TEXT,baskı INT)"
        self.cursor.execute(sorgu)
        self.bağlantı.commit()

    def bağlantıkes(self):
        self.bağlantı.close()

    def kitapları_göster(self):
        sorgu="select*from kitaplar"
        self.cursor.execute(sorgu)
        a=self.cursor.fetchall()

        if len(a)==0:
            print("kitaplık boş!!!")
        else:
            for i in a:
                kitap=kitaplık(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitap_sorgula(self,isim):
        sorgu="select*from kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        b=self.cursor.fetchall()

        if len(b)==0:
            print("bu isimde bir kitap bulunmuyor!!!")
        else:
            kitap=kitaplık(b[0][0],b[0][1],b[0][2],b[0][3],b[0][4])
            print(kitap)

    def kitap_ekle(self,kitaplık):
        sorgu="insert into kitaplar values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitaplık.isim,kitaplık.yazar,kitaplık.yayın,kitaplık.tür,kitaplık.baskı))
        self.bağlantı.commit()

    def kitap_sil(self,isim):
        sorgu="delete from kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.bağlantı.commit()

    def baskı_arttır(self,isim):
        sorgu="select * from kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        c=self.cursor.fetchall()

        if len(c)==0:
            print("böyle bir kitap yok!!!")

        else:
            baskı=c[0][4]
            baskı+=1
            sorgu2="Update kitaplar set baskı=? where isim=?"
            self.cursor.execute(sorgu2,(baskı,isim))
            self.bağlantı.commit()







































