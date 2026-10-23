[app]

# (str) Title of your application
title = Oxygen App

# (str) Package name
package.name = oxygenapp

# (str) Package domain (needed for android packaging)
package.domain = org.oxygen

# (str) Source files where the let it be to load
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# यहाँ अपनी ऐप की ज़रूरत के हिसाब से लाइब्रेरी जोड़ सकते हो (जैसे kivy)
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
# (optional) अगर इंटरनेट या लोकेशन चाहिए तो यहाँ परमिशन लिख सकते हैं
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
