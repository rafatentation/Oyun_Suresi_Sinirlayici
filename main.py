import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# 1. FUZZY SİSTEM TANIMLARI
# Girdiler
time_of_day = ctrl.Antecedent(np.arange(0, 24, 1), 'time_of_day')
play_duration = ctrl.Antecedent(np.arange(0, 361, 1), 'play_duration')
is_school_day = ctrl.Antecedent(np.arange(0, 2, 1), 'is_school_day')
eye_strain = ctrl.Antecedent(np.arange(0, 11, 1), 'eye_strain')
previous_play = ctrl.Antecedent(np.arange(0, 361, 1), 'previous_play')

# Çıktılar
break_duration = ctrl.Consequent(np.arange(0, 61, 1), 'break_duration')
allowed_play = ctrl.Consequent(np.arange(0, 241, 1), 'allowed_play')

# 2. ÜYELİK FONKSİYONLARI
time_of_day['morning'] = fuzz.trimf(time_of_day.universe, [0, 6, 12])
time_of_day['afternoon'] = fuzz.trimf(time_of_day.universe, [10, 14, 18])
time_of_day['evening'] = fuzz.trimf(time_of_day.universe, [16, 20, 23])
time_of_day['night'] = fuzz.trimf(time_of_day.universe, [21, 23, 23])

play_duration['short'] = fuzz.trimf(play_duration.universe, [0, 0, 60])
play_duration['medium'] = fuzz.trimf(play_duration.universe, [30, 120, 180])
play_duration['long'] = fuzz.trimf(play_duration.universe, [150, 360, 360])

is_school_day['no'] = fuzz.trimf(is_school_day.universe, [0, 0, 0.5])
is_school_day['yes'] = fuzz.trimf(is_school_day.universe, [0.5, 1, 1])

eye_strain['low'] = fuzz.trimf(eye_strain.universe, [0, 0, 4])
eye_strain['medium'] = fuzz.trimf(eye_strain.universe, [2, 5, 8])
eye_strain['high'] = fuzz.trimf(eye_strain.universe, [6, 10, 10])

previous_play['little'] = fuzz.trimf(previous_play.universe, [0, 0, 120])
previous_play['moderate'] = fuzz.trimf(previous_play.universe, [60, 180, 240])
previous_play['much'] = fuzz.trimf(previous_play.universe, [180, 360, 360])

break_duration['short'] = fuzz.trimf(break_duration.universe, [0, 0, 15])
break_duration['medium'] = fuzz.trimf(break_duration.universe, [10, 30, 45])
break_duration['long'] = fuzz.trimf(break_duration.universe, [30, 60, 60])

allowed_play['very_short'] = fuzz.trimf(allowed_play.universe, [0, 0, 60])
allowed_play['short'] = fuzz.trimf(allowed_play.universe, [30, 90, 120])
allowed_play['moderate'] = fuzz.trimf(allowed_play.universe, [90, 150, 180])
allowed_play['long'] = fuzz.trimf(allowed_play.universe, [150, 240, 240])

# 3. KURALLAR
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

system = ctrl.ControlSystem(rules)

# 4. ARAYÜZ TASARIMI
class OyunSuresiSinirlayici:
    def __init__(self, root):
        self.root = root
        self.root.title("Oyun Süresi Sınırlayıcı")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")
        
        self.setup_ui()
    
    def setup_ui(self):
        # Başlık
        title = ttk.Label(self.root, 
                         text="Oyun Süresi Sınırlayıcı\n(Gençler için Ebeveyn Yardımı)", 
                         font=('Arial', 14, 'bold'),
                         background="#f5f5f5")
        title.pack(pady=10)
        
        # Giriş alanları çerçevesi
        input_frame = ttk.Frame(self.root, padding=(20, 10))
        input_frame.pack(pady=10, fill=tk.X)
        
        # Giriş alanları
        self.create_dropdown(input_frame, "Günün Saati:", "time", 
                           [f"{i:02d}:00" for i in range(24)], 16, 0)
        self.create_entry(input_frame, "Bugün Oynanan Süre (dk):", "play_time", "120", 1)
        self.create_dropdown(input_frame, "Okul Günü mü?", "school_day", ["Evet", "Hayır"], 0, 2)
        self.create_dropdown(input_frame, "Göz Yorgunluğu (1-10):", "eye_strain", 
                           [str(i) for i in range(1, 11)], 4, 3)
        self.create_entry(input_frame, "Dün Oynanan Süre (dk):", "prev_play", "90", 4)
        
        # Butonlar çerçevesi
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="HESAPLA", command=self.calculate,
                  style='Accent.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="GRAFİKLER", command=self.show_graphs,
                  style='Secondary.TButton').pack(side=tk.LEFT, padx=5)
        
        # Sonuç alanı
        self.result_frame = ttk.LabelFrame(self.root, text="Sonuç", padding=(20, 10))
        self.result_frame.pack(pady=10, fill=tk.X, padx=20)
        
        self.result_label = ttk.Label(self.result_frame, 
                                    text="Lütfen bilgileri girin ve hesapla butonuna basın",
                                    font=('Arial', 11),
                                    justify=tk.CENTER)
        self.result_label.pack()
        
        # Stil ayarları
        self.set_styles()
    
    def set_styles(self):
        style = ttk.Style()
        style.configure('TLabel', background="#f5f5f5", font=('Arial', 10))
        style.configure('TEntry', font=('Arial', 10), padding=5)
        style.configure('TCombobox', padding=5)
        style.configure('Accent.TButton', font=('Arial', 11, 'bold'), 
                      foreground='white', background='#4CAF50')
        style.configure('Secondary.TButton', font=('Arial', 11), 
                      foreground='white', background='#2196F3')
        style.map('Accent.TButton', background=[('active', '#45a049')])
        style.map('Secondary.TButton', background=[('active', '#1976D2')])
        style.configure('TLabelframe', background="#f5f5f5")
        style.configure('TLabelframe.Label', background="#f5f5f5")
    
    def create_dropdown(self, frame, label_text, name, values, default_idx, row):
        ttk.Label(frame, text=label_text).grid(row=row, column=0, sticky="e", padx=5, pady=5)
        setattr(self, name, ttk.Combobox(frame, values=values, state="readonly"))
        getattr(self, name).grid(row=row, column=1, sticky="ew", padx=5, pady=5)
        getattr(self, name).current(default_idx)
        frame.grid_columnconfigure(1, weight=1)
    
    def create_entry(self, frame, label_text, name, default_value, row):
        ttk.Label(frame, text=label_text).grid(row=row, column=0, sticky="e", padx=5, pady=5)
        setattr(self, name, ttk.Entry(frame, font=('Arial', 10)))
        getattr(self, name).grid(row=row, column=1, sticky="ew", padx=5, pady=5)
        getattr(self, name).insert(0, default_value)
    
    def calculate(self):
        try:
            # Girdileri al
            time = int(self.time.get().split(":")[0])
            play = int(self.play_time.get())
            school_day = 1 if self.school_day.get() == "Evet" else 0
            eye = int(self.eye_strain.get())
            prev_play = int(self.prev_play.get())
            
            # Değer kontrolü
            if not (0 <= play <= 360) or not (0 <= prev_play <= 360) or not (1 <= eye <= 10):
                raise ValueError("Geçersiz giriş değerleri")
            
            # Fuzzy hesaplama
            sim = ctrl.ControlSystemSimulation(system)
            sim.input['time_of_day'] = time
            sim.input['play_duration'] = play
            sim.input['is_school_day'] = school_day
            sim.input['eye_strain'] = eye
            sim.input['previous_play'] = prev_play
            sim.compute()
            
            # Sonuçları göster
            result_text = f"⏱ Önerilen Mola Süresi: {sim.output['break_duration']:.0f} dakika\n"
            result_text += f"🎮 İzin Verilen Oyun Süresi: {sim.output['allowed_play']:.0f} dakika"
            
            # Ekstra öneriler
            if eye >= 8:
                result_text += "\n\n❗ Gözleriniz çok yorgun, 15-20 dakika gözlerinizi dinlendirin"
            if time >= 22:
                result_text += "\n\n🌙 Geç saatte oyun oynamak uyku düzeninizi bozabilir"
            
            self.result_label.config(text=result_text)
            
        except ValueError as e:
            messagebox.showerror("Hata", "Lütfen geçerli değerler girin:\n- Oyun süreleri 0-360 dakika\n- Göz yorgunluğu 1-10 arası")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu:\n{str(e)}")
    
    def show_graphs(self):
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Üyelik Fonksiyonları Grafikleri")
        graph_window.geometry("900x700")
        
        fig = Figure(figsize=(9, 7), dpi=100)
        fig.set_facecolor('#f5f5f5')
        
        # 7 grafik için 3x3 grid (son 2 boş kalacak)
        ax1 = fig.add_subplot(331)
        ax2 = fig.add_subplot(332)
        ax3 = fig.add_subplot(333)
        ax4 = fig.add_subplot(334)
        ax5 = fig.add_subplot(335)
        ax6 = fig.add_subplot(336)
        ax7 = fig.add_subplot(337)
        
        # Grafikleri çiz
        self.plot_membership(time_of_day, "Günün Saati", ax1)
        self.plot_membership(play_duration, "Oyun Süresi (dk)", ax2)
        self.plot_membership(is_school_day, "Okul Günü mü?", ax3)
        self.plot_membership(eye_strain, "Göz Yorgunluğu", ax4)
        self.plot_membership(previous_play, "Dünün Oyun Süresi (dk)", ax5)
        self.plot_membership(break_duration, "Mola Süresi (dk)", ax6)
        self.plot_membership(allowed_play, "İzin Verilen Süre (dk)", ax7)
        
        fig.tight_layout(pad=3.0)
        
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Kapatma butonu
        btn_frame = ttk.Frame(graph_window)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Kapat", command=graph_window.destroy).pack()
    
    def plot_membership(self, var, title, ax):
        ax.set_title(title, fontsize=10)
        for term in var.terms:
            ax.plot(var.universe, var[term].mf, label=term)
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_facecolor('#f9f9f9')

# Uygulamayı başlat
if __name__ == "__main__":
    root = tk.Tk()
    app = OyunSuresiSinirlayici(root)
    root.mainloop()