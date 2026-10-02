import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))

from generate_schedule import load_and_schedule, TEACHERS, TIME_SLOTS, DAYS

schedule, students_info = load_and_schedule()

print("="*60)
print("1. PROF. DR. RAMAZAN ÖZÇELİK (Şube 7)")
print("="*60)
t7_courses = []
for d in range(5):
    for sl in range(9):
        e = schedule[7][d][sl]
        if e:
            t7_courses.append((d, sl, e))

print(f"Toplam Saat: {len(t7_courses)}")
lisans_sec_7 = [(d, sl, e) for d, sl, e in t7_courses if e['type'] in ('Lisans', 'Seçmeli')]
print(f"Fakülte/Bölüm Tarafından Sabitlenmiş Lisans ve Seçmeli Dersler:")
for d, sl, e in lisans_sec_7:
    print(f"   - {DAYS[d]} {TIME_SLOTS[sl][0]}-{TIME_SLOTS[sl][1]}: {e['code']} ({e['type']}, {e['name']})")

print("\n" + "="*60)
print("2. PROF. DR. FERHAT ERDAL (Şube 9)")
print("="*60)
t9_courses = []
for d in range(5):
    for sl in range(9):
        e = schedule[9][d][sl]
        if e:
            t9_courses.append((d, sl, e))

print(f"Toplam Saat: {len(t9_courses)}")
lisans_sec_9 = [(d, sl, e) for d, sl, e in t9_courses if e['type'] in ('Lisans', 'Seçmeli')]
print(f"Fakülte/Bölüm Tarafından Sabitlenmiş Lisans ve Seçmeli Dersler:")
for d, sl, e in lisans_sec_9:
    print(f"   - {DAYS[d]} {TIME_SLOTS[sl][0]}-{TIME_SLOTS[sl][1]}: {e['code']} ({e['type']}, {e['name']})")
