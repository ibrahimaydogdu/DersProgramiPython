import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))

from generate_schedule import load_and_schedule, TEACHERS, TIME_SLOTS, DAYS

schedule, students_info = load_and_schedule()

print("Mevcut Günlük Dağılım:")
for t_id in [7, 9]:
    daily = [sum(1 for sl in range(9) if schedule[t_id][d][sl] is not None) for d in range(5)]
    print(f"Şube {t_id} ({TEACHERS[t_id]['title']}): Toplam {sum(daily)} saat -> Pzt:{daily[0]}, Sal:{daily[1]}, Çar:{daily[2]}, Per:{daily[3]}, Cum:{daily[4]}")
