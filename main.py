from kivy.app import App
from kivy.uix.vbox import BoxLayout
from android.runnable import run_on_ui_thread
from jnius import autoclass

WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity

class TitaniumApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.open_link()
        return self.layout

    @run_on_ui_thread
    def open_link(self):
        webview = WebView(Activity)
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        webview.setWebViewClient(WebViewClient())
        # ÖZ REAL LİNKİNİ BURAYA YAZ
        webview.loadUrl("https://sənin-sayt-linkin.com")
        Activity.setContentView(webview)

if __name__ == '__main__':
    TitaniumApp().run()
    
