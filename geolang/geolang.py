# -*- coding: utf-8 -*

"""
Georgian Language Toolkit for Python 3

Source: <https://github.com/Lh4cKg/simple-geolang-toolkit>
"""

import re
from typing import Dict, Any, Iterable, Union, List, Tuple
from functools import lru_cache, partial
from unicodedata import normalize


__author__ = 'Lasha Gogua'
__email__ = 'Lh4cKg@gmail.com'
__version__ = '0.2.0'

__all__ = ['GeoLangToolKit', 'encode_slugify', 'encode_text']


class GeoLangToolKit(object):

    def __init__(
            self,
            ka2latin_script: Union[str, List[str], Tuple[Iterable[str]]] = None
    ) -> None:
        """
        Romanization of Georgian is the process of transliterating the Georgian
        language from the Georgian script into the Latin script.

        default script is National:
            თ - t
            კ - k'
            ტ - t'
            ფ - p
            ქ - k
            პ - p'
            ჟ - zh
            ღ - gh
            ყ - q'
            შ - sh
            ჩ - ch
            ც - ts
            ძ - dz
            წ - ts'
            ჭ - ch'
        """
        self.ka_script: str = 'აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'

        if isinstance(ka2latin_script, (list, tuple)):
            self.latin_script = ka2latin_script
        elif isinstance(ka2latin_script, str):
            if len(ka2latin_script) < 33:
                raise ValueError(
                    'Wrong latin script characters, available list, '
                    'tuple or comma separated string, max length 33.'
                )
            else:
                self.latin_script = ka2latin_script.split(',')
        else:
            self.latin_script: Iterable[str] = (
                'a', 'b', 'g', 'd', 'e', 'v', 'z', 't', 'i', 'k', 'l', 'm',
                'n', 'o', 'p', 'zh', 'r', 's', 't', 'u', 'p', 'k', 'gh', 'q',
                'sh', 'ch', 'ts', 'dz', 'ts', 'ch', 'kh', 'j', 'h'
            )

    @property
    @lru_cache
    def ka2lat_map(self) -> Dict[str, str]:
        """

        :return characters map of georgian to latin
        """

        return {ka: lat for ka, lat in zip(self.ka_script, self.latin_script)}

    @property
    @lru_cache
    def lat2ka_map(self) -> Dict[str, str]:
        """

        :return georgian characters map of latin to georgian
        """

        return {lat: ka for lat, ka in zip(self.latin_script, self.ka_script)}

    def lat2ka(self, value: str, na_value: str = None) -> str:
        """
        convert the given string from latin into georgian chars

        :param value: Georgian or Latin text
        :param na_value: N/A value if could not find character, default None.

        :return

        >>> # example
        >>> self.lat2ka('laSas uyvars ana da piToni lol ))')
        "ლაSას უyვარს ანა და ფიTონი ლოლ ))"
        """

        chars = list()
        i = 0
        while i < len(value):
            char = value[i]
            try:
                chars.append(self.lat2ka_map[char])
            except KeyError:
                if na_value:
                    chars.append(na_value)
                else:
                    chars.append(char)
            i += 1

        return ''.join(chars)

    def ka2lat(self, value: str, na_value: str = None) -> str:
        """
        convert the given name from georgian into latin chars

        :param value: Georgian or Latin text
        :param na_value: N/A value if could not find character, default None.

        :return

        >>> # example
        >>> self.ka2lat('მე მიყვარს ანა!')
        "me miqvars ana!"
        """

        chars = list()
        i = 0
        while i < len(value):
            char = value[i]
            try:
                chars.append(self.ka2lat_map[char])
            except KeyError:
                if na_value:
                    chars.append(na_value)
                else:
                    chars.append(char)
            i += 1

        return ''.join(chars)

    def _replace_str(self, ka2latin: bool, match: re.Match) -> str:
        """
        replace strings
        """

        char = match.group()

        if ka2latin and char in self.ka2lat_map:
            return self.ka2lat_map[char]

        return char

    @staticmethod
    def _slugify(value: Any) -> str:
        """
        Converts to ASCII. Converts spaces to hyphens.
        Removes characters that
        aren't alphanumerics, underscores, or hyphens.
        Also strips leading and trailing whitespace.

        """

        if isinstance(value, bytes):
            s = str(value, 'utf-8', 'strict')
        else:
            s = str(value)
        s = normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
        return re.sub(r'[-\s]+', '-', re.sub(r'[^\w\s-]', '', s).strip())

    def encode_slugify(self, value: str, ka2latin: bool = False) -> str:
        """

        Convert Georgian letters to latin if 'ka2latin' is True.
        Convert spaces to hyphens.
        Remove characters that aren't alphanumerics, underscores, or hyphens.
        Convert to lowercase. Also strip leading and trailing whitespace.

        :param value: Georgian or Latin text
        :param ka2latin: if True, value with Georgian letters will be converted
                        to Latin letters, default False.
        :return:

        >>> encode_slugify("მე\'მიყვარს-ანი და ის/ჩემი ცხოვბრებაა! ჩ", True)
        "memiqvars-ani-da-ischemi-tskhovbrebaa-ch"
        >>> encode_slugify("პითონი და ჯანგო")
        >>> encode_slugify("adé\jcà lr\\rr'huété")  # could not find unicode
        "adé\jcà lr\\rr'huété"
        >>> encode_slugify("更新时间")  # could not find unicode
        "更新时间"

        """

        if isinstance(value, bytes):
            value = str(value, 'utf-8', 'strict')
        else:
            value = str(value)

        replace_str = partial(self._replace_str, ka2latin)
        s = re.sub(r'[^a-zA-Z0-9\\s\\-]{1}', replace_str, value)

        return re.sub(r'[-\s]+', '-', re.sub(r'[^\w\s-]', '', s).strip().lower())

    def encode_text(
            self,
            value: str,
            ka2latin: bool = True,
            latin2ka: bool = False,
            na_value: str = None) -> str:
        """

        :param value: Georgian or Latin text
        :param ka2latin: if True, value with Georgian letters will be converted
                        to Latin letters, default True.
        :param latin2ka: if True, value with Latin letters will be converted
                        to Georgian letters, default False.
        :param na_value: N/A value if could not find character, default None.
        :return: georgian or latin letters
        """

        if not ka2latin and not latin2ka:
            raise ValueError(
                'Missing required argument, '
                'Choose one `ka2latin` or `latin2ka`'
            )

        if isinstance(value, bytes):
            value = str(value, 'utf-8', 'strict')
        else:
            value = str(value)

        if latin2ka:
            return self.lat2ka(value, na_value)

        return self.ka2lat(value, na_value)


instance: GeoLangToolKit = GeoLangToolKit()
encode_slugify = instance.encode_slugify
encode_text = instance.encode_text
