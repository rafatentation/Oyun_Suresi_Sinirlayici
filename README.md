# 🎮 Oyun Süresi Sınırlayıcı (Gençler için Ebeveyn Yardımı)

Bu proje, fuzzy logic (bulanık mantık) kullanarak gençlerin sağlıklı oyun alışkanlıkları geliştirmesine yardımcı olmak için geliştirilmiş bir karar destek sistemidir. Sistem, çeşitli faktörleri analiz ederek optimal oyun süresi ve mola önerileri sunar.

![Arayüz Örneği](assets/interface_screenshot.png) <!-- Ekran görüntüsü eklenecek -->

## 🌟 Öne Çıkan Özellikler

- *Akıllı Oyun Süresi Yönetimi*
  - Günün saatine göre dinamik öneriler
  - Okul günü/hafta sonu ayrımı
  - Göz yorgunluğu faktörü

- *Çoklu Parametre Analizi*
  - 5 girdi faktörü: 
    - Günün saati (0-23)
    - Oyun süresi (0-360 dk)
    - Okul günü durumu
    - Göz yorgunluğu seviyesi (1-10)
    - Önceki gün oyun süresi
  
- *2 Çıktı Önerisi*
  - Optimal mola süresi (0-60 dk)
  - Önerilen oyun süresi (0-240 dk)

- *15 Bulanık Mantık Kuralı* ile kapsamlı analiz
- Kullanıcı dostu Tkinter arayüzü
- Üyelik fonksiyonlarının görselleştirilmesi

## 🛠 Teknik Detaylar

### Kullanılan Teknolojiler
- *Python 3.8+*
- *scikit-fuzzy* (Bulanık mantık motoru)
- *Tkinter* (GUI arayüzü)
- *matplotlib* (Grafik görselleştirme)
- *numpy* (Sayısal hesaplamalar)

### Üyelik Fonksiyonları
| Değişken        | Kategoriler                     | Aralık       |
|-----------------|---------------------------------|-------------|
| Günün Saati     | Sabah/Öğlen/Akşam/Gece         | 0-23 saat   |
| Oyun Süresi     | Kısa/Orta/Uzun                 | 0-360 dk    |
| Göz Yorgunluğu  | Düşük/Orta/Yüksek              | 1-10 skala  |
| Okul Günü       | Evet/Hayır                     | Binary      |
| Önceki Oyun     | Az/Orta/Çok                    | 0-360 dk    |

### Örnek Kurallar
```python
ctrl.Rule(is_school_day['yes'] & time_of_day['night'], allowed_play['very_short']),
ctrl.Rule(eye_strain['high'], break_duration['long']),
ctrl.Rule(previous_play['much'] & is_school_day['yes'], allowed_play['very_short'])
📦 Kurulum
Gereksinimleri yükleyin:

bash
pip install numpy matplotlib scikit-fuzzy
Projeyi çalıştırın:

bash
python oyun_suresi_sinirlayici.py
🖥 Kullanım Kılavuzu
Tüm giriş alanlarını doldurun:

Günün saatini seçin

Bugün oynanan süreyi girin

Okul günü durumunu belirtin

Göz yorgunluğu seviyesini seçin

Dün oynanan süreyi girin

"HESAPLA" butonuna basın

Sistemin önerilerini inceleyin:

Önerilen mola süresi

İzin verilen oyun süresi

Ek sağlık tavsiyeleri

"GRAFİKLER" butonu ile üyelik fonksiyonlarını görselleştirin

📊 Örnek Çıktı
⏱ Önerilen Mola Süresi: 30 dakika
🎮 İzin Verilen Oyun Süresi: 90 dakika

❗ Gözleriniz çok yorgun, 15-20 dakika gözlerinizi dinlendirin
🌙 Geç saatte oyun oynamak uyku düzeninizi bozabili
