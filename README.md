# 🎮 Oyun Süresi Sınırlayıcı (Gençler için Ebeveyn Yardımı)

Bu proje, fuzzy logic (bulanık mantık) temelli bir karar destek sistemidir. Gençlerin bilgisayar oyunlarıyla geçirdiği süreyi dengelemek ve göz sağlığı gibi faktörleri gözetmek amacıyla geliştirilmiştir. Uygulama, 5 farklı girdi parametresi alarak 2 farklı öneri sunar:

- Önerilen oyun süresi
- Önerilen mola süresi

Python dili ile yazılmış olan bu sistemin arayüzü Tkinter ile hazırlanmıştır. Görselleştirme için matplotlib ve karar analizi için scikit-fuzzy kütüphanesi kullanılmıştır.

---

## 🧾 Girdiler

Sistem aşağıdaki 5 girdi üzerinden çalışır:

| Girdi İsmi         | Açıklama                                                                 | Değer Aralığı     |
|--------------------|--------------------------------------------------------------------------|-------------------|
| `time_of_day`      | Günün saati (sadece saat kısmı alınır, 24 saatlik format)                | 0 - 23            |
| `play_duration`    | Bugün oynanan oyun süresi (dakika)                                       | 0 - 360           |
| `is_school_day`    | Günün okul günü olup olmadığını belirtir (Evet: 1, Hayır: 0)              | 0 veya 1          |
| `eye_strain`       | Göz yorgunluğu seviyesi                                                  | 1 - 10            |
| `previous_play`    | Dünün oyun süresi                                                        | 0 - 360           |

---

## 🔧 Kullanılan Teknolojiler

- Python 3.8+
- scikit-fuzzy
- tkinter
- matplotlib
- numpy

---

## 🛠 Kurulum

pip install numpy matplotlib scikit-fuzzy

🚀 Uygulamanın Başlatılması
python oyun_suresi_sinirlayici.py

## 📂 Proje Dosya Yapısı

```bash
├── oyun_suresi_sinirlayici.py
├── assets/
│   └── interface_screenshot.png
└── README.md
``` 
## 📌 Girdilerin Tanımlanması
```bash
time_of_day = ctrl.Antecedent(np.arange(0, 24, 1), 'time_of_day')
→ 0-23 saat aralığında günün saatini temsil eder.

play_duration = ctrl.Antecedent(np.arange(0, 361, 1), 'play_duration')
→ Bugünkü oyun süresi. 0 ile 360 dakika arasında değer alabilir.

is_school_day = ctrl.Antecedent(np.arange(0, 2, 1), 'is_school_day')
→ Okul günü olup olmadığını belirtir. 0 (Hayır), 1 (Evet).****

eye_strain = ctrl.Antecedent(np.arange(0, 11, 1), 'eye_strain')
→ Göz yorgunluğu. 1-10 arası kullanıcıdan alınan değere göre değerlendirilir.

previous_play = ctrl.Antecedent(np.arange(0, 361, 1), 'previous_play')
→ Önceki gün oynanan oyun süresi. 0–360 dakika aralığında.
```

## 📌 Çıktıların Tanımlanması
```bash
break_duration = ctrl.Consequent(np.arange(0, 61, 1), 'break_duration')
→ Verilecek mola süresi. 0–60 dakika aralığında önerilir.

allowed_play = ctrl.Consequent(np.arange(0, 241, 1), 'allowed_play')
→ İzin verilen oyun süresi. 0–240 dakika aralığında önerilir.
```

## 📊 Üyelik Fonksiyonları
```bash
Günün Saati
time_of_day['morning'] = fuzz.trimf(time_of_day.universe, [0, 6, 12])
time_of_day['afternoon'] = fuzz.trimf(time_of_day.universe, [10, 14, 18])
time_of_day['evening'] = fuzz.trimf(time_of_day.universe, [16, 20, 23])
time_of_day['night'] = fuzz.trimf(time_of_day.universe, [21, 23, 23])

Oyun Süresi
play_duration['short'] = fuzz.trimf(play_duration.universe, [0, 0, 60])
play_duration['medium'] = fuzz.trimf(play_duration.universe, [30, 120, 180])
play_duration['long'] = fuzz.trimf(play_duration.universe, [150, 360, 360])

Okul Günü****
is_school_day['no'] = fuzz.trimf(is_school_day.universe, [0, 0, 0.5])
is_school_day['yes'] = fuzz.trimf(is_school_day.universe, [0.5, 1, 1])

Göz Yorgunluğu
eye_strain['low'] = fuzz.trimf(eye_strain.universe, [0, 0, 4])
eye_strain['medium'] = fuzz.trimf(eye_strain.universe, [2, 5, 8])
eye_strain['high'] = fuzz.trimf(eye_strain.universe, [6, 10, 10])

Önceki Gün Oyun Süresi
previous_play['little'] = fuzz.trimf(previous_play.universe, [0, 0, 120])
previous_play['moderate'] = fuzz.trimf(previous_play.universe, [60, 180, 240])
previous_play['much'] = fuzz.trimf(previous_play.universe, [180, 360, 360])

Mola Süresi (Çıktı)
break_duration['short'] = fuzz.trimf(break_duration.universe, [0, 0, 15])
break_duration['medium'] = fuzz.trimf(break_duration.universe, [10, 30, 45])
break_duration['long'] = fuzz.trimf(break_duration.universe, [30, 60, 60])

Oyun Süresi (Çıktı)
allowed_play['very_short'] = fuzz.trimf(allowed_play.universe, [0, 0, 60])
allowed_play['short'] = fuzz.trimf(allowed_play.universe, [30, 90, 120])
allowed_play['moderate'] = fuzz.trimf(allowed_play.universe, [90, 150, 180])
allowed_play['long'] = fuzz.trimf(allowed_play.universe, [150, 240, 240])
```

## 🔁 Bulanık Mantık Kuralları
```bash
rules = [
    ctrl.Rule(is_school_day['yes'] & time_of_day['night'], allowed_play['very_short']),
    ctrl.Rule(is_school_day['yes'] & time_of_day['evening'], allowed_play['short']),
    ctrl.Rule(is_school_day['no'], allowed_play['moderate']),
    ctrl.Rule(eye_strain['high'], break_duration['long']),
    ctrl.Rule(eye_strain['medium'], break_duration['medium']),
    ctrl.Rule(eye_strain['low'], break_duration['short']),
    ctrl.Rule(play_duration['long'], break_duration['long']),
    ctrl.Rule(play_duration['medium'], break_duration['medium']),
    ctrl.Rule(play_duration['short'], break_duration['short']),
    ctrl.Rule(previous_play['much'] & is_school_day['yes'], allowed_play['very_short']),
    ctrl.Rule(previous_play['moderate'] & is_school_day['yes'], allowed_play['short']),
    ctrl.Rule(previous_play['little'], allowed_play['moderate']),
    ctrl.Rule(time_of_day['morning'] & is_school_day['yes'], allowed_play['very_short']),
    ctrl.Rule(time_of_day['afternoon'] & is_school_day['no'], allowed_play['moderate']),
    ctrl.Rule(eye_strain['high'] & play_duration['long'], break_duration['long']),
]
```

## 💻 Arayüz Özellikleri
Tkinter kullanılarak yapılmıştır.

Giriş alanları:

Saat seçici

Sayısal giriş kutuları

Dropdown menüler

"HESAPLA" butonu ile fuzzy karar hesaplanır.

"GRAFİKLER" butonu ile üyelik fonksiyonları matplotlib ile görselleştirilir.

## 📊 Örnek Çıktı

![Ekran şəkli 2025-05-26 051510](https://github.com/user-attachments/assets/0e55e942-b890-4b4a-9712-6284a771b764)

## ⏱ Önerilen Mola Süresi: 30 dakika
## 🎮 İzin Verilen Oyun Süresi: 90 dakika

## ❗ Gözleriniz çok yorgun, 15-20 dakika gözlerinizi dinlendirin
## 🌙 Geç saatte oyun oynamak uyku düzeninizi bozabilir




