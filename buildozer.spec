[app]

# (str) Title of your application
title = Jagadish App

# (str) Package name
package.name = jagadishapp

# (str) Package domain (needed for android packaging)
package.domain = org.jagadish

# (list) Source files to include (let it include python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# ನಿಮ್ಮ ಆ್ಯಪ್‌ಗೆ ಬೇಕಾದ ಲೈಬ್ರರಿಗಳನ್ನು ಇಲ್ಲಿ ನೀಡಿ (ಉದಾಹರಣೆಗೆ kivy ಬಳಸಿದರೆ)
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
