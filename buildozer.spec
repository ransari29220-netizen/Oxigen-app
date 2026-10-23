[app]

# (str) Title of your application
title = Oxygen

# (str) Package name
package.name = oxygen

# (str) Package domain (needed for android packaging)
package.domain = org.oxygen

# (list) Source files to include (let it include all python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
