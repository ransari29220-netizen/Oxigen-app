[app]

# (str) Title of your application
title = Oxygen

# (str) Package name
package.name = oxygen

# (str) Package domain (needed for android packaging)
package.domain = org.oxygen

# (str) Version of the application
version = 0.1

# (str) Source code directory (where main.py is located)
source.dir = .

# (list) Source files to include (let it include all python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android build tools version to use
android.build_tools_version = 33.0.2

[buildozer]
log_level = 2
warn_on_root = 1
