import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))

from generate_schedule import load_and_schedule, TEACHERS, TIME_SLOTS, DAYS

schedule, students_info = load_and_schedule()

for t_id in [7, 9]:
    t_info = TEACHERS[t_id]
    print(f"==================================================")
    print(f"Şube {t_id}: {t_info['title']} (Oda: {t_info['room']})")
    print(f"==================================================")
    for d_idx, d_name in enumerate(DAYS):
        courses_in_day = []
        for sl_idx in range(9):
            e = schedule[t_id][d_idx][sl_idx]
            if e:
                courses_in_day.append(f"{TIME_SLOTS[sl_idx][0]}-{TIME_SLOTS[sl_idx][1]} [Slot {sl_idx}]: {e['code']} ({e['type']}, {e['name']}) - Öğr: {e.get('student_name','')}")
        print(f"\n{d_name} (Toplam {len(courses_in_day)} saat):")
        for c in courses_in_day:
            print(f"   * {c}")
    print("\n")
