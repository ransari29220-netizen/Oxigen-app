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

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*.png,images/*.jpg

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*.jpg

# (list) List of directory to exclude
#source.exclude_dirs = tests, bin

# (list) Application versioning (method 1)
version = 0.1

# (list) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,requests

# (str) Custom source folders for requirements
#requirements.source.dir = ../../../

# (list) Permissions
#android.permissions = INTERNET

# (str) Orientation of the application
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PYTHON_SCRIPT,NAME2:ENTRYPOINT_TO_PYTHON_SCRIPT

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (hex color code)
#android.presplash_color = #FFFFFF

# (list) The Android archs to build for,, defaults to armeabi-v7a.
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) Use AndroidX support
android.androidx = True
