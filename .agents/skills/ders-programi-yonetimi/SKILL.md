---
name: ders-programi-yonetimi
description: >-
  Akdeniz Üniversitesi İnşaat Mühendisliği lisansüstü ders programı motorunu (generate_schedule.py) çalıştırmak,
  öğretim üyesi taleplerini işlemek, yeni öğrenci veya ders eklemek, çakışma analizi yapmak ve Excel/Markdown
  çıktılarını güncellemek gerektiğinde bu skill'i kullanın.
---

# Lisansüstü Ders Programı Yönetimi ve Optimizasyonu

Bu kılavuz, Akdeniz Üniversitesi Mühendislik Fakültesi İnşaat Mühendisliği lisansüstü ders programlama sisteminin bakımını yapmak, yeni talepleri işlemek ve program çıktılarını yeniden üretmek için gerekli adım adım prosedürleri içerir.

---

## 1. İş Akışı Adımları

### Adım 1: Girdi Dosyalarının ve Talebin İncelenmesi
Yeni bir talep geldiğinde (örn: bir öğretim üyesinin gün/saat değişikliği, yeni kayıt olan bir öğrenci, sehven seçilen şube düzeltmesi):
1. İlgili öğretim üyesinin mevcut programını `DersProgrami_Kisisel.xlsx` veya [`MEMORY.md`](../../MEMORY.md) üzerinden kontrol edin.
2. Değişikliğin türünü belirleyin:
   - **Özel Saat Tercihi:** Hoca danışmanlık, seminer veya uzmanlık dersinin belirli bir günde yapılmasını istiyorsa.
   - **Şube/Öğrenci Düzeltmesi:** Öğrencinin danışman hoca yerine başka bir hocanın şubesini seçmesi durumu.
   - **Yeni Öğrenci/Ders Eklenmesi:** `DersiAlanOgrenciler.xml` içerisine yeni kayıt yansıması veya kod seviyesinde ekleme.

### Adım 2: `generate_schedule.py` Üzerinde Düzenleme Yapma
Değişiklikleri [`generate_schedule.py`](../../generate_schedule.py) dosyasında ilgili bölümlere ekleyin:

1. **Öğretim Üyesi Manuel Danışmanlık Talepleri:**
   - `manual_danismanlik_slots` sözlüğüne öğrenci numarası ve `(gün, slot)` çifti eklenir:
     ```python
     manual_danismanlik_slots = {
         'ÖĞRENCİ_NO': (gün_indeksi, slot_indeksi),  # 0=Pzt..4=Cum, 0=08:30..8=16:30
     }
     ```
2. **Öğretim Üyesi Seminer Talepleri:**
   - `manual_seminar_slots` sözlüğüne hoca şube numarası ve `(gün, slot1, slot2)` eklenir:
     ```python
     manual_seminar_slots = {
         t_id: (gün_indeksi, ilk_slot, ikinci_slot), # 2 saatlik ardışık blok
     }
     ```
3. **Uzmanlık Alan Dersi Blok Sabitlemeleri:**
   - `manual_uzmanlik_slots` sözlüğüne hedef gün ve 4'er saatlik slot penceresi eklenir:
     ```python
     manual_uzmanlik_slots = {
         t_id: [(hedef_gün, (0, 1, 2, 3))], # Sabah: 0..3, Öğleden sonra: 5..8
     }
     ```
4. **Öğrenci Şube ve Mükerrer Kayıt Düzeltmeleri:**
   - `load_and_schedule()` fonksiyonundaki `DersiAlanOgrenciler.xml` döngüsü içerisine özel koşul eklenir (Furkan Ayan ve Fatma Aydemir örnekleri incelenebilir).

### Adım 3: Program Motorunu Çalıştırma
PowerShell terminalinde scripti çalıştırın:
```powershell
python generate_schedule.py
```

Başarılı çalıştırmada şu çıktı alınmalıdır:
```text
--- DERS PROGRAMI ÜRETİM MOTORU BAŞLATILIYOR ---
Kişisel ders programı dosyaları 'KisiselDersProgramlari' klasöründe işlendi.
DersProgrami_Kisisel.xlsx başarıyla üretildi.
DersProgrami_Otomasyon.xlsx başarıyla üretildi.
DersProgrami_Raporu.md başarıyla üretildi.

--- TÜM İŞLEMLER BAŞARIYLA TAMAMLANDI ---
```

### Adım 4: Doğrulama ve Raporlama Kontrolü
Script çalıştıktan sonra [`DersProgrami_Raporu.md`](../../DersProgrami_Raporu.md) dosyasını inceleyerek şu kriterleri teyit edin:
1. **Çakışma Durumu:** **0 (Sıfır Çakışma)** olmalıdır.
2. **Günlük Maksimum Ders Yükü:** Tabloda tüm hocalar için `Max <= 8` ifadesinin korunduğundan emin olun.
3. **Toplam Ders Yükleri:** Bölüm içi ve genel toplam saatlerinin doğruluğunu kontrol edin.

---

## 2. Karşılaşılabilecek Sorunlar ve Çözümleri

### 1. `PermissionError: [Errno 13] Permission denied: 'DersProgrami_...xlsx'`
- **Neden:** Excel dosyası kullanıcı veya bir program tarafından açık tutulmaktadır.
- **Çözüm:** Kullanıcıya dosyayı kapatmasını bildirin veya dosyanın kapanmasını bekleyin. Script otomatik uyarı verip çökmeden işlemi tamamlar.

### 2. Öğrenci veya Hoca Saat Çakışması
- **Neden:** Manuel atanan bir saat, öğrencinin seçmeli dersiyle veya hocanın lisans dersiyle çakışmaktadır.
- **Çözüm:**
  - İlgili öğrencinin `LisansüstüDersProgramiSecmeli.xml` dosyasındaki ders saatlerini kontrol edin.
  - Danışmanlık için uç saatleri (`08:30`, `12:30`, `16:30`) tercih edin.
  - Günlük toplam ders saati 8'e ulaşmamış boş günleri seçin.

### 3. İkinci Öğretim Derslerinin Otomasyona Sızması
- **Neden:** Tezsiz YL / İSG derslerinin yanlışlıkla `Lisansustu_Gorevlendirmeler` sayfasına aktarılması.
- **Çözüm:** `SECOND_EDUCATION_COURSES` değişkeninin `create_automation_excel()` fonksiyonunda filtrelemeye tabi tutulduğundan (`entry['type'] != 'TezsizYL'`) emin olun.
