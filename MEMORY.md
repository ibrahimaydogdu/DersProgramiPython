# İnşaat Mühendisliği Ders Programı Hafıza ve Bilgi Bankası (MEMORY.md)

Bu dosya, sonraki promptlar ve geliştirme adımları için bölüm öğretim üyeleri, derslikler, özel tercihler, tarihsel hata düzeltmeleri ve veri şemalarına ait kalıcı hafıza kaydıdır.

---

## 1. Öğretim Üyeleri ve Derslik Bilgi Matrisi

| Şube No (`t_id`) | Ünvan ve Ad Soyad | Çalışma Odası / Derslik | Uzmanlık Türü / Saati | Danışmanlık Sayısı | Seminer Şube | İkinci Öğretim (İSG Tezsiz YL) | Toplam Yük |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | Prof. Dr. Ömer CİVALEK | C303 | 8 Saat (FBE 9901 - DR) | 7 Şube | 1 Şube (2 Saat) | - | 29 Saat |
| **2** | Prof. Dr. Aynur KAZAZ | C304 | 8 Saat (FBE 9911 - DR) | 7 Şube | 1 Şube (2 Saat) | 8 Saat (Salı/Cuma Akşam) | 39 Saat (31 Bölüm + 8 İSG) |
| **3** | Prof. Dr. N. Uğur KOÇKAL | C332 | 8 Saat (FBE 9901 - DR) | 8 Şube | 0 Şube | 5 Saat (Pzt/Cuma Akşam) | 35 Saat (30 Bölüm + 5 İSG) |
| **4** | Prof. Dr. Nihat DİPOVA | C305 | 4 Saat (FBE 6901 - YL) | 5 Şube | 1 Şube (2 Saat) | - | 22 Saat |
| **5** | Prof. Dr. İzzet Ufuk ÇAĞDAŞ | C326 | 4 Saat (FBE 5901 - YL) | 1 Şube | 0 Şube | - | 19 Saat |
| **6** | Prof. Dr. Okan ÖZCAN | C324 | 8 Saat (FBE 9911 - DR) | 6 Şube | 2 Şube (4 Saat) | - | 30 Saat |
| **7** | Prof. Dr. Ramazan ÖZÇELİK | C334 | 8 Saat (4 YL + 4 DR) | 10 Şube | 1 Şube (2 Saat) | - | 28 Saat |
| **8** | Prof. Dr. İbrahim AYDOĞDU | C331 | 8 Saat (4 YL + 4 DR) | 5 Şube | 1 Şube (2 Saat) | - | 27 Saat |
| **9** | Prof. Dr. Ferhat ERDAL | C335 | 8 Saat (FBE 9901 - DR) | 4 Şube | 0 Şube | - | 23 Saat |
| **10** | Prof. Dr. Sevil KÖFTECİ | C327 | 8 Saat (4 YL + 4 DR) | 5 Şube | 1 Şube (2 Saat) | - | 17 Saat |
| **11** | Doç. Dr. Rıfat TÜR | C333 | 4 Saat (FBE 5901 - YL) | 4 Şube | 1 Şube (2 Saat) | - | 21 Saat |
| **12** | Dr. Öğr. Üyesi Engin EMSEN | C325 | 4 Saat (FBE 6901 - YL) | 2 Şube | 1 Şube (2 Saat) | - | 17 Saat |
| **13** | Doç. Dr. Bekir AKGÖZ | C302 | 8 Saat (FBE 9901 - DR) | 5 Şube | 1 Şube (2 Saat) | - | 28 Saat |
| **14** | Doç. Dr. Halil İbrahim BURGAN | C323 | 7 Saat (3 YL + 4 DR) | 12 Şube | 2 Şube (4 Saat) | - | 37 Saat |
| **15** | Prof. Dr. Banihan GÜNAY | C322 | 4 Saat (FBE 6901 - YL) | 6 Şube | 1 Şube (2 Saat) | - | 26 Saat |
| - | *Seminer Salonu* | *C328* | - | - | - | - | - |

---

## 2. Belgelenmiş İstisnalar ve Tarihsel Düzeltmeler

Sistemde uygulanan ve kod içerisine işlenmiş özel düzeltmeler şunlardır:

1. **Furkan Ayan (Öğr. No: 202551015021) Şube Düzeltmesi:**
   - Öğrenci OBS sisteminde Seminer I dersi şubesini sehven `1` (Prof. Dr. Ömer Civalek) olarak seçmiştir.
   - Asıl tez danışmanı Doç. Dr. Halil İbrahim BURGAN (Şube: 14) olduğundan, öğrencinin seminer şubesi kod seviyesinde `14` olarak düzeltilmiş ve Burgan hocanın seminer grubuna aktarılmıştır.

2. **Fatma Aydemir (Öğr. No: 202551015006) Mükerrer Kayıt Düzeltmesi:**
   - Öğrencinin OBS sisteminde hem ders aşaması (`FBE 5901` ve `FBE 5903` - 11.09.2026) hem de tez aşaması (`FBE 6901` ve `FBE 6903` - 18.09.2026) mükerrer kayıtları mevcuttur.
   - Kullanıcı talimatı doğrultusunda geçersiz ders dönemi kayıtları elenmiş; yalnızca geçerli tez danışmanlığı (`FBE 6903` - Şube 3) Prof. Dr. N. Uğur KOÇKAL'ın programına işlenmiştir.

3. **Ekrem Bakır Şube Düzeltmesi:**
   - Prof. Dr. İzzet Ufuk ÇAĞDAŞ'ın öğrencisi Ekrem Bakır'ın ders seçiminde şube sehven `8` olarak girilmiştir. Şube `5` olarak düzeltilmiş ve hocaya 4 saat `FBE 5901` tanımlanmıştır.

4. **Doç. Dr. Bekir AKGÖZ Seminer Sabitlemesi:**
   - Evindar Kaya Eren'in seminer dersi hocanın talebiyle **Pazartesi 10:30-12:20** (Slot 2 ve 3) olarak sabitlenmiştir.

5. **Prof. Dr. Nihat DİPOVA Çakışma ve Gün Dengelemesi:**
   - Seminer dersi **Perşembe 13:30-15:20** (C305) olarak sabitlenerek öğrencinin JEO 5041 (09:30-12:20) çakışması önlenmiştir.
   - İNM 403 Lisans Seminer Çalışması (Şube 5) Pazartesi 12:30 ve Salı 12:30 saatlerinde korunmuştur.
   - 5 lisansüstü danışmanlığı Salı gününe toplanmıştır (08:30 Kayaoğlu, 09:30 Altan, 10:30 Ceylan, 11:30 Yılmaz, 13:30 Özçelik).

6. **Prof. Dr. N. Uğur KOÇKAL Günlük Yük Dengelemesi:**
   - Çarşamba sabahı ve Perşembe sabahı 08:30-12:20 saatleri 4'er saat Uzmanlık Alan Dersi olarak sabitlenmiştir.
   - Çarşamba sabah 08:30 ve 12:30 danışmanlıkları Cuma gününe kaydırılarak Çarşamba gününün yükü 8 saatte dengelenmiştir.

7. **Doç. Dr. Halil İbrahim BURGAN Özel Danışmanlık Saatleri:**
   - Mustafa SİR (İklim Değişikliği YL - 202551096010): Pazartesi 08:30 (Slot 0).
   - Rogers Nyonbior Gwiah (202451015008): Salı 11:30 (Slot 3).

---

## 3. İkinci Öğretim Ek Görevlendirmeleri Matrisi

Bu görevler FBE İş Sağlığı ve Güvenliği Tezsiz YL programına ait olup **otomasyon Excel'ine dahil edilmez**:

- **Prof. Dr. Aynur KAZAZ (Şube: 2 - Toplam 8 Saat):**
  - Salı 17:30 - 20:10 (3 saat) - C213: *İnşaat İşlerinde İş Sağlığı ve Güvenliği (Seçimli)*
  - Salı 20:15 - 22:55 (3 saat) - C213: *İş Kazaları ve Tahkikat Süreci (Zorunlu)*
  - Cuma 17:30 - 19:15 (2 saat) - Dersin Hocası: *Dönem Projesi (Proje)*
- **Prof. Dr. Niyazi Uğur KOÇKAL (Şube: 3 - Toplam 5 Saat):**
  - Pazartesi 17:30 - 20:10 (3 saat) - C213: *Yangından Korunma Yöntemleri (Seçimli)*
  - Cuma 17:30 - 19:15 (2 saat) - Dersin Hocası: *Dönem Projesi (Proje)*

---

## 4. Girdi Veri Şemaları

### A. `DersProgrami_Lisans.xlsx` (Örgün Lisans Programı)
- `row[2]`: Ders Kodu
- `row[3]`: Şube Kodu
- `row[4]`: Ders Adı
- `row[6]`: Başlangıç Saati (`08:30`)
- `row[7]`: Bitiş Saati (`09:20`)
- `row[10]`: Derslik Kodu
- `row[14]`: Gün (0=Pzt..4=Cum)
- `row[15]`: Uygulama mı (`__1` ise 1, aksi 0)
- `row[20]`: Öğretim Görevlisi Adı/Soyadı

### B. `LisansüstüDersProgramiSecmeli.xml` (FBE Seçmeli Dersleri)
- `DATATEXT2`: Ders Kodu
- `DATATEXT3`: Şube Kodu
- `DATATEXT4`: Ders Adı
- `DATATEXT5`: Program Kodu (`15` YL, `16` DR)
- `DATATEXT6`: Başlangıç Saati
- `DATATEXT7`: Bitiş Saati
- `DATATEXT10`: Derslik Kodu
- `DATATEXT14`: Gün (0=Pzt..4=Cum)
- `DATATEXT15`: Uygulama mı (`__1` ise 1)
- `DATATEXT20`: Öğretim Görevlisi Soyadı/Adı

### C. `DersiAlanOgrenciler.xml` (Öğrenci Ders Kayıtları)
- `DATATEXT4`: Öğrenci No
- `DATATEXT5` & `DATATEXT6`: Öğrenci Adı ve Soyadı
- `DATATEXT9`: Program Metni (`(DR)` içeriyorsa Doktora: 16, aksi YL: 15)
- `DATATEXT11`: Şube Numarası
- `DATATEXT12`: Ders Kodu
- `DATATEXT13`: Ders Adı (Seminer / Danışmanlık / Uzmanlık)

---

## 5. Doğrulanmış Sistem İstatistikleri (Baseline Metrics)
- **Öğretim Üyesi:** 15
- **Lisans Ders Saati:** 106
- **Lisansüstü Seçmeli Ders Saati:** 66 (22 ders)
- **Uzmanlık Alan Saati:** 99
- **Danışmanlık Şube/Saat:** 87
- **Seminer Şube/Saat:** 14 şube (28 saat)
- **Bölüm Dışı İSG İ.Ö.:** 13 saat
- **Çakışma:** **0 (Sıfır)**
- **Günlük Üst Limit İhlali:** **0 (Tüm hocalar <= 8 saat)**
