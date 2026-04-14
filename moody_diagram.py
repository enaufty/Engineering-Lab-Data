import numpy as np
import matplotlib.pyplot as plt


def haaland(Re, relative_roughness):
    """Haaland denklemi ile sürtünme faktörü (Colebrook-White'a çok yakın bir açık formül)"""
    term = (relative_roughness / 3.7) ** 1.11 + 6.9 / Re
    f = (-1.8 * np.log10(term)) ** -2
    return f


# 1. Adım: Reynolds sayısı aralıklarını logaritmik olarak oluştur
# Laminer: 600 - 2300 arası | Türbülanslı: 4000 - 10^8 arası
Re_laminar = np.logspace(np.log10(10), np.log10(2300), 100)
re_turbulent = np.logspace(np.log10(4000), np.log10(1e8), 500)

# 2. Adım: Laminer akış sürtünme faktörünü hesapla
f_laminar = 64 / Re_laminar

# 3. Adım: Çizilecek bağıl pürüzlülük (ε/D) değerlerinin listesi
roughness_values = [0, 1e-5, 5e-5, 1e-4, 2e-4, 4e-4, 6e-4, 8e-4,
                    1e-3, 2e-3, 4e-3, 6e-3, 8e-3, 0.01, 0.015, 0.02, 0.03, 0.04, 0.05]

# --- ÇİZİM AŞAMASI ---
plt.figure(figsize=(12, 8))

# Laminer bölgeyi çiz
plt.loglog(Re_laminar, f_laminar, 'k-', linewidth=2, label='Laminer Akış ($f=64/Re$)')

# Türbülanslı bölgeyi farklı pürüzlülük değerleri için çiz
for eps_D in roughness_values:
    f_turb = haaland(re_turbulent, eps_D)
    plt.loglog(re_turbulent, f_turb, 'b-', alpha=0.7, linewidth=1.5)

    # Eğrilerin tam bittiği sağ uca bağıl pürüzlülük değerlerini yazdır
    plt.text(re_turbulent[-1] * 1.1, f_turb[-1], f"{eps_D:g}", fontsize=9, verticalalignment='center')

# Geçiş bölgesini (Transitional Zone) belirtmek için gri bir gölge ekle
plt.axvspan(2300, 4000, color='gray', alpha=0.2, label='Geçiş Bölgesi')

# Grafiği süsle (İsimler, Izgaralar, Sınırlar)
plt.title('Moody Diyagramı', fontsize=16, fontweight='bold')
plt.xlabel('Reynolds Sayısı ($Re$)', fontsize=14)
plt.ylabel('Sürtünme Faktörü ($f$)', fontsize=14)

# Logaritmik ızgaraları belirginleştir
plt.grid(True, which="both", ls="-", alpha=0.3)
plt.grid(True, which="major", ls="-", alpha=0.6, color='gray')

# Eksen sınırlarını ayarla
plt.xlim(1e1, 1e8)  # 1e3 yerine 1e1 yaptık ki düşük Re değerleri de görünsün
plt.ylim(0.008, 10)

# Sağ taraftaki eksen için bir açıklama (Bağıl pürüzlülük epsilon/D)
plt.text(2e8, 0.025, 'Bağıl Pürüzlülük ($\epsilon/D$)', rotation=90, verticalalignment='center', fontsize=14)

# --- KENDİ DEĞERLERİNİ BURAYA YAZ ---
# Aşağıdaki iki değeri kendi sistemine göre değiştir:
benim_Re = 24      # Örnek: Hesaplanmış Reynolds sayın
benim_eps_D = 0.00075   # Örnek: Borunun bağıl pürüzlülüğü (ε/D)

# Python senin için f değerini otomatik hesaplasın
if benim_Re < 2300:
    benim_f = 64 / benim_Re  # Laminer ise bu formül
else:
    benim_f = haaland(benim_Re, benim_eps_D) # Türbülanslı ise bu formül

# Kendi noktanı grafiğe büyük kırmızı bir nokta ('ro') olarak ekle
plt.plot(benim_Re, benim_f, color='red', marker='o', markersize=10, zorder=5, label='Benim Değerim')
# ------------------------------------

plt.legend(loc='lower left', fontsize=12)
plt.tight_layout()

# Ekranda göster
plt.show()