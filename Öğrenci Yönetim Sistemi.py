# Python-ile-Veri-Bilimi-3.-Hafta-Odevi
#Öğrenci Yönetim Sistemi
# Öğrenci listesi
ogrenciler = []

# Öğrenci ekleme fonksiyonu
def ogrenci_ekle():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    numara = input("Öğrenci numarası: ")
    bolum = input("Bölüm: ")
    not_ortalamasi = float(input("Not ortalaması: "))
    
    ogrenci = {
        "ad": ad,
        "soyad": soyad,
        "numara": numara,
        "bolum": bolum,
        "not_ortalamasi": not_ortalamasi
    }
    ogrenciler.append(ogrenci)
    print("Öğrenci başarıyla eklendi.\n")

# Öğrenci listeleme fonksiyonu
def ogrencileri_listele():
    if not ogrenciler:
        print("Henüz öğrenci eklenmedi.\n")
        return
    print("Öğrenci Listesi:")
    for ogrenci in ogrenciler:
        print(f"{ogrenci['numara']} - {ogrenci['ad']} {ogrenci['soyad']} - {ogrenci['bolum']} - Not Ortalaması: {ogrenci['not_ortalamasi']}")
    print()

# Belirli bir öğrenciyi görüntüleme fonksiyonu
def ogrenci_goruntule():
    numara = input("Görüntülemek istediğiniz öğrencinin numarası: ")
    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            print(f"{ogrenci['numara']} - {ogrenci['ad']} {ogrenci['soyad']} - {ogrenci['bolum']} - Not Ortalaması: {ogrenci['not_ortalamasi']}\n")
            return
    print("Öğrenci bulunamadı.\n")

# Öğrenci güncelleme fonksiyonu
def ogrenci_guncelle():
    numara = input("Güncellemek istediğiniz öğrencinin numarası: ")
    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            print("Yeni bilgileri giriniz:")
            ogrenci["ad"] = input("Yeni Ad: ")
            ogrenci["soyad"] = input("Yeni Soyad: ")
            ogrenci["bolum"] = input("Yeni Bölüm: ")
            ogrenci["not_ortalamasi"] = float(input("Yeni Not Ortalaması: "))
            print("Öğrenci bilgileri güncellendi.\n")
            return
    print("Öğrenci bulunamadı.\n")

# Öğrenci silme fonksiyonu
def ogrenci_sil():
    numara = input("Silmek istediğiniz öğrencinin numarası: ")
    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            ogrenciler.remove(ogrenci)
            print("Öğrenci başarıyla silindi.\n")
            return
    print("Öğrenci bulunamadı.\n")

# Menü
while True:
    print("1- Öğrenci Ekle")
    print("2- Öğrenci Listele")
    print("3- Öğrenci Görüntüle")
    print("4- Öğrenci Güncelle")
    print("5- Öğrenci Sil")
    print("0- Çıkış")
    
    secim = input("Seçiminizi yapın: ")
    
    if secim == "1":
        ogrenci_ekle()
    elif secim == "2":
        ogrencileri_listele()
    elif secim == "3":
        ogrenci_goruntule()
    elif secim == "4":
        ogrenci_guncelle()
    elif secim == "5":
        ogrenci_sil()
    elif secim == "0":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.\n")
