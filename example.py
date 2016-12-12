#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
# USAGE INFORMATION:
# As you can see this text, you obviously have opened the file in a text editor.
#
# If you would like to *run* this example rather than *read* it, you
# should open Terminal.app, drag this document's icon onto the terminal
# window, bring Terminal.app to the foreground (if necessary) and hit return.
#

from __future__ import print_function
import Pashua
import os.path

conf = u"""
# Set window title
*.title = Welcome to Pashua

# Introductory text
txt.type = text
txt.default = Pashua is an application for generating dialog windows from \
programming languages which lack support for creating native GUIs on Mac OS X.\
Any information you enter in this example window will be returned to the \
calling script when you hit “OK”; if you decide to click “Cancel” or press \
“Esc” instead, no values will be returned.[return][return]This window shows\
nine of the UI element types that are available. You can find a full list \
of all GUI elements and their corresponding attributes in the documentation \
(➔ Help menu) that is included with Pashua.
txt.height = 276
txt.width = 310
txt.x = 340
txt.y = 44
txt.tooltip = This is an element of type “text”

# Add a text field
tf.type = textfield
tf.label = Example textfield
tf.default = Textfield content
tf.width = 310
tf.tooltip = This is an element of type “textfield”

# Add a filesystem browser
ob.type = openbrowser
ob.label = Example filesystem browser (textfield + open panel)
ob.width=310
ob.tooltip = This is an element of type “openbrowser”

# Define radiobuttons
rb.type = radiobutton
rb.label = Example radiobuttons
rb.option = Radiobutton item #1
rb.option = Radiobutton item #2
rb.option = Radiobutton item #3
rb.tooltip = This is an element of type “radiobutton”

# Add a popup menu
pop.type = popup
pop.label = Example popup menu
pop.width = 310
pop.option = Popup menu item #1
pop.option = Popup menu item #2
pop.option = Popup menu item #3
pop.default = Popup menu item #2
pop.tooltip = This is an element of type “popup”

# Add 2 checkboxes
chk.rely = -18
chk.type = checkbox
chk.label = Pashua offers checkboxes, too
chk.tooltip = This is an element of type “checkbox”
chk.default = 1
chk2.type = checkbox
chk2.label = But this one is disabled
chk2.disabled = 1
chk2.tooltip = Another element of type “checkbox”

# Add a cancel button with default label
cb.type = cancelbutton
cb.tooltip = This is an element of type “cancelbutton”

db.type = defaultbutton
db.tooltip = This is an element of type “defaultbutton” (which is \
automatically added to each window, if not included in the configuration)

"""

# Set the images' paths relative to Pashua.app's path
app_bundle = os.path.dirname(os.path.dirname(Pashua.locate_pashua()))
icon = app_bundle + '/Resources/AppIcon@2.png'

if os.path.exists(icon):
    # Display Pashua's icon
    conf += u"""img.type = image
                img.x = 435
                img.y = 248
                img.maxwidth = 128
                img.tooltip = This is an element of type 'image'
                img.path = %s""" % icon

result = Pashua.run(conf.encode('utf8'))

print("Pashua returned the following dictionary keys and values:")

for key in result.keys():
    print("%s = %s" % (key, result[key]))
