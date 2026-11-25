
kutuphane = {
    "1984": {"yazar": "George Orwell", "adet": 3},
    "Suc ve Ceza": {"yazar": "Fyodor Dostoyevski", "adet": 2},
    "Kucuk Prens": {"yazar": "Antoine de Saint-Exupery", "adet": 5},
    "Dune": {"yazar": "Frank Herbert", "adet": 1},
    "Simyaci": {"yazar": "Paulo Coelho", "adet": 4}
}


class Uye:
    def __init__(self, ad_soyad):
        self.ad_soyad = ad_soyad
        self.odunc_kitaplar = []

    def kitap_al(self, kutuphane, kitap_adi):
        if kitap_adi not in kutuphane:
            print(f"Uyarı: '{kitap_adi}' kütüphanede mevcut değil.")
        elif len(self.odunc_kitaplar) >= 3:
            print(f"Uyarı: {self.ad_soyad} adlı üyenin kitap limiti (3) dolmuş.")
        elif kutuphane[kitap_adi]["adet"] <= 0:
            print(f"Uyarı: '{kitap_adi}' kitabının stoğu tükenmiş.")
        else:
            kutuphane[kitap_adi]["adet"] -= 1
            self.odunc_kitaplar.append(kitap_adi)
            print(f"Başarılı: '{kitap_adi}' kitabı {self.ad_soyad} tarafından ödünç alındı.")

    def kitap_iade_et(self, kutuphane, kitap_adi):
        if kitap_adi in self.odunc_kitaplar:
            self.odunc_kitaplar.remove(kitap_adi)
            kutuphane[kitap_adi]["adet"] += 1
            print(f"Başarılı: '{kitap_adi}' kitabı iade edildi.")
        else:
            print(f"Uyarı: '{kitap_adi}' kitabı {self.ad_soyad}'ın ödünç listesinde bulunmuyor.")


uyeler = {
    "Ahmet Yilmaz": Uye("Ahmet Yilmaz"),
    "Zeynep Kaya": Uye("Zeynep Kaya")
}


while True:
    print("\n--- MİNİ KÜTÜPHANE MENÜSÜ ---")
    print("1 - Kitap Ödünç Al")
    print("2 - Kitap İade Et")
    print("3 - Üye Kitap Dağılımı ve Stok Durumu")
    print("4 - Üye Oluşturma")
    print("5 - Çıkış")
    
    secim = input("Yapmak istediğiniz işlemi seçin (1-5): ")

    if secim == "1":
        uye_ad_soyad = input("İşlem yapacak üyenin adı ve soyadı: ")
        if uye_ad_soyad in uyeler:
            kitap_adi = input("Ödünç alınacak kitap adı: ")
            uyeler[uye_ad_soyad].kitap_al(kutuphane, kitap_adi)
        else:
            print("Uyarı: Sistemde böyle bir üye bulunamadı.")

    elif secim == "2":
        uye_ad_soyad = input("İşlem yapacak üyenin adı ve soyadı: ")
        if uye_ad_soyad in uyeler:
            kitap_adi = input("İade edilecek kitap adı: ")
            uyeler[uye_ad_soyad].kitap_iade_et(kutuphane, kitap_adi)
        else:
            print("Uyarı: Sistemde böyle bir üye bulunamadı.")

    elif secim == "3":
        print("\n--- Üye Kitap Dağılımı ---")
        for uye_ad_soyad, uye_nesnesi in uyeler.items():
            print(f"Üye: {uye_ad_soyad} | Ödünç Kitaplar: {uye_nesnesi.odunc_kitaplar}")
        
        print("\n--- Kütüphane Stok Durumu ---")
        for kitap, bilgi in kutuphane.items():
            print(f"{kitap} ({bilgi['yazar']}) - Stok: {bilgi['adet']}")

    elif secim == "4":
        while True:
            yeni_ad_soyad = input("Yeni üyenin adını ve soyadını girin: ")
            if yeni_ad_soyad in uyeler:
                print("Uyarı: Bu ad ve soyad sistemde zaten kayıtlı! Lütfen farklı bir isim girin.")
            else:
                uyeler[yeni_ad_soyad] = Uye(yeni_ad_soyad)
                print(f"Başarılı: '{yeni_ad_soyad}' sisteme üye olarak eklendi.")
                break

    elif secim == "5":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim! Lütfen 1 ile 5 arasında bir değer girin.")

