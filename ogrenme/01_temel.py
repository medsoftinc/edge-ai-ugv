# 1) Değişkenler
robot_adi = "İKA-1"
hiz = 0.5        # m/s
batarya = 87     # yüzde

print(f"{robot_adi} hazır. Hız: {hiz} m/s, batarya: %{batarya}")

# 2) Liste
mesafeler = [2.4, 1.8, 0.6, 3.1, 5]   # 5 yöndeki engel mesafeleri (metre)
print("En yakın engel:", min(mesafeler), "m")

# 3) Döngü ve koşul
for yon, mesafe in enumerate(mesafeler):
    if mesafe < 1.0:
        print(f"  Yön {yon}: {mesafe} m -> TEHLİKE")
    else:
        print(f"  Yön {yon}: {mesafe} m -> güvenli")

# 4) Fonksiyon
def hiz_hesapla(en_yakin):
    if en_yakin < 0.5:
        return 0.0
    elif en_yakin < 1.0:
        return 0.2
    return 0.5

yeni_hiz = hiz_hesapla(min(mesafeler))
print("Seçilen hız:", yeni_hiz, "m/s")
