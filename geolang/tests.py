import unittest

from geolang import encode_slugify, encode_text


class GeoLangToolkitTests(unittest.TestCase):

    def test_encode_slugify(self):
        res = encode_slugify('პი ად აწდ აწდა წდ აწდ აწდაწ')
        self.assertEqual(res, 'პი-ად-აწდ-აწდა-წდ-აწდ-აწდაწ')
        res = encode_slugify('pi ად აწდ აწდა წდ აწდ აწდაწ afawf a fawf a')
        self.assertEqual(res, 'pi-ად-აწდ-აწდა-წდ-აწდ-აწდაწ-afawf-a-fawf-a')
        res = encode_slugify('ლაშა და ანა', True)
        self.assertEqual(res, 'lasha-da-ana')
        res = encode_slugify('ლაშა და ანა a b c', True)
        self.assertEqual(res, 'lasha-da-ana-a-b-c')
        res = encode_slugify("მე\'მიყვარს-ანი და ის/ჩემი ცხოვბრებაა! ჩ", True)
        self.assertEqual(res, 'memiqvars-ani-da-ischemi-tskhovbrebaa-ch')
        res = encode_slugify("更新时间")
        self.assertEqual(res, '更新时间')
        res = encode_slugify("adé\jcà lr\\rr'huété")
        self.assertEqual(res, 'adéjcà-lrrrhuété')
        res = encode_slugify("პითონი და ჯანგო")
        self.assertEqual(res, 'პითონი-და-ჯანგო')
        res = encode_slugify(
            "    ABC some programming languages are fucking   "
        )
        self.assertEqual(res, 'abc-some-programming-languages-are-fucking')

    def test_encode_text(self):
        res = encode_text('ლაშა დაჩი მაიმუნია და რა უნდა ნეტა?!')
        self.assertEqual(res, 'lasha dachi maimunia da ra unda neta?!')
        res = encode_text('laSas uyvars ana da piToni lol ))')
        self.assertEqual(res, 'laSas uyvars ana da piToni lol ))')
        res = encode_text('laSas uyvars ana da piToni lol ))', latin2ka=True)
        self.assertEqual(res, 'ლაSას უyვარს ანა და ფიTონი ლოლ ))')
        res = encode_text(
            'laSas uyvars ana da piToni lol ))', latin2ka=True, na_value='-'
        )
        self.assertEqual(res, 'ლა-ას-უ-ვარს-ანა-და-ფი-ონი-ლოლ---')


if __name__ == '__main__':
    unittest.main()
