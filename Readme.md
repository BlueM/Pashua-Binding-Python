Overview
===========

This is a Python 2 language binding (glue code) for using [Pashua](http://www.bluem.net/jump/pashua) from Python. Pashua is a Mac OS X application for using native GUI dialog windows in various programming languages.

This code can be found in a GitHub repository at https://github.com/BlueM/Pashua-Binding-Python. For examples in other programming languages, see https://github.com/BlueM/Pashua-Bindings.


Usage
======

The repository contains two files:

* `Pashua.py`, a Python module which handles the communication with Pashua
* `example.py`, a simple script wich uses `Pashua.py` to display a dialog´

The way the example and the module work is neither the best nor the only way to “talk” to Pashua from within Python, but rather one out of several possibe implementations.

Of course, you will need Pashua on your Mac to run the example. The code expects Pashua.app in one of the “typical” locations, such as `/Applications` or `~/Applications`, or in the folder which contains `example.py`.


Compatibility
=============
This code requires Python 2.6 or newer and should run with the default Python installation that ships with Mac OS X 10.6 or later.

It is compatible with Pashua 0.10. It will work with earlier versions of Pashua, but non-ASCII characters will not be displayed correctly, as any versions before 0.10 required an argument for marking input as UTF-8.

