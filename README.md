# 🕹️ Oyun Süresi Sınırlayıcı (Bulanık Mantık Tabanlı)

Bu proje, oyun oynama süresini kontrol altında tutmak ve oyuncunun durumuna göre oyun süresi önerisinde bulunmak amacıyla **bulanık mantık (fuzzy logic)** kullanan bir karar destek sistemidir. Kullanıcı arayüzüyle birlikte çalışan sistem; ekran süresi, oyuncu yaşı, göz yorgunluğu, dikkat düzeyi ve önceki mola süresi gibi parametreleri değerlendirerek **oyun süresi önerisi** sunar ve **mola uyarısında** bulunur.

---

## 🎯 Amaç

Kullanıcının oyun başında veya oyun sırasında zihinsel ve fiziksel durumuna göre uygun oyun süresi tahmini yapmak ve gerektiğinde mola vermesi için öneride bulunmak.

---

## 🧠 Özellikler

### 📥 Girdi Değişkenleri (5 adet)

- **Göz Yorgunluğu (0–10)**
- **Dikkat Seviyesi (0–10)**
- **Yaş (6–50 yaş)**
- **Ekran Süresi (dk)**
- **Son Mola Süresi (dk)**

### 📤 Çıktı Değişkenleri (2 adet)

- **Oyun Süresi Önerisi (dk)**
- **Mola Önerisi (Evet / Hayır)**

### 📏 Bulanık Kurallar

- Sistem 10’dan fazla bulanık mantık kuralı içerir (örnek: “Dikkat seviyesi düşük ve ekran süresi yüksekse, mola önerilir”).

### 📈 Grafiksel Gösterim

- Girdi ve çıktı değişkenlerine ait **üyelik fonksiyonları**, matplotlib ile görselleştirilir.

### 📜 Kural Görüntüleme

- Tüm bulanık mantık kuralları, ayrı bir pencerede kullanıcıya **metin olarak** sunulur.

### 🖥️ Kullanıcı Arayüzü

- **Tkinter** ile geliştirilmiş, kullanıcı dostu ve koyu temalı pencere arayüzü.
- Girdi değerleri **slider (kaydırmalı çubuk)** ile girilir.
- "Hesapla" butonuyla sonuçlar anlık olarak görüntülenir.

---

## 🔧 Kullanılan Teknolojiler

- Python  
- Tkinter (GUI)  
- scikit-fuzzy (bulanık mantık motoru)  
- matplotlib (grafik çizimi)

---

## ⚙️ Kurulum

Gerekli kütüphaneleri yüklemek için:

```bash
pip install numpy matplotlib scikit-fuzzy



🚀 Projeyi Çalıştırma

1. Depoyu klonlayın:
git clone https://github.com/kullaniciadi/oyun_suresi_sinirlayici.git

2. Proje klasörüne geçin:
cd oyun_suresi_sinirlayici

3. Uygulamayı başlatın:
python main.py

📝 Notlar
Arayüz, sade ve sezgisel bir kullanıcı deneyimi için tasarlanmıştır.

Bulanık sistem kuralları genişletilebilir ve özelleştirilebilir yapıdadır.

Üyelik fonksiyonları ve kurallar üzerinden değişiklik yaparak sistem hassasiyeti kolayca ayarlanabilir.




