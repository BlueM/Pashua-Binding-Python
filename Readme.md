Overview
===========

This is a Python (version 2 or 3) language binding (glue code) for using [Pashua](http://www.bluem.net/jump/pashua) from Python. Pashua is a Mac OS X application for using native GUI dialog windows in various programming languages.

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
This code requires Python 2.6 or newer and should run with the default Python 2.6/2.7 installations shipped with OS X 10.6 or later as well as with Python 3.5.

It is compatible with Pashua 0.10. It will work with earlier versions of Pashua, but non-ASCII characters will not be displayed correctly, as any versions before 0.10 required an argument for marking input as UTF-8.


Authors
=========
James Reese, Tor Sigurdsson, Canis Lupus, Ed Heil, Alex Chan, Carsten Blüm


License
=========
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
