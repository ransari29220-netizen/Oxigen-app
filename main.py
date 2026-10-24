from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from plyer import tts
import urllib.request
import json

class OxygenApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=25)
        
        # शुरुआत में एक साफ और लाइट बैकग्राउंड (हल्का ग्रे/सफेद)
        with self.layout.canvas.before:
            self.bg_color = Color(0.92, 0.94, 0.96, 1)
            self.rect = Rectangle(size=(1000, 1000), pos=(0, 0))
            self.layout.bind(size=self._update_rect, pos=self._update_rect)
        
        # ऐप का टाइटल - चमकदार और बोल्ड
        self.title_label = Label(
            text='[b][color=111111]OXYGEN AIR MONITOR[/color][/b]', 
            markup=True, 
            font_size='28sp',
            halign='center'
        )
        self.layout.add_widget(self.title_label)
        
        # डेटा दिखाने वाला लेबल - बड़ा और साफ़ टेक्स्ट
        self.status_label = Label(
            text='[color=222222]Live data check karne ke liye\n[b]Check Air Quality[/b] dabayein[/color]', 
            markup=True,
            font_size='22sp',
            halign='center',
            valign='middle'
        )
        self.layout.add_widget(self.status_label)
        
        # स्टाइलिश और चमकदार बटन
        self.check_btn = Button(
            text='Check Air Quality & Speak', 
            font_size='20sp',
            bold=True,
            size_hint=(1, 0.25),
            background_color=(0.08, 0.45, 0.85, 1) # सुंदर नीला रंग
        )
        self.check_btn.bind(on_press=self.fetch_weather_data)
        self.layout.add_widget(self.check_btn)
        
        return self.layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def fetch_weather_data(self, instance):
        try:
            url = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=28.6139&longitude=77.2090&current=pm2_5"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
            data = json.loads(response.read().decode())
            
            pm25 = data["current"]["pm2_5"]
            
            # हवा की स्थिति के हिसाब से सुंदर लाइट बैकग्राउंड और चमकदार टेक्स्ट
            with self.layout.canvas.before:
                if pm25 <= 50:
                    status = "[color=006622][b]Safe Air (Hawa bilkul saaf hai)[/b][/color]"
                    voice_msg = "Hawa bilkul saaf hai. Aap bina mask ke ghum sakte hain."
                    self.bg_color.rgba = (0.85, 0.98, 0.85, 1) # सॉफ्ट लाइट हरा
                elif pm25 <= 100:
                    status = "[color=996600][b]Moderate (Thoda pradooshan hai)[/b][/color]"
                    voice_msg = "Thoda pradushan hai. Savdhaan rahein."
                    self.bg_color.rgba = (0.98, 0.93, 0.75, 1) # सॉफ्ट लाइट पीला
                else:
                    status = "[color=cc0000][b]Toxic / Dangerous (Zahreeli hawa, mask pehno!)[/b][/color]"
                    voice_msg = "Zahreeli hawa hai! Kripya mask pehno aur ghar ke andar rahein."
                    self.bg_color.rgba = (0.98, 0.82, 0.82, 1) # सॉफ्ट लाइट गुलाबी/लाल
            
            self.status_label.text = f"[b]PM2.5 Level: {pm25}[/b]\n\n{status}"
            
            # ऐप बोलकर भी बताएगा
            tts.speak(voice_msg)
            
        except Exception as e:
            self.status_label.text = "[color=ff0000]Internet connection check karein![/color]"

if __name__ == '__main__':
    OxygenApp().run()
