🎮 Oyun Süresi Sınırlayıcı (Gençler için Ebeveyn Yardımı)
Bu proje, bulanık mantık (fuzzy logic) temelli bir karar destek sistemidir. Amaç, gençlerin sağlıklı dijital alışkanlıklar kazanmasını sağlamak ve ebeveynlere oyun süresi yönetiminde destek olmaktır. Sistem, kullanıcının günün saatinden göz yorgunluğuna kadar farklı faktörleri değerlendirerek optimum oyun süresi ve mola süresi önermektedir.

🌟 Öne Çıkan Özellikler
🔹 Akıllı Oyun Süresi Yönetimi
Günün saatine göre öneri yapar (sabah, öğlen, akşam, gece)

Okul günü ile hafta sonu ayrımı yapar

Göz yorgunluğunu dikkate alır

Önceki gün oynanan sürelere göre sınırlandırma getirir

🔹 Çoklu Parametre Analizi
Toplam 5 girdi, 2 çıktı ile değerlendirme yapılır:

Girdiler:
Günün Saati (0–23 saat aralığı)

Bugünkü Oyun Süresi (0–360 dakika)

Okul Günü Durumu (Evet / Hayır)

Göz Yorgunluğu (1–10 arası skala)

Önceki Gün Oyun Süresi (0–360 dakika)

Çıktılar:
Önerilen Mola Süresi (0–60 dakika)

İzin Verilen Oyun Süresi (0–240 dakika)

🔹 Kural Tabanı (15 Adet Bulanık Kural)
python
Kopyala
Düzenle
ctrl.Rule(is_school_day['yes'] & time_of_day['night'], allowed_play['very_short']),
ctrl.Rule(eye_strain['high'], break_duration['long']),
ctrl.Rule(previous_play['much'] & is_school_day['yes'], allowed_play['very_short'])
Kurallar, oyun süresini sınırlandırmak ve gerektiğinde mola vermeyi önermek için çeşitli kombinasyonlar içerir.

🖥 Kullanıcı Arayüzü (Tkinter)
Modern ve kullanıcı dostu arayüz:
Günün saatini, oyun süresini, okul gününü, göz yorgunluğunu ve önceki oyun süresini girmeye olanak tanır.

“HESAPLA” butonuyla önerilen süreleri hesaplar.

“GRAFİKLER” butonuyla tüm üyelik fonksiyonlarını görselleştirir (matplotlib ile çizilir).

Örnek Çıktı:
Kopyala
Düzenle
⏱ Önerilen Mola Süresi: 30 dakika
🎮 İzin Verilen Oyun Süresi: 90 dakika

❗ Gözleriniz çok yorgun, 15-20 dakika gözlerinizi dinlendirin
🌙 Geç saatte oyun oynamak uyku düzeninizi bozabilir
🛠 Teknik Detaylar
Kullanılan Teknolojiler:
Python 3.8+

scikit-fuzzy (bulanık mantık motoru)

Tkinter (grafik arayüz)

matplotlib (grafik çizimleri)

numpy (sayısal işlemler)

Üyelik Fonksiyonları:
Değişken	Kategoriler	Aralık
Günün Saati	Sabah / Öğlen / Akşam / Gece	0–23
Oyun Süresi	Kısa / Orta / Uzun	0–360 dk
Göz Yorgunluğu	Düşük / Orta / Yüksek	1–10 skala
Okul Günü	Evet / Hayır	0 veya 1 (Binary)
Önceki Oyun Süresi	Az / Orta / Çok	0–360 dk

Bu fonksiyonlar fuzz.trimf() ile üçgen üyelik şeklinde tanımlanmıştır.

📦 Kurulum
bash
Kopyala
Düzenle
pip install numpy matplotlib scikit-fuzzy
Projenin ana dosyasını çalıştırmak için:

bash
Kopyala
Düzenle
python oyun_suresi_sinirlayici.py
🔧 Geliştirici Notları
Arayüz sınıfı OyunSuresiSinirlayici olarak tanımlanmıştır.

Kullanıcıdan alınan girişler kontrol edilir, ardından ctrl.ControlSystemSimulation ile çıktı hesaplanır.

Üyelik fonksiyonları görselleştirmeleri ayrı pencerede çizdirilir (matplotlib + TkAgg entegrasyonu).

Program sonunda main bloğunda Tkinter GUI başlatılır.
