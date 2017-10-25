import unittest
from microurl.bitly import bitlyapi

BITLY_ACCESS_TOKEN = '948f673940a8a91636dbb980d2e6be3060920465'


class TestBitly(unittest.TestCase):

    test_url = "http://micropyramid.com/"

    def get_bitly(self):
        bitly = bitlyapi(BITLY_ACCESS_TOKEN)
        return bitly

    def test_bitly(self):
        bitly = self.get_bitly()
        self.assertTrue(bitly)

    def test_shorturl(self):
        bitly = self.get_bitly()
        domain = "j.mp"
        response = bitly.shorturl(url=self.test_url, preferred_domain=domain)
        short_url = response.get('url')
        assert short_url.startswith('http://' + domain + '/')

    def test_expand(self):
        bitly = self.get_bitly()
        response = bitly.shorturl(url=self.test_url)
        self.assertTrue(response)
        short_url = response.get('url')

        response = bitly.expand(short_url)
        expanded_url = response['expand'][0]['long_url']
        self.assertEqual(expanded_url, self.test_url)

    def test_url_info(self):
        bitly = self.get_bitly()
        short_url = bitly.url_info(url=self.test_url)
        self.assertTrue(short_url)

    def test_link_lookup(self):
        bitly = self.get_bitly()
        short_url = bitly.link_lookup(url=self.test_url)
        self.assertTrue(short_url)

    def test_link_edit(self):
        bitly = self.get_bitly()
        short_url = bitly.link_lookup(url=self.test_url)
        self.assertTrue(short_url)

    def test_user_link_lookup(self):
        bitly = self.get_bitly()
        short_url = bitly.user_link_lookup(url=self.test_url)
        self.assertTrue(short_url)

    def test_user_link_save(self):
        bitly = self.get_bitly()
        title = "micropyramid"
        note = "Pyhon devlopment"
        private = "only organization"
        ts = 'tech'
        result = bitly.user_link_save(longUrl=self.test_url,
                                      title=title,
                                      note=note,
                                      private=private,
                                      user_ts=ts)
        self.assertTrue(result)

    def test_link_info(self):
        bitly = self.get_bitly()
        result = bitly.link_info("http://kjlssjd1sd.com")
        self.assertFalse(result)
