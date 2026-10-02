import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))

from generate_schedule import load_and_schedule, TEACHERS, TIME_SLOTS, DAYS

schedule, students_info = load_and_schedule()

print("--- YENİ YERLEŞİM SİMÜLASYONU (SADECE UZMANLIK VE DANIŞMANLIK DEĞİŞTİRİLEREK) ---")

# 1. Ferhat Erdal Cuma dersini (FBE 9901 4 saat) Salı 13:30-17:20'ye alabilir miyiz?
# Salı 13:30-17:20 boş mu?
free_sal_ferhat = all(schedule[9][1][sl] is None for sl in [5, 6, 7, 8])
print(f"Ferhat Hoca Salı 13:30-17:20 (Slot 5..8) Boş mu? -> {free_sal_ferhat}")

# 2. Ramazan Özçelik Cuma dersini (FBE 6901 4 saat) Çarşamba 13:30-17:20'ye alabilir miyiz?
# Çarşamba slot 5,6,7 boş, slot 8'de Ersin Karaman var. Ersin Karaman'ı Pazartesi 13:30'a alırsak Çarşamba 13:30-17:20 tamamen boşalır mı?
print(f"Ramazan Hoca Çarşamba 13:30-16:20 (Slot 5..7) Boş mu? -> {all(schedule[7][2][sl] is None for sl in [5, 6, 7])}")
print(f"Ramazan Hoca Pazartesi 13:30-16:20 (Slot 5..7) Boş mu? -> {all(schedule[7][0][sl] is None for sl in [5, 6, 7])}")
print(f"Ramazan Hoca Perşembe 09:30-12:20 (Slot 1..3) Boş mu? -> {all(schedule[7][3][sl] is None for sl in [1, 2, 3])}")
