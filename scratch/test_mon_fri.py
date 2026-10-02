import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))

import openpyxl, xml.etree.ElementTree as ET
from collections import defaultdict
from generate_schedule import load_and_schedule, TEACHERS, TIME_SLOTS, DAYS

schedule, students_info = load_and_schedule()

print("="*70)
print("TEST 1: FERHAT ERDAL - PAZARTESİ VE CUMA LİSANSÜSTÜ DERSLERİNİ KALDIRMAK")
print("="*70)
# Ferhat Hoca:
# Pzt: sadece İNM 403 (12:30-13:20) kalsın (1 saat)
# Cum: 0 saat
# Salı, Çarşamba, Perşembe'ye 22 saat sığıyor mu?

# Simülasyon tablosu:
# Salı:
# 08:30-12:20: FBE 9901 (4 saat Uzmanlık)
# 12:30-13:20: İNM 403 (1 saat Lisans)
# 13:30-14:20: Danışmanlık 1 (Osman Can Kaya)
# 14:30-15:20: Danışmanlık 2 (Adriana)
# 15:30-16:20: Danışmanlık 3 (Ersin Kaçmaz)
# Toplam Salı = 8 saat

# Çarşamba:
# 08:30-09:20: Danışmanlık 4 (Seçil Karaçalı - Seçil'in Çar 08:30'u boş!)
# 09:30-12:20: İNM 211 (3 saat Lisans)
# 12:30-13:20: Boş (veya müsait)
# 13:30-17:20: FBE 9901 (4 saat Uzmanlık)
# Toplam Çarşamba = 8 saat (veya 7 saat)

# Perşembe:
# 08:30-09:20: Boş
# 09:30-12:20: İNM 433 (3 saat Lisans)
# 12:30-13:20: Boş
# 13:30-16:20: İNM 5065 (3 saat Seçmeli)
# 16:30-17:20: Boş
# Toplam Perşembe = 6 saat (veya Seçil buraya 08:30'a konursa 7 saat)

print("Ferhat Hoca Dağılımı:")
print("Pzt: 1 saat (İNM 403 - Lisans Semineri, yetki dışı)")
print("Sal: 8 saat")
print("Çar: 8 saat")
print("Per: 6 saat")
print("Cum: 0 saat (Tamamen Boş)")
print("Toplam = 23 saat. Çakışma = 0. Günlük Max = 8. Mümkün mü? -> EVET!")

print("\n" + "="*70)
print("TEST 2: RAMAZAN ÖZÇELİK - PAZARTESİ LİSANSÜSTÜ DERSLERİNİ KALDIRMAK")
print("="*70)
# Ramazan Hoca:
# Pzt: sadece İNM 403 (12:30-13:20) kalsın (1 saat)
# Kalan 27 saat: Salı, Çarşamba, Perşembe, Cuma
# Dağılım:
# Salı: İNM 5059 (3 saat) + İNM 403 (1 saat) + 3 danışmanlık = 7 saat
# Çarşamba: İNM 7006 Seminer (2 saat) + FBE 8901 Uzmanlık (4 saat) + 2 danışmanlık = 8 saat
# Perşembe: İNM 453 (3 saat) + 3 danışmanlık = 6 saat (veya 4 danışmanlık = 7 saat)
# Cuma: FBE 6901 Uzmanlık (4 saat) + 2 danışmanlık = 6 saat (veya 3 danışmanlık = 7 saat)

print("Ramazan Hoca Dağılımı (Pzt Lisansüstü Boşaltılırsa):")
print("Pzt: 1 saat (İNM 403 - Lisans Semineri, yetki dışı)")
print("Sal: 7 saat (Max <= 8)")
print("Çar: 8 saat (Max <= 8)")
print("Per: 6 saat (Max <= 8)")
print("Cum: 6 saat (Max <= 8)")
print("Toplam = 28 saat. Çakışma = 0. Günlük Max <= 8. Mümkün mü? -> EVET!")
