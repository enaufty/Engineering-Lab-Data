import matplotlib.pyplot as plt

# 1. ADIM: KENDİ VERİLERİNİ BURAYA GİR
# Ölçüm yaptığınız RPM değerlerini sırasıyla araya virgül koyarak yazın:
rps_degerleri = [0.083, 0.1, 0.17, 0.2, 0.33, 0.5]

# Tork ile Faktörü çarparak bulduğunuz Dinamik Viskozite (cP) değerlerini sırasıyla yazın:
shear_stress = [0.056, 0.051, 0.058, 0.058, 0.07, 0.082]


# (Opsiyonel) Eğer asistanınız X eksenini RPM değil de RPS (saniyedeki devir) istediyse:
# Bu durumda aşağıdaki satırın başındaki '#' işaretini kaldırıp, plot kısmındaki x eksenini rps_degerleri yapabilirsiniz.
# rps_degerleri = [rpm / 60 for rpm in rpm_degerleri]


# 2. ADIM: GRAFİĞİ ÇİZ
plt.figure(figsize=(9, 6)) # Grafiğin boyutu (Genişlik, Yükseklik)

# Çizgi ve nokta (marker) ayarları
plt.plot(rps_degerleri, shear_stress,
         marker='o',  # Noktaların şekli (yuvarlak)
         linestyle='-',  # Çizgi stili (düz çizgi)
         color='#1f77b4',  # Çizgi rengi (güzel bir mavi tonu)
         linewidth=2.5,  # Çizgi kalınlığı
         markersize=8,  # Noktaların büyüklüğü
         markerfacecolor='red') # Noktaların iç rengi

# 3. ADIM: EKSEN İSİMLERİ VE BAŞLIK
plt.title("KETCHUP SAMPLE-2", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("RPS", fontsize=12, fontweight='bold')
plt.ylabel("SHEAR STRESS", fontsize=12, fontweight='bold')

# 4. ADIM: GÖRSEL DÜZENLEMELER (Arka plan ızgarası vb.)
plt.grid(True, linestyle='--', alpha=0.6) # Kesik çizgili, hafif şeffaf ızgara
plt.gca().spines['top'].set_visible(False)    # Üst çerçeveyi sil (daha şık durur)
plt.gca().spines['right'].set_visible(False)  # Sağ çerçeveyi sil

plt.tight_layout() # Düzeni ekrana tam oturt

# Grafiği ekranda göster ve kaydet
#plt.savefig("viskozite_grafigi.png", dpi=300) # Raporuna eklemen için yüksek çözünürlüklü kaydeder
#print("Grafik başarıyla çizildi ve 'viskozite_grafigi.png' olarak kaydedildi!")
plt.show()