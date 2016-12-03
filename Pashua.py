"""
Pashua.py - Interface to Pashua

Pashua is an application that can be used to provide some type of dialog GUI
for Python and shell applications on Mac OS X. Pashua.py is the glue between
your script and Pashua. To learn more about Pashua, take a look at the
application's Readme file. Pashua's homepage is www.bluem.net/jump/pashua
Please note in order for the example to work, the Pashua application
must be in the current path, in /Applications/ or in ~/Applications/
If none of these paths apply, you will have to specify it manually:
Pashua.PATH = '/path/to/appfolder';
... before you call Pashua.run(). Alternatively, you may specify the
path (the directory that contains Pashua.app, without trailing slash)
as 3rd argument to run().

"""

import os.path
import sys
import subprocess

BUNDLE_PATH = "Pashua.app/Contents/MacOS/Pashua"

PASHUA_PLACES = [
    os.path.join(os.path.dirname(sys.argv[0]), "Pashua"),
    os.path.join(os.path.dirname(sys.argv[0]), BUNDLE_PATH),
    os.path.join(".", BUNDLE_PATH),
    os.path.join("/Applications", BUNDLE_PATH),
    os.path.join(os.path.expanduser("~/Applications"), BUNDLE_PATH),
    os.path.join("/usr/local/bin", BUNDLE_PATH)
]


# Find Pashua by looking in each of the search locations, returning the first
# matching path. Will raise an exception, if Pashua.app cannot be found.
def locate_pashua(pashua_path=None):
    if pashua_path:
        # Custom path given
        PASHUA_PLACES.insert(0, pashua_path + '/' + BUNDLE_PATH)

    for bundle_path in PASHUA_PLACES:
        if os.path.exists(bundle_path):
            return bundle_path

    raise IOError("Unable to locate the Pashua application.")


# Calls the pashua executable, parses its result string and generates
# a dictionary that's returned.
def run(config_data, pashua_path=None):

    # Get path to the executable inside Pashua.app
    app_path = locate_pashua(pashua_path)


    # Send string to pashua standard input, receive result.
    s=subprocess.Popen([app_path,  "-"],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    result, _ = s.communicate(input=config_data)

    # Parse result
    d = {}
    for line in result.decode('utf8').splitlines():
        if '=' in line: # avoid empty lines.
            k, _, v = line.partition('=')
            d[k] = v.rstrip()

    return d
