[app]
title = TITANIUM NEXUS
package.name = titanium_nexus
package.domain = com.ismayil.titanium
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# 2026-cı il üçün ən stabil tələblər
requirements = python3,kivy==2.3.0,pyjnius,requests,urllib3
orientation = portrait
fullscreen = 1

# Android Ayarları
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.skip_update = False

# İcazələr
android.permissions = INTERNET, ACCESS_NETWORK_STATE, CAMERA, RECORD_AUDIO

# Log səviyyəsi (Xətaları görmək üçün)
log_level = 2
