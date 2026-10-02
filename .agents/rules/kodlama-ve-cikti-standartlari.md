# Kodlama, Biçimlendirme ve Çıktı Standartları

Bu kural belgesi, projede geliştirilen Python kodlarının mimari kalitesini, openpyxl biçimlendirme kurallarını ve çıktı dosyalarının yapısal standartlarını belirler.

---

## 1. Python Kodlama ve Sistem Standartları

1. **Karakter Kodlaması (Encoding):**
   - Windows ortamında Türkçe karakterler (`ç, ğ, ı, ö, ş, ü, İ, Ş, Ğ`) cp1252 hatasına yol açabileceğinden tüm dosya I/O ve standart çıktı işlemlerinde UTF-8 zorunludur:
     ```python
     import sys
     sys.stdout.reconfigure(encoding='utf-8')
     ```
   - Dosya okuma/yazma işlemlerinde: `open(filepath, 'w', encoding='utf-8')`.

2. **Excel Dosya Kilitlenmesi (PermissionError Koruması):**
   - Kullanıcı Excel dosyalarını açık tutarken script çalıştırıldığında çökmesini önlemek için tüm `wb.save()` çağrıları `try-except PermissionError` bloğu içine alınmalıdır:
     ```python
     try:
         wb.save(filepath)
     except PermissionError:
         print(f"UYARI: '{filepath}' dosyası açık olduğu için kaydedilemedi. Lütfen dosyayı kapatıp tekrar deneyiniz.")
     ```

3. **Dosya Adı Temizliği (`to_ascii`):**
   - Bireysel hoca dosyaları oluşturulurken dosya adlarında Türkçe karakter ve özel karakter bırakılmamalıdır (`DersProgrami_Sube01_Prof_Dr_Omer_CIVALEK.xlsx`).

---

## 2. openpyxl Tasarım ve Biçimlendirme Standartları

Kişisel ders programları için profesyonel, modern ve pastel tonlu kurumsal renk paleti kullanılır:

| Görev / Ders Türü | Dolgu Rengi (Hex) | Yazı Rengi (Hex) | Kenarlık (Hex) | Anlamı |
| :--- | :--- | :--- | :--- | :--- |
| **Lisans** | `#D9E8FB` (Yumuşak Mavi) | `#1E3A8A` (Koyu Mavi) | `#93C5FD` | Lisans örgün eğitim dersleri |
| **Seçmeli** | `#D1FAE5` (Nane Yeşili) | `#065F46` (Koyu Zümrüt) | `#A7F3D0` | FBE Lisansüstü Seçmeli Dersleri |
| **Uzmanlık** | `#EDE9FE` (Lavanta) | `#5B21B6` (Koyu Mor) | `#DDD6FE` | Tez Aşaması Uzmanlık Alan Dersi |
| **Danışmanlık**| `#FFEDD5` (Sıcak Şeftali) | `#9A3412` (Koyu Turuncu) | `#FED7AA` | Lisansüstü Tez Danışmanlık Görevi |
| **Seminer** | `#FEF3C7` (Kehribar Sarısı) | `#92400E` (Koyu Hardal) | `#FDE68A` | Lisansüstü Seminer Uygulama |
| **Tezsiz YL (İ.Ö.)** | `#FCE7F3` (Gül Pembe) | `#9D174D` (Koyu Gül/Bordo) | `#F472B6` | İş Sağlığı ve Güvenliği Ek Görev |
| **Müsait** | `#F8FAFC` (Açık Slate) | `#94A3B8` (Açık Gri) | `#E2E8F0` | Boş / Değiştirilebilir Saatler |

- **Yazı Tipi:** Standart olarak `Segoe UI` kullanılır.
- **Satır Yükseklikleri:**
  - Başlık Banner: 24 pt
  - Alt Başlık: 22 pt
  - Tablo Başlıkları (Günler): 28 pt
  - Gündüz Saat Satırları (1-9): 46 pt
  - Günlük Toplam Satırı: 22 pt
  - Akşam Satırları (Varsa): 48 pt
- **Hücre İçi Metin:** Hücre içinde `Ders Kodu (Şube - Teo/Uyg)\nDers Adı\nÖğr: Öğrenci Adı veya Yer: Derslik` formatında çok satırlı düzen ve `wrap_text=True` kullanılır.

---

## 3. Otomasyon Çıktısı Standartları (`DersProgrami_Otomasyon.xlsx`)

Otomasyon sayfası, Öğrenci İşleri OBS sistemine toplu veri aktarımı için tasarlanmıştır.

### Sütun Sıralaması (13 Sütun):
1. `A Şube Kodu` (int)
2. `B Ders Kodu` (str - örn: `FBE 6901`)
3. `C Gün` (int: 0=Pzt, 1=Sal, 2=Çar, 3=Per, 4=Cum)
4. `D Başlangıç Saati` (str - örn: `08:30`)
5. `E Bitiş Saati` (str - örn: `09:20`)
6. `F Derslik Kodu` (str - örn: `C323`)
7. `G Uygulama` (int: 0 No, 1 Yes)
8. `H Ortak Ders` (int: 0 No, 1 Yes)
9. `I Çakışma Kontrol Dışı` (int: 0 No, 1 Yes)
10. `J Program Kodu` (int: 15 YL, 16 DR)
11. `Ders Adı` (str)
12. `Öğretim Üyesi` (str)
13. `Öğrenci Adı / Not` (str)

### Çok Düzeyli Sıralama (Sort Order):
Otomasyona aktarılacak kayıtlar şu öncelikle sıralanır:
1. Öğretim Üyesi ID (`t_id`: 1..15)
2. Program Kodu (`prog`: Önce 15 YL, sonra 16 DR)
3. Gün (`day`: 0..4)
4. Slot (`slot`: 0..8)
5. Şube Kodu (`sube`)
