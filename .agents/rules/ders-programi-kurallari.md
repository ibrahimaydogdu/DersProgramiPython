# İnşaat Mühendisliği Lisansüstü Ders Programı ve Görevlendirme Kuralları

Bu kural belgesi, Akdeniz Üniversitesi Mühendislik Fakültesi İnşaat Mühendisliği Lisansüstü Ders Programlama Motoru (`generate_schedule.py`) ve veri yönetimi ile ilgili tüm bağlayıcı akademik ve teknik kuralları tanımlar.

---

## 1. Akademik ve Mevzuat Kuralları

### Kural 1: Uzmanlık Alan Dersi Yükleri
- **Yüksek Lisans (YL):** Teori: 4 saat, Uygulama: 0 saat (Program Kodu: `15`).
- **Doktora (DR):** Teori: 8 saat, Uygulama: 0 saat (Program Kodu: `16`).
- Bir öğretim üyesi aynı dönemde YL için en fazla 1, DR için en fazla 1 uzmanlık alan dersi açabilir.
- Bir öğretim üyesinin toplam uzmanlık alan ders saati **en fazla 8 saat** olabilir.
  - Sadece YL öğrencisi olan hocalara: 4 saat (örn: Prof. Dr. Nihat Dipova, Prof. Dr. İzzet Ufuk Çağdaş, Doç. Dr. Rıfat Tür, Dr. Öğr. Üyesi Engin Emsen, Prof. Dr. Banihan Günay).
  - Hem YL hem DR öğrencisi olan hocalara: 4 saat YL + 4 saat DR = 8 saat (örn: Prof. Dr. Ramazan Özçelik, Prof. Dr. İbrahim Aydoğdu, Prof. Dr. Sevil Köfteci, Doç. Dr. Halil İbrahim Burgan).
  - Yalnızca DR öğrencisi olan veya 8 saatlik tek DR uzmanlık alan dersi seçilmiş hocalara: 8 saat (örn: Prof. Dr. Ömer Civalek, Prof. Dr. Aynur Kazaz, Prof. Dr. N. Uğur Koçkal, Prof. Dr. Okan Özcan, Prof. Dr. Ferhat Erdal, Doç. Dr. Bekir Akgöz).

### Kural 2: Lisansüstü Danışmanlık Görevi
- Lisansüstü Danışmanlık dersi Teori: 0, Uygulama: 1 saattir (Program Kodu: YL için `15`, DR için `16`).
- Her danışmanlık şubesinin kontenjanı **kesinlikle 1'dir**. Yani her öğrenci için ayrı bir şube ve ayrı bir saat tanımlanır.
- Danışmanlık şube kodları `X + 100*k` formülüne tam uymalıdır (Örn: Hoca Şube No = 14 ise danışmanlık şubeleri: 14, 114, 214, 314...).
- Danışmanlık hücrelerinde mutlaka ilgili öğrencinin ad ve soyadı yer almalıdır.

### Kural 3: Lisansüstü Seminer Dersi
- Lisansüstü Seminer dersi Teori: 0, Uygulama: 2 saattir (Blok 2 saat olarak yerleştirilir).
- Bir gruptaki tüm öğrenciler ve dersin öğretim üyesi aynı 2 saatlik blokta bulunmalıdır.

### Kural 4: Sıfır Ders Saati Olan Dersler
- Yüksek Lisans Tezi, Doktora Tezi, Doktora Yeterlilik ve Uzmanlık Alan Sınavı gibi haftalık ders yükü 0 olan dersler haftalık programa işlenmez.

### Kural 5: Günlük Maksimum Ders Saati Sınırı (Kural 10)
- Herhangi bir öğretim üyesine aynı gün içerisinde örgün eğitim saatlerinde (08:30-17:20) **en fazla 8 ders saati** atanabilir.
- Günlük toplam ders saati 8'i aşamaz (`daily_count <= 8`).

### Kural 6: Derslik Politikası
- Lisansüstü Uzmanlık Alan, Danışmanlık ve Seminer dersleri öğretim üyelerinin kendi çalışma odalarında (`TEACHERS[t_id]['room']`) yürütülür.
- Lisans dersleri ve lisansüstü seçmeli dersler ise amfi/sınıflarda işlenir (orijinal derslik kodları korunur).

---

## 2. Çakışma Önleme Kuralları

1. **Öğretim Üyesi Takvimi:** Bir öğretim üyesinin aynı gün ve saat diliminde (`day`, `slot`) birden fazla görevi bulunamaz (Lisans, Seçmeli, Uzmanlık, Danışmanlık, Seminer çakışamaz).
2. **Öğrenci Takvimi:** Danışmanlık, seminer veya uzmanlık dersine kayıtlı öğrencinin, o gün ve saatte aldığı başka bir lisansüstü seçmeli dersi olamaz. Öğrencinin seçmeli ders saatleri meşgul (`busy`) kabul edilir.
3. **Slot Önceliklendirmesi (Tavsiye 4):** Lisansüstü seçmeli dersler genelde 09:30-12:20 ve 13:30-16:20 arasında yoğunlaştığından, danışmanlıklar öncelikle serbest uç saatlere yerleştirilir:
   - 1. Öncelik: `0` (08:30-09:20), `4` (12:30-13:20), `8` (16:30-17:20)
   - 2. Öncelik: `1`, `7`, `2`, `6`, `3`, `5`

---

## 3. İkinci Öğretim (İSG Tezsiz YL) İzolasyon Kuralı

- Prof. Dr. Aynur KAZAZ (8 saat) ve Prof. Dr. Niyazi Uğur KOÇKAL (5 saat) için Fen Bilimleri Enstitüsü İş Sağlığı ve Güvenliği ABD Tezsiz Yüksek Lisans ikinci öğretim dersleri mevcuttur.
- **KRİTİK KURAL:** Bu dersler yalnızca kişisel programlara (`DersProgrami_Kisisel.xlsx` ve `KisiselDersProgramlari/`) 17:30-22:55 saat dilimleri arasında pembe tonlu renkle işlenir.
- Bu dersler **kesinlikle** İnşaat Mühendisliği bölüm otomasyon dosyasına (`DersProgrami_Otomasyon.xlsx`) **aktarılmaz** (`is_external = True` ya da tip filtresi ile izole edilir).
