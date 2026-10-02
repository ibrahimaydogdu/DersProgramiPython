import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))

import openpyxl, xml.etree.ElementTree as ET
from collections import defaultdict
from generate_schedule import load_and_schedule, TEACHERS, TIME_SLOTS, DAYS

schedule, students_info = load_and_schedule()

# Ramazan Hoca öğrencileri ve meşgul saatleri
tree_sec = ET.parse('LisansüstüDersProgramiSecmeli.xml')
tree_ogr = ET.parse('DersiAlanOgrenciler.xml')

elective_course_slots = defaultdict(list)
for t in tree_sec.getroot():
    code = t.findtext('DATATEXT2')
    day = int(t.findtext('DATATEXT14'))
    st = str(t.findtext('DATATEXT6')).strip()
    if len(st) == 4: st = '0' + st
    slot = {'08:30':0, '09:30':1, '10:30':2, '11:30':3, '12:30':4, '13:30':5, '14:30':6, '15:30':7, '16:30':8}.get(st)
    if slot is not None and 0 <= day < 5:
        elective_course_slots[code].append((day, slot))

student_busy = defaultdict(set)
ramazan_students = []
for t in tree_ogr.getroot():
    sube = int(t.findtext('DATATEXT11'))
    if sube % 100 == 7:
        ogr_no = t.findtext('DATATEXT4')
        ogr_ad = ((t.findtext('DATATEXT5') or '') + ' ' + (t.findtext('DATATEXT6') or '')).strip()
        code = t.findtext('DATATEXT12')
        cname = t.findtext('DATATEXT13') or ''
        ramazan_students.append((ogr_no, ogr_ad, code, cname))
        if code in elective_course_slots:
            for d, sl in elective_course_slots[code]:
                student_busy[ogr_no].add((d, sl))

print("Ramazan Hoca Öğrencileri ve Meşgul Saatleri:")
unique_ogrs = {o[0]: o[1] for o in ramazan_students}
for o_no, o_ad in unique_ogrs.items():
    print(f"  - {o_ad} ({o_no}): Meşgul -> {sorted(list(student_busy[o_no]))}")

# Şimdi Ramazan Hoca'nın Cuma gününü boşaltıp dersleri diğer günlere dağıtabilir miyiz kontrol edelim
# Mevcut saatler:
# Pzt: 6 saat
# Sal: 6 saat
# Çar: 4 saat
# Per: 6 saat
# Cum: 6 saat (FBE 6901 4 saat, Hacı Tıkna 1 saat, Beyza Aytaç 1 saat)
# Kalan 4 günün kapasitesi:
# Pzt: 6 -> 8 (+2 boş)
# Sal: 6 -> 8 (+2 boş)
# Çar: 4 -> 8 (+4 boş)
# Per: 6 -> 8 (+2 boş)
# Toplam boş kapasite: 2 + 2 + 4 + 2 = 10 saat! Cuma'daki 6 saat rahatlıkla sığabilir!
print("\nKapasite Analizi (Cuma Boşaltılırsa):")
print("Pzt (Mevcut 6) -> 8'e kadar +2 yer var")
print("Sal (Mevcut 6) -> 8'e kadar +2 yer var")
print("Çar (Mevcut 4) -> 8'e kadar +4 yer var (FBE 6901 4 saatlik blok tam buraya gelebilir!)")
print("Per (Mevcut 6) -> 8'e kadar +2 yer var")
print("Toplam boş kapasite: 10 saat (Cuma'daki 6 saat için yeterli!)")
