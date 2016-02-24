#!/usr/bin/env python

# -*- coding: utf-8 -*

__author__ = "Lasha Gogua"
__version__ = "0.1.3"

"""
Georgian Language Toolkit for Python 3
"""

# python imports
import re
import unicodedata

# django imports
from django.utils.functional import allow_lazy
from django.utils.safestring import SafeText, mark_safe
from django.utils.encoding import force_text
from django.utils.six import text_type

# package imports
from .unicode import unicode as uc
from .unicode import unicode_version_ka as uni_v_ka


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
		self.LATIN_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
		self.UNICODE = uc
		self.UNI_V_KA = uni_v_ka

	@property
	def get_ka_alphabet(self):
		"""
			get georgian alphabet

			>>> get_ka_alphabet()
			აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ
		"""

		alphabet = self.KA_GE
		return alphabet

	@property
	def get_lat_alphabet(self):
		"""
			get latin alphabet

			>>> get_lat_alphabet()
			abcdefghijklmnopqrstuvwxyz
		"""

		alphabet = self.LATIN_ALPHABET
		return alphabet

	@property
	def KA2KA(self):
		"""
		Desc: georgian to georgian

		"""

		convert = {c: i for i, c in zip(self.KA_GE, self.KA_GE) }
		return convert

	@property
	def LAT2LAT(self):
		"""
		Desc: latin to latin
		"""

		convert = {c: i for i,c in zip(self.LATIN, self.LATIN)}
		return convert

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

	@property
	def UNI_V_KA2LAT(self):
		"""
		Desc: character map of many unicode to latin
		"""

		convert = self.UNI_V_KA
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

	def ENCODE_SLUGIFY(self,data,_slugify=True,_lower=False,_uni_v_ka=False):
		"""
		   Desc: 

		   >>> # examples
		   >>> ENCODE_SLUGIFY("მე\'მიყვარს-ანი და ის/ჩემი ცხოვბრებაა! ჩ")
		   'memiyvars-ani-da-iscemi-cxovbrebaa-c'
		   >>> ENCODE_SLUGIFY("adé\jcà l\'huété")
		   'adejca-lhuete'
		   >>> ENCODE_SLUGIFY("更新时间") # could not find unicode
		   ' '   
		   >>> ENCODE_SLUGIFY("მე\'მიყვარს-ანი და ის/ჩემი ცხოვბრებაა! ჩ",_slugify=False)
		   "me'miyvars-ani da is/Cemi cxovbrebaa! C"
		"""

		# _slugify = True
		def slugify(value):
			"""
			Desc: Converts to ASCII. Converts spaces to hyphens. Removes characters that
			aren't alphanumerics, underscores, or hyphens. Also strips leading and trailing whitespace.
			"""

			value = force_text(value)
			value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
			value = re.sub('[^\w\s-]', '', value).strip()
			return mark_safe(re.sub('[-\s]+', '-', value))
		
		slugify = allow_lazy(slugify, text_type, SafeText)

		def _rep_str(match):
			"""
			    Desc: replace string
			"""

			_str = match.group()
			if _str in self.UNI2LAT:
				return self.UNI2LAT[_str]
			else:
				return _str

		def _rep_str_uni_v_ka(match):
			"""
			    Desc: replace string
			"""

			_str = match.group()
			if _str in self.UNI_V_KA2LAT:
				return self.UNI_V_KA2LAT[_str]
			else:
				return _str

		if _lower is True:
			value = re.sub('[^a-zA-Z0-9\\s\\-]{1}', _rep_str, data).lower()
		else:
			value = re.sub('[^a-zA-Z0-9\\s\\-]{1}', _rep_str, data)

		if _lower is True and _uni_v_ka is True:
			value = re.sub('[^a-zA-Z0-9\\s\\-]{1}', _rep_str_uni_v_ka, data).lower()

		if _slugify:
			value = slugify(value)

		result = value.encode('ascii','ignore')
		return result


_inst = GeoLangToolKit()
_KA_ALPHABET = _inst.get_ka_alphabet
_LAT_ALPHABET = _inst.get_lat_alphabet
KA2KA = _inst.KA2KA
LAT2LAT = _inst.LAT2LAT
KA2LAT = _inst.KA2LAT
LAT2KA = _inst.LAT2KA
UNI2LAT = _inst.UNI2LAT
_2KA = _inst._2KA
_2LAT = _inst._2LAT
encode_slugify = _inst.ENCODE_SLUGIFY