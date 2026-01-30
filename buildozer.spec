[app]
title = TITANIUM NEXUS
package.name = titanium_nexus
package.domain = com.ismayil.titanium
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Stabil tələblər
requirements = python3,kivy==2.3.0,pyjnius,requests,urllib3,certifi

orientation = portrait
fullscreen = 1

# Android Ayarları (Stabil API 33)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

log_level = 2
