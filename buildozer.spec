[app]

# (str) Title of your application
title = Oxygen App

# (str) Package name
package.name = oxygenapp

# (str) Package domain (needed for android packaging)
package.domain = org.oxygen

# (str) Source where the app lives
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion & exclusion patterns
source.include_patterns = assets/*,images/*.png

# (list) Application requirements
requirements = python3,kivy,plyer,requests,urllib3,certifi,idna,charset-normalizer

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,VIBRATE

# (list) Orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) The Android arch to build for
android.archs = arm64-v8a

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage
android.private_storage = True

# (str) Format used to package the app for release/debug
android.build_mode = debug

# (bool) Enable Android SDK license agreement acceptance
android.accept_sdk_license = True

[buildozer]
log_level = 2
bin_dir = bin
warn_root = 1
