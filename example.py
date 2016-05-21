#!/usr/bin/env python

# -*- coding: utf-8 -*

import geolang as _ka
from geolang import __author__, __version__


K2L = _ka.ka2Lat
L2K = _ka.lat2Ka
_2KA = _ka._2ka
_2LAT = _ka._2lat
encode_slugify = _ka.encode_slugify

"""
>>> K2L
{'ჩ': 'C', 'დ': 'd', 'ჟ': 'J', 'კ': 'k', 'უ': 'u', 'ხ': 'x', 'ქ': 'q', 'ვ': 'v', 'ღ': 'R', 'მ': 'm', 'ნ': 'n', 'გ': 'g', 'ტ': 't', 
'ძ': 'Z', 'წ': 'w', 'ფ': 'f', 'ზ': 'z', 'ი': 'i', 'ყ': 'y', 'ა': 'a', 'ს': 's', 'ე': 'e', 'შ': 'S', 'ჭ': 'W', 'ჰ': 'h', 'რ': 'r', 
'ო': 'o', 'თ': 'T', 'ბ': 'b', 'ლ': 'l', 'ც': 'c', 'პ': 'p', 'ჯ': 'j'}
"""
print(K2L)

"""
>>> L2K
{'x': 'ხ', 'b': 'ბ', 'd': 'დ', 'C': 'ჩ', 'Z': 'ძ', 'i': 'ი', 'q': 'ქ', 'e': 'ე', 'S': 'შ', 'p': 'პ', 's': 'ს', 'a': 'ა', 'f': 'ფ', 'u': 'უ', 
'n': 'ნ', 'v': 'ვ', 'T': 'თ', 'h': 'ჰ', 'y': 'ყ', 'r': 'რ', 't': 'ტ', 'j': 'ჯ', 'z': 'ზ', 'g': 'გ', 'R': 'ღ', 'l': 'ლ', 'J': 'ჟ', 'w': 'წ', 
'c': 'ც', 'W': 'ჭ', 'o': 'ო', 'k': 'კ', 'm': 'მ'}
"""
print(L2K)

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
print('Author is %s, Package version is %s.' % (__author__,__version__))

name = 'ლაშას უყვარს ანი. ჩ,ჟ,ჭ,თ,ძ,ღ'
print(encode_slugify(name, _slugify=True, _lower=True, uni_ka=True))