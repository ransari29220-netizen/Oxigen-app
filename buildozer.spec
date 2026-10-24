[app]

# (str) Title of your application
title = Oxygen App

# (str) Package name
package.name = oxygenapp

# (str) Package domain (needed for android packaging)
package.domain = org.oxygen

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion & exclusion patterns
source.include_patterns = assets/*,images/*.png

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,plyer,requests,urllib3,certifi,idna,charset-normalizer

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,VIBRATE

# (list) Orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color
#android.presplash_color = #FFFFFF

# (list) List of Java JARs to add to the libs/ directory
#android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android project (Gradle)
#android.add_src =

# (list) Gradle dependencies
#android.gradle_dependencies =

# (list) Add a custom proguard file
#android.proguard_rule =

# (list) Extra xml to add to AndroidManifest.xml
#android.manifest_extras =

# (list) Extra XML files to add to res/xml/ (e.g. for accessibility services)
#android.manifest_application_extras =

# (list) Source files to include (let it blank to include all files)
#android.app_licenses = ''

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86
# Supported by Python for Android since 2019-10-05 (only arm64-v8a is supported by Google Play since 2019-08-01)
android.archs = arm64-v8a

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --public (False)
android.private_storage = True

# (bool) Skip byte-code compilation for python files
#android.skip_bytecode = False

# (str) Format used to package the app for release/debug (aab or apk)
android.ant_path = 
android.build_mode = debug

# (bool) Enable Android SDK license agreement acceptance
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact, local or remote
bin_dir = bin

# (int) Display warning if not run as root
warn_root = 1
