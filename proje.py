import time

from kütüphane import*

print("""
***************************************
KÜTÜPHANE PROGRAMINA HOŞGELDİNİZ

İşlemler;

1-Kitapları Göster

2-Kitap Sorgulama

3-Kitap Ekle

4-Kitap Sil

5-Baskı Arttır

(Programdan Çıkmak İçin 'Q' Tuşuna Basın!)

*****************************************
""")

kütüphane=kütüphane()

while True:

    işlem=int(input("işlem numarası giriniz:"))

    if işlem=="Q":
        print("Programdan Çıkılıyor! \n Yine Bekleriz...")
        break

    elif işlem==1:
        kütüphane.kitapları_göster()

    elif işlem==2:
        a=input("Sorgulamak İstediğiniz Kitabın İsmini Giriniz:")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)
        kütüphane.kitap_sorgula(a)

    elif işlem==3:
        b=input("Lütfen Eklemek İstediğiniz Kitabın İsmini Giriniz:")
        c=input("Lütfen Eklemek İstediğiniz Kitabın Yazarını Giriniz:")
        d=input("Lütfen Eklemek İstediğiniz Kitabın Yayınevini Giriniz:")
        e=input("Lütfen Eklemek İstediğiniz Kitabın Türünü Giriniz:")
        f=input("Lütfen Eklemek İstediğiniz Kitabın Baskısını Giriniz:")
        yeni_kitap=kitaplık(b,c,d,e,f)
        print("Kitap Ekleniyor...")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi!")

    elif işlem==4:
        g=input("Lütfen Silmek İstediğiniz Kitabın İsmini Giriniz:")
        print("Kitap Siliniyor...")
        time.sleep(2)
        kütüphane.kitap_sil(g)
        print("Kitap Silindi!")

    elif işlem==5:
        h=input("Lütfen Baskısını Arttırmak İstediğiniz Kitabın İsmini Giriniz:")
        print("Baskı arttırılıyor...")
        time.sleep(2)
        kütüphane.baskı_arttır(h)
        print("Baskı Arttırıldı!")

    else:
        print("Geçersiz İşlem Numarası Girdiniz!!!")









































