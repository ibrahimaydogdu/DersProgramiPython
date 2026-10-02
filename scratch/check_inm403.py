import sys, openpyxl
sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook('DersProgrami_Lisans.xlsx')
ws = wb.active

print(f"{'Ders Kodu':<10} {'Şube':<6} {'Adı':<25} {'Gün':<5} {'Başlangıç':<10} {'Bitiş':<10} {'Öğretim Üyesi'}")
print("-" * 80)
for row in ws.iter_rows(min_row=2, values_only=True):
    code = str(row[2])
    inst = str(row[20])
    if '403' in code or 'ÖZÇELİK' in inst.upper() or 'ERDAL' in inst.upper():
        print(f"{code:<10} {str(row[3]):<6} {str(row[4])[:24]:<25} {str(row[14]):<5} {str(row[6]):<10} {str(row[7]):<10} {inst}")
