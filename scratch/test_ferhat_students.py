import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))

import openpyxl, xml.etree.ElementTree as ET
from collections import defaultdict
from generate_schedule import load_and_schedule, TEACHERS, TIME_SLOTS, DAYS

schedule, students_info = load_and_schedule()

# Ferhat Hoca öğrencileri ve dersleri
# Danışmanlıklar:
# Osman Can Kaya (202451016001 - DR) -> FBE 9903
# Adriana Lizzette Cruz Quintanilla (202351016001 - DR) -> FBE 9913
# Ersin Kaçmaz (202351015014 - YL) -> FBE 6903
# Seçil Karaçalı (202551015010 - YL) -> FBE 6903
# Uzmanlık:
# Osman Can Kaya -> FBE 9901 (8 saat = 2x4 blok)

# Öğrencilerin seçmeli ders takvimleri:
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
ferhat_ogr_nos = ['202451016001', '202351016001', '202351015014', '202551015010']
for t in tree_ogr.getroot():
    ogr_no = t.findtext('DATATEXT4')
    if ogr_no in ferhat_ogr_nos:
        code = t.findtext('DATATEXT12')
        if code in elective_course_slots:
            for d, sl in elective_course_slots[code]:
                student_busy[ogr_no].add((d, sl))

print("Ferhat Hoca Danışmanlık Öğrencilerinin Meşgul Saatleri (Seçmeli Dersleri):")
for o in ferhat_ogr_nos:
    print(f"Öğr No: {o}, Meşgul Saatler: {sorted(list(student_busy[o]))}")
