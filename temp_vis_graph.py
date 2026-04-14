import matplotlib.pyplot as plt
import numpy as np

# --- 1. VERİ GİRİŞİ ---
# Ölçüm yaptığın 6 farklı RPM değerini buraya yaz:
rpm_etiketleri = [2, 4, 6, 10, 12, 30]

# Ölçüm yaptığın sıcaklıkları (Celsius) buraya yaz:
# (Genelde her devir için aynı sıcaklıklarda ölçüm yapılır)
sicakliklar_celsius = [20, 70]

# Her bir RPM için ölçtüğün viskozite (cP) değerlerini liste olarak gir:
# Not: Her listenin uzunluğu, yukarıdaki sıcaklık listesiyle aynı olmalıdır.
veriler = {
    2:  [0.075, 0.033],  # 6 RPM için viskoziteler
    4: [0.063, 0.024],  # 12 RPM için viskoziteler
    6: [0.049, 0.018],  # 20 RPM için viskoziteler
    10: [0.048, 0.012],  # 30 RPM için viskoziteler
    12: [0.053, 0.0125],  # 50 RPM için viskoziteler
    30: [0.0506, 0.0148]   # 60 RPM için viskoziteler
}

# --- 2. HESAPLAMALAR ---
T_kelvin = np.array(sicakliklar_celsius) + 273
x_ekseni = 1 / T_kelvin # 1/T değerleri

# --- 3. GRAFİK ÇİZİMİ ---
plt.figure(figsize=(12, 7))

# Her bir RPM serisi için döngü kurup çizgi ekliyoruz
renkler = ['red', 'blue', 'green', 'orange', 'purple', 'brown']

for i, rpm in enumerate(rpm_etiketleri):
    y_ekseni = np.log(veriler[rpm]) # ln(viskozite)
    plt.plot(x_ekseni, y_ekseni, marker='o', linestyle='-',
             color=renkler[i], label=f'{rpm} RPM', linewidth=1.5)

# --- 4. GRAFİK DÜZENLEME ---
plt.title("TEMPERATURE-VISCOSITY GRAPH", fontsize=14, fontweight='bold')
plt.xlabel("1/T (Kelvin⁻¹)", fontsize=12)
plt.ylabel("ln(Viscosity)", fontsize=12)

# Arka plan ızgarası
plt.grid(True, linestyle=':', alpha=0.7)

# Lejant (Hangi çizgi hangi RPM?)
plt.legend(title="RPMs", loc='best')

# Şık görünüm için kenarlıkları düzenle
plt.tight_layout()

# Kaydet ve Göster
#plt.savefig("arrhenius_6_rpm_analizi.png", dpi=300)
#print("Grafik 'arrhenius_6_rpm_analizi.png' olarak kaydedildi.")
plt.show()