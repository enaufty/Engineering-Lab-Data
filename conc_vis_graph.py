import matplotlib.pyplot as plt
import numpy as np

# --- 1. VERİ GİRİŞİ ---

# Deneyde kullandığın konsantrasyonları yaz (Örn: %1, %2, %5, %10)
konsantrasyonlar = [100, 50]

# Ölçüm yaptığın 6 RPM değerini yaz
rpms = [5, 6, 10, 12, 20, 30]

# Her bir RPM için, yukarıdaki konsantrasyon sırasına göre viskozite (cP) değerlerini gir
# Önemli: Her listenin uzunluğu konsantrasyon listesiyle aynı olmalı (burada 4 adet).
veriler = {
    5:  [28300, 6700],  # 6 RPM'deki viskoziteler
    6: [24700, 5100],  # 12 RPM'deki viskoziteler
    10: [17700, 3480],  # 20 RPM'deki viskoziteler
    12: [15600, 2900],  # 30 RPM'deki viskoziteler
    20: [11250, 2100],   # 50 RPM'deki viskoziteler
    30: [8640, 1640]    # 60 RPM'deki viskoziteler
}

# --- 2. GRAFİK ÇİZİMİ ---

plt.figure(figsize=(10, 7))

# Renk paleti (6 farklı çizgi için)
renkler = ['#d62728', '#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#8c564b']

# Her RPM serisini döngüyle grafiğe ekle
for i, rpm in enumerate(rpms):
    plt.plot(konsantrasyonlar, veriler[rpm],
             marker='o',
             linestyle='-',
             linewidth=2,
             markersize=7,
             color=renkler[i],
             label=f'{rpm} RPM')

# --- 3. EKSEN VE BAŞLIK AYARLARI ---

plt.title("VISCOSITY CONCENTRATION GRAPH", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Concentration (%)", fontsize=12, fontweight='bold')
plt.ylabel("Viscosity (cP)", fontsize=12, fontweight='bold')

# Grafik düzenlemeleri
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title="Ölçüm Hızları", loc='upper left', fontsize=10)

# Gereksiz çerçeveleri temizle (Modern görünüm)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

# Grafiği yüksek çözünürlükte kaydet
#plt.savefig("konsantrasyon_viskozite_tek_numune.png", dpi=300)
#print("Grafik 'konsantrasyon_viskozite_tek_numune.png' olarak kaydedildi.")