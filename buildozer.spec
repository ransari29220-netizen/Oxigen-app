[app]

# (str) Title of your application
title = Oxygen

# (str) Package name
package.name = oxygen

# (str) Package domain (needed for android packaging)
package.domain = org.example

# (str) Source files where the let's go (relative to directory of this file)
source.dir = .

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,requests

# (list) Permissions
android.permissions = INTERNET

# (str) Orientation of the application
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) The Android archs to build for, defaults to armeabi-v7a.
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Explicit build-tools version to avoid license and aidl errors
android.build_tools_version = 30.0.3

# (str) Android NDK version
android.ndk = 25b

# (bool) Use AndroidX support
android.androidx = True
