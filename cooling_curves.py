import matplotlib.pyplot as plt

# Zaman (Dakika)
time = [0, 2, 4, 6]

# Sıcaklık Verileri (°C)
set1 = [60, 31, 24, 20]
set2 = [39, 34, 25, 20]
set3 = [52, 32, 24, 19.5]
set4 = [60, 35, 24, 19]

# Grafiği oluşturma
plt.figure(figsize=(10, 6))

# Çizgileri ve işaretçileri ekleme
plt.plot(time, set1, marker='o', linestyle='-', linewidth=2, label='Set-1 (Reference)')
plt.plot(time, set2, marker='s', linestyle='-', linewidth=2, label='Set-2 (Stirring Speed)')
plt.plot(time, set3, marker='^', linestyle='-', linewidth=2, label='Set-3 (Surface Area)')
plt.plot(time, set4, marker='d', linestyle='-', linewidth=2, label='Set-4 (Salt Solution)')

# Eksen isimlendirmeleri ve başlık
plt.title('Cooling Curves of Different Experimental Conditions', fontsize=14, fontweight='bold')
plt.xlabel('Time (min)', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

# Grid (Izgara) ve Lejant (Etiketler) ayarları
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)

# Eksen sınırlarını biraz esnetelim ki noktalar kenarlara yapışmasın
plt.ylim(15, 65)
plt.xlim(-0.2, 6.2)

# Grafiği gösterme ve kaydetme opsiyonu
plt.tight_layout()
plt.show()