[app]
title = Oxygen App
package.name = oxygenapp
package.domain = org.oxygen
source.dir = .
source.exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,plyer,android,urllib3,certifi,idna,charset-normalizer,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.min_api = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
