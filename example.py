#!/usr/bin/env python

# -*- coding: utf-8 -*



import geolang as _ka

K2L = _ka.KA2LAT
L2K = _ka.LAT2KA
U2T = _ka.UNI2LAT
_2KA = _ka._2KA
_2LAT = _ka._2LAT
encode_slugify = _ka.encode_slugify

print(K2L)
print(L2K)
print(U2T)
_try_2ka = "I Love You Python And Django"
"""
>>> _try_2ka = "I Love You Python And Django"
>>> _2KA(_try_2ka)
   ოვე  ოუ  ყტჰონ  ნდ  ჯანგო
"""
print(_2KA(_try_2ka))

_try_2lat = "მე მიყვარს ანი"
"""
>>> _try_2lat = "მე მიყვარს ანი"
>>> _2LAT(_try_2lat)
me miyvars ani
"""
print(_2LAT(_try_2lat))

_try_encode_slugify = "ი ლოვე ყოუ პყტჰონ ანდ დჯანგო"
"""
>>> _try_encode_slugify = "ი ლოვე ყოუ პყტჰონ ანდ დჯანგო"
>>> encode_slugify(_try_encode_slugify)
b'i-love-you-python-and-django'
"""
print(encode_slugify(_try_encode_slugify))

_try_encode_slugify_1 = "é\jcàé\jcàétéétéé\jéé\jcàété\jcàétécàété"
"""
>>> _try_encode_slugify_1 = "é\jcàé\jcàétéétéé\jéé\jcàété\jcàétécàété"
>>> encode_slugify(_try_encode_slugify_1)
b'ejcaejcaeteeteejeejcaetejcaetecaete'
"""
print(encode_slugify(_try_encode_slugify_1))
