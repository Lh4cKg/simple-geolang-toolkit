#!/usr/bin/env python

# -*- coding: utf-8 -*

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
from .unicode import unicode_all as uc_all, unicode_ka as uc_ka

__author__ = "Lasha Gogua"
__version__ = "0.1.4"


class GeoLangToolKit(object):
    """
    Note
     -
    Args
     -
    Attributes
     -
    """
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

        self._ka_ge = 'აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'
        self._latin_ka = 'abgdevzTiklmnopJrstufqRySCcZwWxjh'
        self._latin = 'abcdefghijklmnopqrstuvwxyz'
        self._unicode_all = uc_all
        self._unicode_ka = uc_ka

    @property
    def ka_ge(self):
        """
            get georgian alphabet

            >>> ka_ge()
            'აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'
        """

        alphabet = self._ka_ge
        return alphabet

    @property
    def latin(self):
        """
            get latin alphabet

            >>> latin()
            'abcdefghijklmnopqrstuvwxyz'
        """

        alphabet = self._latin
        return alphabet

    @property
    def latin_ka(self):
        """
            get latin_ka alphabet

            >>> latin_ka()
            'abgdevzTiklmnopJrstufqRySCcZwWxjh'
        """

        alphabet = self._latin
        return alphabet

    @property
    def __ka2ka(self):
        """
        Desc: georgian to georgian
        """

        convert = {c: i for i, c in zip(self.ka_ge, self.ka_ge)}
        return convert

    @property
    def __lat2lat(self):
        """
        Desc: latin to latin
        """

        convert = {c: i for i, c in zip(self.latin_ka, self.latin_ka)}
        return convert

    @property
    def ka2lat(self):
        """
            Desc: character map of georgian to latin

            >>> # example
            >>> ka2lat()
            {'ხ': 'x', 'ა': 'a', 'ჭ': 'W', 'ჟ': 'J', 'ბ': 'b', 'რ': 'r', 'დ': 'd',
              'ნ': 'n', 'ჩ': 'C', 'ფ': 'f', 'უ': 'u', 'თ': 'T', 'პ': 'p',
              'ტ': 't', 'ზ': 'z', 'ი': 'i', 'ლ': 'l', 'წ': 'w', 'გ': 'g', 'ღ': 'R',
              'ე': 'e', 'მ': 'm', 'ყ': 'y', 'ვ': 'v', 'შ': 'S', 'ჰ': 'h',
              'კ': 'k', 'ძ': 'Z', 'ქ': 'q', 'ო': 'o', 'ჯ': 'j', 'ც': 'c', 'ს': 's'}
        """

        convert = {c: i for i, c in zip(self.ka_ge, self.latin_ka)}
        return convert

    @property
    def lat2ka(self):
        """
            Desc: character map of latin to georgian

            >>> # example
            >>> lat2ka()
            {'S': 'შ', 'W': 'ჭ', 'k': 'კ', 'u': 'უ', 'n': 'ნ', 'R': 'ღ', 'o': 'ო',
               'a': 'ა', 'b': 'ბ', 'v': 'ვ', 'x': 'ხ', 'j': 'ჯ', 'p': 'პ',
              'C': 'ჩ', 't': 'ტ', 'J': 'ჟ', 's': 'ს', 'l': 'ლ', 'r': 'რ', 'Z': 'ძ',
              'm': 'მ', 'i': 'ი', 'h': 'ჰ', 'q': 'ქ', 'e': 'ე', 'T': 'თ',
              'c': 'ც', 'd': 'დ', 'z': 'ზ', 'g': 'გ', 'w': 'წ', 'y': 'ყ'}
        """

        convert = {c: i for i, c in zip(self.latin_ka, self.ka_ge)}
        return convert

    @property
    def __uni2lat(self):
        """
        Desc: character map of many unicode to latin
        """

        convert = self._unicode_all
        return convert

    @property
    def __uni_ka2lat(self):
        """
        Desc: character map of many unicode to latin
        """

        convert = self._unicode_ka
        return convert

    def _2ka(self, data):
        """
        Desc: convert the given name from latin into georgian chars

        >>> # example
        >>> _2ka('laSas uyvars ani da piToni lol ))')
        ლაშას უყვარს ანი და პითონი ლოლ
        """

        converted = []
        ka_chars = self.ka2lat.keys()
        i = 0
        while i < len(data.lower()):
            char = data[i]
            i += 1
            try:
                converted.append(self.ka2lat[char])
            except KeyError:
                if char in ka_chars:
                    converted.append(char)
                else:
                    converted.append(' ')

        return ''.join(converted)

    def _2lat(self, data):
        """
        Desc: convert the given name from georgian into latin chars

        >>> # example
        >>> _2lat('მე მიყვარს ანი, ის ცხოვრობს თბილიში!')
        me miyvars ani  is cxovrobs TbiliSi
        """

        converted = []
        lat_chars = self.ka2lat.keys()
        i = 0
        while i < len(data.lower()):
            char = data[i]
            i += 1
            try:
                converted.append(self.lat2ka[char])
            except KeyError:
                if char in lat_chars:
                    converted.append(char)
                else:
                    converted.append(' ')

        return ''.join(converted)

    def encode_slugify(self, data, _slugify=True, _lower=False, uni_ka=False):
        """
           Desc:

           >>> # examples
           >>> ENCODE_SLUGIFY("მე\'მიყვარს-ანი და ის/ჩემი ცხოვბრებაა! ჩ")
           'memiyvars-ani-da-iscemi-cxovbrebaa-c'
           >>> ENCODE_SLUGIFY("adé\jcà lr\r'huété")
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
            aren't alphanumerics, underscores, or hyphens.
            Also strips leading and trailing whitespace.
            """

            value = force_text(value)
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
            value = re.sub(r'[^\w\s-]', '', value).strip()
            return mark_safe(re.sub(r'[-\s]+', '-', value))

        slugify = allow_lazy(slugify, text_type, SafeText)

        def _rep_str(match):
            """
                Desc: replace string
            """

            _str = match.group()

            if uni_ka:
                if _str in self.__uni_ka2lat:
                    return self.__uni_ka2lat[_str]
                else:
                    return _str
            else:
                if _str in self.__uni2lat:
                    return self.__uni2lat[_str]
                else:
                    return _str


        if _lower is True:
            value = re.sub(r'[^a-zA-Z0-9\\s\\-]{1}', _rep_str, data).lower()
        else:
            value = re.sub(r'[^a-zA-Z0-9\\s\\-]{1}', _rep_str, data)

        if _lower is True and uni_ka is True:
            value = re.sub(r'[^a-zA-Z0-9\\s\\-]{1}', _rep_str, data).lower()

        if _slugify:
            value = slugify(value)

        # result = value.encode('ascii', 'ignore')
        result = '%s' % value
        return result

instance = GeoLangToolKit()
ka2Lat = instance.ka2lat
lat2Ka = instance.lat2ka
_2ka = instance._2ka
_2lat = instance._2lat
encode_slugify = instance.encode_slugify
