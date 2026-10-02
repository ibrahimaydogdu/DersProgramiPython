# Akdeniz Üniversitesi İnşaat Mühendisliği Lisansüstü Ders Programı Otomasyonu

Bu depo, Akdeniz Üniversitesi Mühendislik Fakültesi İnşaat Mühendisliği Bölümü'nde görev yapan 15 öğretim üyesinin haftalık örgün lisans ve lisansüstü ders programlarını, uzmanlık alan derslerini, tez danışmanlıklarını ve lisansüstü seminerlerini çakışmasız olarak optimize edip üreten ve Öğrenci Bilgi Sistemi (OBS) otomasyonuna uygun formatta dışa aktaran Python tabanlı yazılım sistemini içerir.

---

## 🚀 Temel Özellikler

- **0 (Sıfır) Çakışma Garantisi:** Hem 15 öğretim üyesinin takvimleri hem de dersi alan tüm lisansüstü öğrencilerin seçmeli ders takvimleri çapraz kontrol edilerek doğrulanır.
- **Mevzuat Uyumu (Günlük $\le$ 8 Saat):** Tüm öğretim üyeleri için örgün saatlerde (08:30 - 17:20) günlük maksimum 8 ders saati sınırı korunur.
- **Öğretim Üyesi Odası Politikası:** Lisansüstü Seminer, Danışmanlık ve Uzmanlık Alan dersleri ilgili hocanın çalışma odasında (`C302` - `C335`) yürütülecek şekilde konumlandırılır.
- **İkinci Öğretim İzolasyonu:** FBE İş Sağlığı ve Güvenliği Tezsiz YL ikinci öğretim akşam dersleri (Prof. Dr. Aynur KAZAZ ve Prof. Dr. Niyazi Uğur KOÇKAL) yalnızca kişisel ders programlarına işlenir; bölüm otomasyonuna aktarılmaz.
- **Otomasyon Dışa Aktarımı:** OBS otomasyon sistemine aktarılmaya hazır 13 sütunlu, öğretim üyesi, program kodu ve gün/saat hiyerarşisinde sıralı standart Excel üretimi.
- **Renkli Kişisel Programlar:** openpyxl ile tasarlanmış, pastel tonlu kurumsal renk şablonuna ve öğrenci isimlerine sahip kişisel programlar ve Bölüm Genel Özeti.

---

## 📁 Proje Dosya Yapısı

```text
├── generate_schedule.py             # Ana programlama ve optimizasyon motoru
├── DersProgrami_Lisans.xlsx         # Girdi: Örgün lisans dersleri haftalık tablosu
├── LisansüstüDersProgramiSecmeli.xml # Girdi: FBE lisansüstü seçmeli dersler programı (YL: 15, DR: 16)
├── DersiAlanOgrenciler.xml          # Girdi: Lisansüstü öğrenci ders seçimleri ve danışmanlık listesi
├── DersProgrami_Kisisel.xlsx        # Çıktı: Bölüm Özeti + 15 Öğretim Üyesi kişisel program sayfaları
├── DersProgrami_Otomasyon.xlsx      # Çıktı: OBS sistemine aktarılacak 13 sütunlu görevlendirme tablosu
├── DersProgrami_Raporu.md           # Çıktı: Detaylı bölüm yük dağılımı ve çakışmasızlık durum raporu
├── KisiselDersProgramlari/          # Çıktı: 15 hoca için ayrı ayrı üretilmiş tekil Excel dosyaları
├── AGENTS.md                        # Yapay zeka ve sistem çalıştırma kılavuzu
├── MEMORY.md                        # Öğretim üyeleri, derslikler, düzeltmeler ve veri şemaları hafızası
└── .agents/
    ├── rules/                       # Akademik ve kodlama kural belgeleri
    └── skills/                      # Ders programı yönetim ve çalıştırma runbook'u
```

---

## 🛠️ Kurulum ve Çalıştırma

### 1. Bağımlılıkları Yükleyin:
```powershell
pip install openpyxl python-docx
```

### 2. Motoru Çalıştırın:
```powershell
python generate_schedule.py
```

İşlem tamamlandığında `DersProgrami_Kisisel.xlsx`, `KisiselDersProgramlari/`, `DersProgrami_Otomasyon.xlsx` ve `DersProgrami_Raporu.md` dosyaları otomatik olarak güncellenir.

---

## 👥 Bölüm Öğretim Üyeleri ve Şube Dağılımı

| Şube No | Öğretim Üyesi | Oda | Lisans | Seçmeli | Uzmanlık | Danışmanlık | Seminer | Toplam Saat |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Prof. Dr. Ömer CİVALEK | C303 | 6 | 6 | 8 | 7 | 2 | **29** |
| 2 | Prof. Dr. Aynur KAZAZ | C304 | 8 | 6 | 8 | 7 | 2 | **31** (+8 İSG) |
| 3 | Prof. Dr. N. Uğur KOÇKAL | C332 | 8 | 6 | 8 | 8 | 0 | **30** (+5 İSG) |
| 4 | Prof. Dr. Nihat DİPOVA | C305 | 5 | 6 | 4 | 5 | 2 | **22** |
| 5 | Prof. Dr. İzzet Ufuk ÇAĞDAŞ | C326 | 8 | 6 | 4 | 1 | 0 | **19** |
| 6 | Prof. Dr. Okan ÖZCAN | C324 | 9 | 3 | 8 | 6 | 4 | **30** |
| 7 | Prof. Dr. Ramazan ÖZÇELİK | C334 | 5 | 3 | 8 | 10 | 2 | **28** |
| 8 | Prof. Dr. İbrahim AYDOĞDU | C331 | 9 | 3 | 8 | 5 | 2 | **27** |
| 9 | Prof. Dr. Ferhat ERDAL | C335 | 8 | 3 | 8 | 4 | 0 | **23** |
| 10 | Prof. Dr. Sevil KÖFTECİ | C327 | 2 | 0 | 8 | 5 | 2 | **17** |
| 11 | Doç. Dr. Rıfat TÜR | C333 | 5 | 6 | 4 | 4 | 2 | **21** |
| 12 | Dr. Öğr. Üyesi Engin EMSEN | C325 | 9 | 0 | 4 | 2 | 2 | **17** |
| 13 | Doç. Dr. Bekir AKGÖZ | C302 | 7 | 6 | 8 | 5 | 2 | **28** |
| 14 | Doç. Dr. Halil İbrahim BURGAN | C323 | 8 | 6 | 7 | 12 | 4 | **37** |
| 15 | Prof. Dr. Banihan GÜNAY | C322 | 8 | 6 | 4 | 6 | 2 | **26** |
