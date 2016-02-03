#!/usr/bin/env python

# -*- coding: utf-8 -*

__author__ = 'Lasha Gogua'

"""
Georgian Language Toolkit for Python 3
"""

# python imports
import re

# django imports
from django.template.defaultfilters import slugify

# package imports
from unicode import unicode

class GeoLangToolKit(object):

	def __init__(self):
		"""
		Desc: georgian and latin alphabet
		ანბანში დამატებითი ასოები აღნიშნულია, შემდეგი ასოებით:
			თ - T
			ჟ - J
			ღ - R
			შ - S
			ჩ - C
			ძ - Z
			ჭ - W
		"""

		self.KA_GE = 'აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'
		self.LATIN = 'abgdevzTiklmnopJrstufqRySCcZwWxjh'
		self.LAT_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
		self.UNICODE = unicode

	@property
	def KA2LAT(self):
		"""
		    Desc: character map of georgian to latin

		    >>> # example
		    >>> KA2LAT()
		    {'ხ': 'x', 'ა': 'a', 'ჭ': 'W', 'ჟ': 'J', 'ბ': 'b', 'რ': 'r', 'დ': 'd', 'ნ': 'n', 'ჩ': 'C', 'ფ': 'f', 'უ': 'u', 'თ': 'T', 'პ': 'p', 
		      'ტ': 't', 'ზ': 'z', 'ი': 'i', 'ლ': 'l', 'წ': 'w', 'გ': 'g', 'ღ': 'R', 'ე': 'e', 'მ': 'm', 'ყ': 'y', 'ვ': 'v', 'შ': 'S', 'ჰ': 'h', 
		      'კ': 'k', 'ძ': 'Z', 'ქ': 'q', 'ო': 'o', 'ჯ': 'j', 'ც': 'c', 'ს': 's'}
		"""

		convert = {c: i for i, c in zip(self.KA_GE,self.LATIN)}
		return convert

	@property
	def LAT2KA(self):
		"""
		    Desc: character map of latin to georgian

		    >>> # example
		    >>> LAT2KA()
		    {'S': 'შ', 'W': 'ჭ', 'k': 'კ', 'u': 'უ', 'n': 'ნ', 'R': 'ღ', 'o': 'ო', 'a': 'ა', 'b': 'ბ', 'v': 'ვ', 'x': 'ხ', 'j': 'ჯ', 'p': 'პ',
		      'C': 'ჩ', 't': 'ტ', 'J': 'ჟ', 's': 'ს', 'l': 'ლ', 'r': 'რ', 'Z': 'ძ', 'm': 'მ', 'i': 'ი', 'h': 'ჰ', 'q': 'ქ', 'e': 'ე', 'T': 'თ', 
		      'c': 'ც', 'd': 'დ', 'z': 'ზ', 'g': 'გ', 'w': 'წ', 'y': 'ყ'}
		"""

		convert = {c: i for i, c in zip(self.LATIN, self.KA_GE)}
		return convert

	@property
	def UNI2LAT(self):
		"""
		Desc: character map of many unicode to latin
		"""

		convert = self.UNICODE
		return convert

	def _2KA(self,data):
		"""
		Desc: convert the given name from latin into georgian chars

		>>> # example
		>>> _2KA('laSas uyvars ani da piToni lol ))')
		ლაშას უყვარს ანი და პითონი ლოლ
		"""

		converted = []
		_KAchars = self.KA2LAT.keys()
		i = 0
		while i < len(data.lower()):
			char = data[i]
			i += 1
			try:
				converted.append(self.KA2LAT[char])
			except KeyError:
				if char in _KAchars:
					converted.append(char)
				else:
					converted.append(' ')

		return ''.join(converted)

	def _2LAT(self,data):
		"""
		Desc: convert the given name from georgian into latin chars

		>>> # example
		>>> _2LAT('მე მიყვარს ანი, ის ცხოვრობს თბილიში!')
		me miyvars ani  is cxovrobs TbiliSi
		"""

		converted = []
		_LATchars = self.KA2LAT.keys()
		i = 0
		while i < len(data.lower()):
			char = data[i]
			i += 1
			try:
				converted.append(self.LAT2KA[char])
			except KeyError:
				if char in _LATchars:
					converted.append(char)
				else:
					converted.append(' ')

		return ''.join(converted)

	def ENCODE_SLUGIFY(self,data,_slugify=True):
		"""
		   Desc: 

		   >>> # examples
		   >>> ENCODE_SLUGIFY("მე\'მიყვარს-ანი და ის/ჩემი ცხოვბრებაა! ჩ")
		   'memiyvars-ani-da-iscemi-cxovbrebaa-c'
		   >>> ENCODE_SLUGIFY("adé\jcà l\'huété")
		   'adejca-lhuete'
		   >>> ENCODE_SLUGIFY("更新时间") # not found unicode
		   ' '   
		   >>> ENCODE_SLUGIFY("მე\'მიყვარს-ანი და ის/ჩემი ცხოვბრებაა! ჩ",_slugify=False)
		   "me'miyvars-ani da is/Cemi cxovbrebaa! C"
		"""
		# _slugify = True
		def _rep_str(data):
			"""
			    Desc: replace string
			"""

			_str = data.group()
			if _str in self.UNI2LAT:
				return self.UNI2LAT[_str]
			else:
				return _str

		value = re.sub('[^a-zA-Z0-9\\s\\-]{1}', _rep_str, data)
		if _slugify:
			value = slugify(value)

		result = value.encode('ascii','ignore')
		return result

_inst = GeoLangToolKit()
K2L = _inst.KA2LAT
L2K = _inst.LAT2KA
U2L = _inst.UNI2LAT
to_ka = _inst._2KA
to_lat = _inst._2LAT
encode_slugify = _inst.ENCODE_SLUGIFY
print(to_ka('Z'))
print(to_lat('ძ'))
# print(U2L)
_try = encode_slugify("更新时间")
a = encode_slugify('')
a1 = encode_slugify('adé\jcà l\'huété')
_try2 = encode_slugify("მე\'მიყვარს-ანი და ის/ჩემი ცხოვბრებაა! ჩ",_slugify=False)
print(_try)
print(a1)
print(_try2)
