===========
Description
===========

``geolang`` is Simple Georgian Language ToolKit for Python 3

Installation Requirements
-----------------------------------

* Python >= 3.6

* To install the source, download it from https://github.com/Lh4cKg/simple-geolang-toolkit and do ``python setup.py install``.

A simple way to install ``geolang`` package::

    $ pip install geolang

To install the source ``geolang`` package::

    $ git clone https://github.com/Lh4cKg/simple-geolang-toolkit "geolang"
    $ cd geolang
    $ python3 setup.py build
    $ python3 setup.py install

Usage
---------

To use ``geolang``, just import it in your project like so:

>>> from geolang import encode_slugify, encode_text

You can convert the Latin words in Georgian

>>> txt = "i love you python and django"
>>> encode_text(txt)
'ი ლოვე yოუ ფyტჰონ ანდ დჯანგო'

You can convert the Georgian words in Latin

>>> txt = "მე მიყვარს ანი"
>>> encode_text(txt)
'me miqvars ani'

>>> txt = "ი ლოვე ყოუ პყტჰონ ანდ დჯანგო"
>>> encode_slugify(txt)
'ი-ლოვე-ყოუ-პყტჰონ-ანდ-დჯანგო'
>>> encode_slugify(txt)
'i-love-qou-pqthon-and-django'
>>> txt = "é\jcàé\jcàétéétéé\jéé\jcàété\jcàétécàété"
>>> encode_slugify(_try_encode_slugify_1)
'éjcàéjcàétéétééjééjcàétéjcàétécàété'

 See more tests_ in this project.

Source Code
-----------------

The source code can be found on github_.

Contributing
-----------------

There are plenty of ways to contribute to this project. If you think you’ve found a bug please submit an issue_.

License
------------------

``geolang`` is distributed under MIT license_.


.. _tests: https://github.com/Lh4cKg/simple-geolang-toolkit/blob/master/tests.py
.. _github: https://github.com/Lh4cKg/simple-geolang-toolkit
.. _issue: https://github.com/Lh4cKg/simple-geolang-toolkit/issues
.. _license: https://github.com/Lh4cKg/simple-geolang-toolkit/blob/master/LICENSE.md