import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))

import openpyxl, xml.etree.ElementTree as ET
from collections import defaultdict
from generate_schedule import load_and_schedule, TEACHERS, TIME_SLOTS, DAYS

schedule, students_info = load_and_schedule()

print("--- YETKİ VE DERS TÜRÜ KONTROLÜ ---")

for t_id in [7, 9]:
    t_info = TEACHERS[t_id]
    print(f"\nŞube {t_id}: {t_info['title']}")
    
    # Cuma günündeki dersler
    cuma_dersleri = [schedule[t_id][4][sl] for sl in range(9) if schedule[t_id][4][sl] is not None]
    print(f"CUMA GÜNÜNDEKİ DERSLER (Toplam {len(cuma_dersleri)} saat):")
    for e in cuma_dersleri:
        print(f"   * {e['code']} - {e['name']} | Tür: {e['type']} | Değiştirme Yetkiniz Var mı? -> {'EVET (Yetki Dahilinde)' if e['type'] in ('Uzmanlık', 'Danışmanlık', 'Seminer') else 'HAYIR (Lisans/Seçmeli)'}")

    # Pazartesi günündeki dersler
    pzt_dersleri = [schedule[t_id][0][sl] for sl in range(9) if schedule[t_id][0][sl] is not None]
    print(f"\nPAZARTESİ GÜNÜNDEKİ DERSLER (Toplam {len(pzt_dersleri)} saat):")
    for e in pzt_dersleri:
        print(f"   * {e['code']} - {e['name']} | Tür: {e['type']} | Değiştirme Yetkiniz Var mı? -> {'EVET (Yetki Dahilinde)' if e['type'] in ('Uzmanlık', 'Danışmanlık', 'Seminer') else 'HAYIR (Lisans/Seçmeli)'}")
