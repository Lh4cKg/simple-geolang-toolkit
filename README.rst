===========
Description
===========

``geolang`` is Simple Georgian Language ToolKit for Python 3

Installation Requirements
-----------------------------------

* Python 3.0, 3.1, 3.2, 3.3, 3.4, 3.5
* Django >= 1.7 
* To install the source, download it from https://github.com/Lh4cKg/simple-geolang-toolkit and do ``python setup.py install``.

A simple way to install ``geolang`` package::

    $ pip install geolang
    $ pip install -r requirements.txt

To install the source ``geolang`` package::

    $ git clone https://github.com/Lh4cKg/simple-geolang-toolkit "geolang"
    $ cd geolang
    $ sudo python setup.py install # if you do not have a default Python 3, then use the python3 install instead of python install
    $ pip install -r requirements.txt

Usage
---------

To use ``geolang``, just import it in your project like so:

>>> import geolang as _ka

You can convert the Latin words in Georgian

>>> latin_to_ka = _ka._2KA
>>> _text_2ka = "i love you python and django"
>>> latin_to_ka(_text_2ka)
ი ლოვე  ყოუ  პყტჰონ  ანდ  დჯანგო

You can convert the Georgian words in Latin

>>> ka_to_latin = _ka._2LAT
>>> _text_2lat = "მე მიყვარს ანი"
>>> ka_to_latin(_text_2lat)
me miyvars ani

>>> encode_slugify = _ka.encode_slugify
>>> _try_encode_slugify = "ი ლოვე ყოუ პყტჰონ ანდ დჯანგო"
>>> encode_slugify(_try_encode_slugify)
b'i-love-you-python-and-django'
>>> encode_slugify(_try_encode_slugify, _slugify=False)
b'i love you python and django'
>>> _try_encode_slugify_1 = "é\jcàé\jcàétéétéé\jéé\jcàété\jcàétécàété"
>>> encode_slugify(_try_encode_slugify_1)
b'ejcaejcaeteeteejeejcaetejcaetecaete'

 See more examples_ in this project.

Source Code
-----------------

The source code can be found on github_.

Contributing
-----------------

There are plenty of ways to contribute to this project. If you think you’ve found a bug please submit an issue_.

License
------------------

``geolang`` is distributed under MIT license_. 


.. _examples: https://github.com/Lh4cKg/simple-geolang-toolkit/blob/master/example.py
.. _github: https://github.com/Lh4cKg/simple-geolang-toolkit
.. _issue: https://github.com/Lh4cKg/simple-geolang-toolkit/issues
.. _license: https://github.com/Lh4cKg/simple-geolang-toolkit/blob/master/LICENSE.md