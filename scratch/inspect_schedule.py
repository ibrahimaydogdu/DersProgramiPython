import sys, os, openpyxl, xml.etree.ElementTree as ET
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')

teachers_map = {
    13: ('Bekir AKGÖZ', 'C302'), 1: ('Ömer CİVALEK', 'C303'), 2: ('Aynur KAZAZ', 'C304'),
    4: ('Nihat DİPOVA', 'C305'), 15: ('Banihan GÜNAY', 'C322'), 14: ('Halil İbrahim BURGAN', 'C323'),
    6: ('Okan ÖZCAN', 'C324'), 12: ('Engin EMSEN', 'C325'), 5: ('İzzet Ufuk ÇAĞDAŞ', 'C326'),
    10: ('Sevil KÖFTECİ', 'C327'), 8: ('İbrahim AYDOĞDU', 'C331'), 3: ('N. Uğur KOÇKAL', 'C332'),
    11: ('Rıfat TÜR', 'C333'), 7: ('Ramazan ÖZÇELİK', 'C334'), 9: ('Ferhat ERDAL', 'C335')
}

time_slots = [
    '08:30-09:20', '09:30-10:20', '10:30-11:20', '11:30-12:20',
    '12:30-13:20', '13:30-14:20', '14:30-15:20', '15:30-16:20', '16:30-17:20'
]
slot_indices = {s.split('-')[0]: i for i, s in enumerate(time_slots)}
days = ['Pzt', 'Sal', 'Çar', 'Per', 'Cum']

grids = {s: [[None for _ in range(9)] for _ in range(5)] for s in teachers_map}

# 1. Lisans
wb = openpyxl.load_workbook('DersProgrami_Lisans.xlsx')
ws = wb.active
for row in ws.iter_rows(min_row=2, values_only=True):
    inst = str(row[20]).upper()
    for s, (tname, room) in teachers_map.items():
        if tname.split()[-1].upper() in inst:
            day = int(row[14])
            st = str(row[6]).strip()
            if len(st) == 4: st = '0' + st
            slot = slot_indices.get(st)
            if slot is not None and 0 <= day < 5:
                grids[s][day][slot] = f"{row[2]}(L)"
            break

# 2. Secmeli
tree_sec = ET.parse('LisansüstüDersProgramiSecmeli.xml')
for t in tree_sec.getroot():
    inst = str(t.findtext('DATATEXT20')).upper()
    for s, (tname, room) in teachers_map.items():
        if tname.split()[-1].upper() in inst:
            day = int(t.findtext('DATATEXT14'))
            st = str(t.findtext('DATATEXT6')).strip()
            if len(st) == 4: st = '0' + st
            slot = slot_indices.get(st)
            code = t.findtext('DATATEXT2')
            if slot is not None and 0 <= day < 5:
                grids[s][day][slot] = f"{code}(S)"
            break

for s in sorted(teachers_map.keys()):
    tname, room = teachers_map[s]
    busy = sum(1 for d in range(5) for sl in range(9) if grids[s][d][sl] is not None)
    print(f"=== Sube {s:2d}: {tname} ({room}) | Current Busy Slots: {busy}/45 ===")
    for d_idx, d_name in enumerate(days):
        cells = []
        for sl in range(9):
            val = grids[s][d_idx][sl]
            cells.append(f"[{val:^11}]" if val else "[     .     ]")
        day_str = " ".join(cells)
        daily_count = sum(1 for sl in range(9) if grids[s][d_idx][sl] is not None)
        print(f"  {d_name}: {day_str} ({daily_count}/8 max)")
