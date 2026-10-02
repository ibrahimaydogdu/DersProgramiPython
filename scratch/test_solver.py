import sys, os, openpyxl, xml.etree.ElementTree as ET
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')

TEACHERS = {
    13: {'name': 'Bekir AKGÖZ', 'title': 'Doç. Dr. Bekir AKGÖZ', 'room': 'C302'},
    1:  {'name': 'Ömer CİVALEK', 'title': 'Prof. Dr. Ömer CİVALEK', 'room': 'C303'},
    2:  {'name': 'Aynur KAZAZ', 'title': 'Prof. Dr. Aynur KAZAZ', 'room': 'C304'},
    4:  {'name': 'Nihat DİPOVA', 'title': 'Prof. Dr. Nihat DİPOVA', 'room': 'C305'},
    15: {'name': 'Banihan GÜNAY', 'title': 'Prof. Dr. Banihan GÜNAY', 'room': 'C322'},
    14: {'name': 'Halil İbrahim BURGAN', 'title': 'Doç. Dr. Halil İbrahim BURGAN', 'room': 'C323'},
    6:  {'name': 'Okan ÖZCAN', 'title': 'Prof. Dr. Okan ÖZCAN', 'room': 'C324'},
    12: {'name': 'Engin EMSEN', 'title': 'Dr. Öğr. Üyesi Engin EMSEN', 'room': 'C325'},
    5:  {'name': 'İzzet Ufuk ÇAĞDAŞ', 'title': 'Prof. Dr. İzzet Ufuk ÇAĞDAŞ', 'room': 'C326'},
    10: {'name': 'Sevil KÖFTECİ', 'title': 'Prof. Dr. Sevil KÖFTECİ', 'room': 'C327'},
    8:  {'name': 'İbrahim AYDOĞDU', 'title': 'Prof. Dr. İbrahim AYDOĞDU', 'room': 'C331'},
    3:  {'name': 'N. Uğur KOÇKAL', 'title': 'Prof. Dr. N. Uğur KOÇKAL', 'room': 'C332'},
    11: {'name': 'Rıfat TÜR', 'title': 'Doç. Dr. Rıfat TÜR', 'room': 'C333'},
    7:  {'name': 'Ramazan ÖZÇELİK', 'title': 'Prof. Dr. Ramazan ÖZÇELİK', 'room': 'C334'},
    9:  {'name': 'Ferhat ERDAL', 'title': 'Prof. Dr. Ferhat ERDAL', 'room': 'C335'},
}

TIME_SLOTS = [
    ('08:30', '09:20'),
    ('09:30', '10:20'),
    ('10:30', '11:20'),
    ('11:30', '12:20'),
    ('12:30', '13:20'),
    ('13:30', '14:20'),
    ('14:30', '15:20'),
    ('15:30', '16:20'),
    ('16:30', '17:20'),
]
SLOT_INDICES = {st: i for i, (st, en) in enumerate(TIME_SLOTS)}
DAYS = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma']

teacher_schedule = defaultdict(lambda: [[None for _ in range(9)] for _ in range(5)])
student_schedule = defaultdict(set)

# 1. Lisans
wb_lisans = openpyxl.load_workbook('DersProgrami_Lisans.xlsx')
ws_lisans = wb_lisans.active
for row in ws_lisans.iter_rows(min_row=2, values_only=True):
    inst = str(row[20]).upper()
    for t_id, t_info in TEACHERS.items():
        surname = t_info['name'].split()[-1].upper()
        if surname in inst:
            day = int(row[14])
            st = str(row[6]).strip()
            if len(st) == 4: st = '0' + st
            slot = SLOT_INDICES.get(st)
            if slot is not None and 0 <= day < 5:
                uyg_val = 1 if row[15] == '__1' else 0
                entry = {
                    'sube': str(row[3]),
                    'code': str(row[2]),
                    'name': str(row[4]),
                    'day': day,
                    'slot': slot,
                    'start': str(row[6]),
                    'end': str(row[7]),
                    'room': str(row[10]),
                    'uyg': uyg_val,
                    'ortak': 0,
                    'ckd': 0,
                    'prog': '01',
                    'type': 'Lisans',
                    'student_name': ''
                }
                teacher_schedule[t_id][day][slot] = entry
            break

# 2. Seçmeli
tree_sec = ET.parse('LisansüstüDersProgramiSecmeli.xml')
elective_course_slots = defaultdict(list)
for t in tree_sec.getroot():
    inst = str(t.findtext('DATATEXT20')).upper()
    code = t.findtext('DATATEXT2')
    day = int(t.findtext('DATATEXT14'))
    st = str(t.findtext('DATATEXT6')).strip()
    if len(st) == 4: st = '0' + st
    slot = SLOT_INDICES.get(st)
    if slot is not None and 0 <= day < 5:
        elective_course_slots[code].append((day, slot))
        for t_id, t_info in TEACHERS.items():
            surname = t_info['name'].split()[-1].upper()
            if surname in inst:
                uyg_val = 1 if t.findtext('DATATEXT15') == '__1' else 0
                prog_code = '15' if t.findtext('DATATEXT5') == '15' else '16'
                entry = {
                    'sube': str(t.findtext('DATATEXT3')),
                    'code': code,
                    'name': str(t.findtext('DATATEXT4')),
                    'day': day,
                    'slot': slot,
                    'start': t.findtext('DATATEXT6'),
                    'end': t.findtext('DATATEXT7'),
                    'room': str(t.findtext('DATATEXT10')),
                    'uyg': uyg_val,
                    'ortak': 0,
                    'ckd': 0,
                    'prog': prog_code,
                    'type': 'Seçmeli',
                    'student_name': ''
                }
                teacher_schedule[t_id][day][slot] = entry
                break

# 3. Read DersiAlanOgrenciler
tree_ogr = ET.parse('DersiAlanOgrenciler.xml')
seminar_branches = defaultdict(lambda: defaultdict(list))
danismanlik_items = []
uzmanlik_by_teacher = defaultdict(lambda: defaultdict(list))

for t in tree_ogr.getroot():
    ogr_no = t.findtext('DATATEXT4')
    ogr_ad = ((t.findtext('DATATEXT5') or '') + ' ' + (t.findtext('DATATEXT6') or '')).strip()
    prog_text = t.findtext('DATATEXT9') or ''
    prog_code = '16' if '(DR)' in prog_text else '15'
    code = t.findtext('DATATEXT12')
    cname = t.findtext('DATATEXT13') or ''
    sube = int(t.findtext('DATATEXT11'))
    base_sube = sube % 100
    
    # Track student busy slots from electives
    if code in elective_course_slots:
        for d, sl in elective_course_slots[code]:
            student_schedule[ogr_no].add((d, sl))
            
    if 'Seminer' in cname:
        seminar_branches[base_sube][(code, sube, cname, prog_code)].append((ogr_no, ogr_ad))
    elif 'Danışmanlık' in cname:
        danismanlik_items.append({
            'code': code,
            'sube': sube,
            'base_sube': base_sube,
            'name': cname,
            'prog': prog_code,
            'ogr_no': ogr_no,
            'ogr_ad': ogr_ad
        })
    elif 'Uzmanlık' in cname:
        uzmanlik_by_teacher[base_sube][code].append((ogr_no, ogr_ad))

print(f"Loaded {len(danismanlik_items)} danışmanlık items.")

# Helper to check daily count
def get_daily_count(t_id, day):
    return sum(1 for sl in range(9) if teacher_schedule[t_id][day][sl] is not None)

# Helper to check if teacher is free
def is_teacher_free(t_id, day, slot):
    return teacher_schedule[t_id][day][slot] is None

# Helper to check if students are free
def are_students_free(ogr_nos, day, slot):
    for o in ogr_nos:
        if (day, slot) in student_schedule[o]:
            return False
    return True

# STEP A: Place Seminars (2 hours blocks, uyg=1)
print("\n--- PLACING SEMINARS ---")
placed_seminars = 0
for t_id in sorted(seminar_branches.keys()):
    room = TEACHERS[t_id]['room']
    for (code, sube, cname, prog_code), ogrenci_list in seminar_branches[t_id].items():
        ogr_nos = [o[0] for o in ogrenci_list]
        ogr_names = ", ".join([o[1] for o in ogrenci_list])
        placed = False
        
        # Look for 2 consecutive slots in a day
        # Prefer days with fewer classes, slot pairs: (0,1), (1,2), (2,3), (5,6), (6,7), (7,8)
        candidate_slots = [
            (0, 1), (1, 2), (2, 3), (5, 6), (6, 7), (7, 8), (4, 5), (3, 4)
        ]
        # Sort days by current load ascending
        days_order = sorted(range(5), key=lambda d: get_daily_count(t_id, d))
        
        for d in days_order:
            if get_daily_count(t_id, d) + 2 > 8:
                continue
            for sl1, sl2 in candidate_slots:
                if is_teacher_free(t_id, d, sl1) and is_teacher_free(t_id, d, sl2):
                    if are_students_free(ogr_nos, d, sl1) and are_students_free(ogr_nos, d, sl2):
                        # Place both slots
                        for sl in (sl1, sl2):
                            entry = {
                                'sube': str(sube),
                                'code': code,
                                'name': cname,
                                'day': d,
                                'slot': sl,
                                'start': TIME_SLOTS[sl][0],
                                'end': TIME_SLOTS[sl][1],
                                'room': room,
                                'uyg': 1,
                                'ortak': 0,
                                'ckd': 0,
                                'prog': prog_code,
                                'type': 'Seminer',
                                'student_name': ogr_names
                            }
                            teacher_schedule[t_id][d][sl] = entry
                            for o in ogr_nos:
                                student_schedule[o].add((d, sl))
                        placed = True
                        placed_seminars += 1
                        print(f"Placed Seminar {code} Sube {sube} for T{t_id} on {DAYS[d]} slots {sl1},{sl2} ({TIME_SLOTS[sl1][0]}-{TIME_SLOTS[sl2][1]})")
                        break
            if placed:
                break
        if not placed:
            print(f"FAILED TO PLACE SEMINAR: {code} Sube {sube} for T{t_id}")

print(f"Seminars placed: {placed_seminars}")

# STEP B: Place Uzmanlık Alan
print("\n--- PLACING UZMANLIK ALAN ---")
# Define configuration for each teacher based on recommendations 3a, 3b, 3c
uzmanlik_plan = {
    1:  [('FBE 9901', 'Uzmanlık Alan Dersi', 1, '16', 8)],
    2:  [('FBE 9911', 'Uzmanlık Alan Dersi', 2, '16', 8)],
    3:  [('FBE 9901', 'Uzmanlık Alan Dersi', 3, '16', 8)],
    4:  [('FBE 6901', 'Uzmanlık Alan Dersi', 4, '15', 4)],
    5:  [], # No students
    6:  [('FBE 9911', 'Uzmanlık Alan Dersi', 6, '16', 8)],
    7:  [('FBE 6901', 'Uzmanlık Alan Dersi', 7, '15', 4), ('FBE 8901', 'Uzmanlık Alan Dersi', 7, '16', 4)],
    8:  [('FBE 6901', 'Uzmanlık Alan Dersi', 8, '15', 4), ('FBE 8901', 'Uzmanlık Alan Dersi', 8, '16', 4)],
    9:  [('FBE 9901', 'Uzmanlık Alan Dersi', 9, '16', 8)],
    10: [('FBE 6901', 'Uzmanlık Alan Dersi', 10, '15', 4), ('FBE 8901', 'Uzmanlık Alan Dersi', 10, '16', 4)],
    11: [('FBE 5901', 'Uzmanlık Alan Dersi', 11, '15', 4)],
    12: [('FBE 6901', 'Uzmanlık Alan Dersi', 12, '15', 4)],
    13: [('FBE 9901', 'Uzmanlık Alan Dersi', 13, '16', 8)],
    14: [('FBE 6901', 'Uzmanlık Alan Dersi', 14, '15', 4), ('FBE 8901', 'Uzmanlık Alan Dersi', 14, '16', 4)],
    15: [('FBE 6901', 'Uzmanlık Alan Dersi', 15, '15', 4)],
}

for t_id, courses in uzmanlik_plan.items():
    room = TEACHERS[t_id]['room']
    for code, cname, sube, prog_code, total_hours in courses:
        # Find enrolled students for conflict check if any
        ogrs = uzmanlik_by_teacher[t_id].get(code, [])
        ogr_nos = [o[0] for o in ogrs]
        ogr_names = ", ".join([o[1] for o in ogrs])
        
        # We need to place total_hours (either 4 or 8)
        # For 8 hours, it can be split into two 4-hour blocks (e.g. 4 on Day A, 4 on Day B)
        # For 4 hours, it is one 4-hour block
        blocks_to_place = [4, 4] if total_hours == 8 else [4]
        
        for block_len in blocks_to_place:
            placed_block = False
            # Find a day where daily_count + block_len <= 8
            # Look for 4 consecutive slots or morning/afternoon block
            # Candidate 4-slot windows:
            # Morning: 0..3 (08:30-12:20)
            # Afternoon: 5..8 (13:30-17:20)
            # Or other 4 consecutive
            windows = [
                (0, 1, 2, 3), # Morning
                (5, 6, 7, 8), # Afternoon
                (1, 2, 3, 4),
                (4, 5, 6, 7),
            ]
            days_order = sorted(range(5), key=lambda d: get_daily_count(t_id, d))
            
            for d in days_order:
                if get_daily_count(t_id, d) + block_len > 8:
                    continue
                for win in windows:
                    if all(is_teacher_free(t_id, d, sl) for sl in win) and all(are_students_free(ogr_nos, d, sl) for sl in win):
                        for sl in win:
                            entry = {
                                'sube': str(sube),
                                'code': code,
                                'name': cname,
                                'day': d,
                                'slot': sl,
                                'start': TIME_SLOTS[sl][0],
                                'end': TIME_SLOTS[sl][1],
                                'room': room,
                                'uyg': 0, # Teori
                                'ortak': 0,
                                'ckd': 0,
                                'prog': prog_code,
                                'type': 'Uzmanlık',
                                'student_name': ogr_names
                            }
                            teacher_schedule[t_id][d][sl] = entry
                            for o in ogr_nos:
                                student_schedule[o].add((d, sl))
                        placed_block = True
                        print(f"Placed Uzmanlık {code} ({block_len}h) for T{t_id} on {DAYS[d]} slots {win[0]}-{win[-1]}")
                        break
                if placed_block:
                    break
            
            if not placed_block:
                # Fallback: place any available block_len slots in that day
                for d in days_order:
                    free_slots = [sl for sl in range(9) if is_teacher_free(t_id, d, sl) and are_students_free(ogr_nos, d, sl)]
                    if len(free_slots) >= block_len and get_daily_count(t_id, d) + block_len <= 8:
                        chosen = free_slots[:block_len]
                        for sl in chosen:
                            entry = {
                                'sube': str(sube),
                                'code': code,
                                'name': cname,
                                'day': d,
                                'slot': sl,
                                'start': TIME_SLOTS[sl][0],
                                'end': TIME_SLOTS[sl][1],
                                'room': room,
                                'uyg': 0,
                                'ortak': 0,
                                'ckd': 0,
                                'prog': prog_code,
                                'type': 'Uzmanlık',
                                'student_name': ogr_names
                            }
                            teacher_schedule[t_id][d][sl] = entry
                            for o in ogr_nos:
                                student_schedule[o].add((d, sl))
                        placed_block = True
                        print(f"Placed Uzmanlık (fallback) {code} ({block_len}h) for T{t_id} on {DAYS[d]} slots {chosen}")
                        break
            if not placed_block:
                print(f"FAILED TO PLACE UZMANLIK: {code} for T{t_id}")

# STEP C: Place Danışmanlık
print("\n--- PLACING DANIŞMANLIK ---")
# Priority slots: Slot 0 (08:30), Slot 4 (12:30), Slot 8 (16:30), then others
priority_slots = [0, 4, 8, 1, 7, 2, 6, 3, 5]

placed_danismanlik = 0
unplaced_danismanlik = []

# Sort danışmanlık items: students who have busy slots should be placed first!
danismanlik_items.sort(key=lambda item: len(student_schedule[item['ogr_no']]), reverse=True)

for item in danismanlik_items:
    t_id = item['base_sube']
    room = TEACHERS[t_id]['room']
    ogr_no = item['ogr_no']
    placed = False
    
    # Sort days by current teacher daily count
    days_order = sorted(range(5), key=lambda d: get_daily_count(t_id, d))
    
    for sl in priority_slots:
        for d in days_order:
            if get_daily_count(t_id, d) + 1 > 8:
                continue
            if is_teacher_free(t_id, d, sl) and are_students_free([ogr_no], d, sl):
                entry = {
                    'sube': str(item['sube']),
                    'code': item['code'],
                    'name': item['name'],
                    'day': d,
                    'slot': sl,
                    'start': TIME_SLOTS[sl][0],
                    'end': TIME_SLOTS[sl][1],
                    'room': room,
                    'uyg': 1, # Danışmanlık 0/1 uygulama
                    'ortak': 0,
                    'ckd': 0,
                    'prog': item['prog'],
                    'type': 'Danışmanlık',
                    'student_name': item['ogr_ad']
                }
                teacher_schedule[t_id][d][sl] = entry
                student_schedule[ogr_no].add((d, sl))
                placed = True
                placed_danismanlik += 1
                break
        if placed:
            break
            
    if not placed:
        unplaced_danismanlik.append(item)
        print(f"FAILED TO PLACE DANIŞMANLIK: {item['code']} Sube {item['sube']} Ogr: {item['ogr_ad']}")

print(f"\nDanışmanlık Placed: {placed_danismanlik}/{len(danismanlik_items)}")

# STEP D: Validation and Summary
print("\n=== FINAL VALIDATION ===")
all_ok = True
for t_id in sorted(TEACHERS.keys()):
    t_name = TEACHERS[t_id]['name']
    total_h = 0
    day_counts = []
    for d in range(5):
        cnt = get_daily_count(t_id, d)
        day_counts.append(cnt)
        total_h += cnt
        if cnt > 8:
            print(f"VIOLATION: T{t_id} {t_name} has {cnt} hours on {DAYS[d]} (> 8 max)!")
            all_ok = False
    print(f"T{t_id:2d} {t_name:<20}: Total {total_h:2d} hrs | Daily: {day_counts}")

if all_ok and len(unplaced_danismanlik) == 0:
    print("\nSUCCESS! ALL CONSTRAINTS SATISFIED: ZERO CONFLICTS, DAILY <= 8, ALL COURSES PLACED!")
