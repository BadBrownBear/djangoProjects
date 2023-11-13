from django.test import TestCase
from horoscope.views import zodiac_dict

# Create your tests here.

class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEquals(response.status_code, 200)


#    def test_libra(self):
#        response = self.client.get('/horoscope/libra')
#        self.assertEquals(response.status_code, 200)
#        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).', response.content.decode())


    def test_redirect(self):
        zodiacs = list(zodiac_dict.keys())
        for i in range(12):
            response = self.client.get(f'/horoscope/{i+1}')
            self.assertEquals(response.status_code, 302)
            self.assertEquals(response.url, f'/horoscope/{zodiacs[i]}')


    def test_signs(self):
        for key, val in zodiac_dict.items():
            response = self.client.get(f'/horoscope/{key}')
            self.assertEquals(response.status_code, 200)
            self.assertIn(val, response.content.decode())
