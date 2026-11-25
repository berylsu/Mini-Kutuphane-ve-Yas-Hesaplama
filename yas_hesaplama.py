from datetime import date


class Kisi:
    def __init__(self, isim, dogum_gunu):
        self.isim = isim
        self.dogum_gunu = dogum_gunu  
        
def yas_hesapla(kisi):
    bugun = date.today()
    gun = kisi.dogum_gunu[0]
    ay = kisi.dogum_gunu[1]
    yil = kisi.dogum_gunu[2]
    
    yas = bugun.year - yil
    
    if (bugun.month, bugun.day) < (ay, gun):
        yas -= 1
        
    return yas

def gun_farki_bul(kisi1, kisi2):
    
    tarih1 = date(kisi1.dogum_gunu[2], kisi1.dogum_gunu[1], kisi1.dogum_gunu[0])
    tarih2 = date(kisi2.dogum_gunu[2], kisi2.dogum_gunu[1], kisi2.dogum_gunu[0])
    
    
    fark = abs((tarih1 - tarih2).days)
    
    if tarih1 < tarih2:
        return f"{kisi1.isim}, {kisi2.isim}'den {fark} gün daha büyüktür."
    elif tarih2 < tarih1:
        return f"{kisi2.isim}, {kisi1.isim}'den {fark} gün daha büyüktür."
    else:
        return f"{kisi1.isim} ve {kisi2.isim} aynı gün doğmuştur."

kisi1 = Kisi("Beril Su", [14, 5, 2005])
kisi2 = Kisi("Anil", [28, 11, 2003])

print(f"{kisi1.isim}'in güncel yaşı: {yas_hesapla(kisi1)}")
print(f"{kisi2.isim}'in güncel yaşı: {yas_hesapla(kisi2)}")
print(gun_farki_bul(kisi1, kisi2))