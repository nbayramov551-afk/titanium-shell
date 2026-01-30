from kivy.app import App
from kivy.uix.widget import Widget
from jnius import autoclass
from android.runnable import run_on_ui_thread

# Android sistem kitabxanaları
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity

class TitaniumApp(App):
    def build(self):
        # Boş bir widget yaradırıq, çünki biz birbaşa Android ekranını istifadə edəcəyik
        self.open_webview()
        return Widget()

    @run_on_ui_thread
    def open_webview(self):
        webview = WebView(Activity)
        settings = webview.getSettings()
        
        # Ən vacib ayarlar (Localhost üçün)
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setAllowFileAccess(True)
        
        webview.setWebViewClient(WebViewClient())
        
        # BURAYA DİQQƏT: Localhost üçün Termux IP-ni bura qoymalısan
        # Məsələn: webview.loadUrl("http://192.168.1.5:8080")
        webview.loadUrl("https://google.com") # İlk yoxlama üçün
        
        Activity.setContentView(webview)

if __name__ == '__main__':
    TitaniumApp().run()
    
