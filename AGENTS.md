# Akdeniz Üniversitesi İnşaat Mühendisliği Ders Programı & Görevlendirme Otomasyonu

Bu çalışma alanı, Akdeniz Üniversitesi Mühendislik Fakültesi İnşaat Mühendisliği Bölümü'nde görevli 15 öğretim üyesinin örgün eğitim lisans ve lisansüstü ders programlarını, uzmanlık alan derslerini, tez danışmanlıklarını ve lisansüstü seminer derslerini çakışmasız olarak optimize edip üreten ve OBS otomasyon sistemine uygun formatta dışa aktaran Python tabanlı sisteme aittir.

---

## 📌 Proje Mimarisi ve Temel Dosyalar

| Dosya / Dizin | Tür | Açıklama |
| :--- | :--- | :--- |
| [`generate_schedule.py`](file:///d:/OneDrive%20Akdeniz%20Ogrenci/OneDrive%20-%20Akdeniz%20%C3%9Cniversitesi/Universite/DersKayit/Lisans%C3%BCst%C3%BCDersG%C3%B6revlendirmeleri/DersProgramiPython/generate_schedule.py) | Python Script | Ana motor: Veri okuma, çakışma kontrolü, yerleştirme optimizasyonu, Excel ve Markdown üretimi. |
| [`DersProgrami_Lisans.xlsx`](file:///d:/OneDrive%20Akdeniz%20Ogrenci/OneDrive%20-%20Akdeniz%20%C3%9Cniversitesi/Universite/DersKayit/Lisans%C3%BCst%C3%BCDersG%C3%B6revlendirmeleri/DersProgramiPython/DersProgrami_Lisans.xlsx) | Girdi (Excel) | İnşaat Mühendisliği lisans derslerinin önceden belirlenmiş haftalık saatleri ve derslikleri. |
| [`LisansüstüDersProgramiSecmeli.xml`](file:///d:/OneDrive%20Akdeniz%20Ogrenci/OneDrive%20-%20Akdeniz%20%C3%9Cniversitesi/Universite/DersKayit/Lisans%C3%BCst%C3%BCDersG%C3%B6revlendirmeleri/DersProgramiPython/Lisans%C3%BCst%C3%BCDersProgramiSecmeli.xml) | Girdi (XML) | FBE İnşaat Mühendisliği lisansüstü seçmeli derslerinin gün ve saat programı (YL: 15, DR: 16). |
| [`DersiAlanOgrenciler.xml`](file:///d:/OneDrive%20Akdeniz%20Ogrenci/OneDrive%20-%20Akdeniz%20%C3%9Cniversitesi/Universite/DersKayit/Lisans%C3%BCst%C3%BCDersG%C3%B6revlendirmeleri/DersProgramiPython/DersiAlanOgrenciler.xml) | Girdi (XML) | Lisansüstü öğrencilerin aldıkları dersler, danışmanlıklar, uzmanlık alanları ve seminer seçimleri. |
| [`DersProgrami_Kisisel.xlsx`](file:///d:/OneDrive%20Akdeniz%20Ogrenci/OneDrive%20-%20Akdeniz%20%C3%9Cniversitesi/Universite/DersKayit/Lisans%C3%BCst%C3%BCDersG%C3%B6revlendirmeleri/DersProgramiPython/DersProgrami_Kisisel.xlsx) | Çıktı (Excel) | Genel Bölüm Özeti ve 15 öğretim üyesinin renklendirilmiş haftalık kişisel ders programı sayfaları. |
| [`KisiselDersProgramlari/`](file:///d:/OneDrive%20Akdeniz%20Ogrenci/OneDrive%20-%20Akdeniz%20%C3%9Cniversitesi/Universite/DersKayit/Lisans%C3%BCst%C3%BCDersG%C3%B6revlendirmeleri/DersProgramiPython/KisiselDersProgramlari) | Çıktı (Dizin) | 15 öğretim üyesi için ayrı ayrı üretilmiş tekil ders programı Excel dosyaları. |
| [`DersProgrami_Otomasyon.xlsx`](file:///d:/OneDrive%20Akdeniz%20Ogrenci/OneDrive%20-%20Akdeniz%20%C3%9Cniversitesi/Universite/DersKayit/Lisans%C3%BCst%C3%BCDersG%C3%B6revlendirmeleri/DersProgramiPython/DersProgrami_Otomasyon.xlsx) | Çıktı (Excel) | OBS otomasyon sistemine aktarılmaya hazır 13 sütunlu standart lisansüstü görevlendirme tablosu. |
| [`DersProgrami_Raporu.md`](file:///d:/OneDrive%20Akdeniz%20Ogrenci/OneDrive%20-%20Akdeniz%20%C3%9Cniversitesi/Universite/DersKayit/Lisans%C3%BCst%C3%BCDersG%C3%B6revlendirmeleri/DersProgramiPython/DersProgrami_Raporu.md) | Çıktı (Markdown) | Yük dağılımı, kural uyumluluğu ve yönetici özetini içeren detaylı durum raporu. |
| [`MEMORY.md`](file:///d:/OneDrive%20Akdeniz%20Ogrenci/OneDrive%20-%20Akdeniz%20%C3%9Cniversitesi/Universite/DersKayit/Lisans%C3%BCst%C3%BCDersG%C3%B6revlendirmeleri/DersProgramiPython/MEMORY.md) | Hafıza | Öğretim üyeleri, derslikler, istisnalar, öğrenci düzeltmeleri ve kural parametreleri hafıza kaydı. |

---

## ⚡ Hızlı Komutlar

Sistemi çalıştırmak ve çıktıları güncellemek için:
```powershell
python generate_schedule.py
```

Bağımlılıkları kontrol etmek için:
```powershell
pip install openpyxl python-docx
```

---

## 🎯 Temel İlkeler ve Kurallar Özeti

1. **Çakışmasızlık Garantisi:** Hem öğretim üyesinin kendi takvimi hem de dersi alan her bir öğrencinin seçmeli ders takvimi çakışmasız olmalıdır.
2. **Günlük Maksimum Ders Yükü:** Bir öğretim üyesine aynı gün için örgün saatlerde (08:30-17:20) **en fazla 8 saat** ders yazılabilir.
3. **Derslik Politikası:** Lisansüstü Uzmanlık Alan, Danışmanlık ve Seminer dersleri öğretim üyelerinin kendi çalışma odalarında (`TEACHERS[t_id]['room']`) yürütülür.
4. **İkinci Öğretim İzolasyonu:** İş Sağlığı ve Güvenliği Tezsiz YL ikinci öğretim dersleri (Prof. Dr. Aynur KAZAZ ve Prof. Dr. Niyazi Uğur KOÇKAL) yalnızca kişisel programlara akşam slotu olarak işlenir; **bölüm otomasyon Excel'ine asla aktarılmaz**.
5. **Karakter Kodlaması:** Dosya okuma/yazma ve konsol çıktılarında `utf-8` kullanılmalıdır (`sys.stdout.reconfigure(encoding='utf-8')`).
