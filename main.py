from kivy.app import App
from kivy.uix.vbox import BoxLayout
from android.runnable import run_on_ui_thread
from jnius import autoclass

# Android-in daxili komponentləri
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity

class TitaniumShell(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.create_webview()
        return self.layout

    @run_on_ui_thread
    def create_webview(self):
        webview = WebView(Activity)
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setDatabaseEnabled(True)
        settings.setAllowFileAccess(True)
        settings.setMixedContentMode(0)
        
        webview.setWebViewClient(WebViewClient())
        
        # 🔗 LİNKİNİ BURAYA QOY
        webview.loadUrl("SƏNİN_CANLI_LİNKİN") 
        
        Activity.setContentView(webview)

if __name__ == '__main__':
    TitaniumShell().run()
  
