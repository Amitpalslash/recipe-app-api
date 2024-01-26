from django.test import SimpleTestCase

from app import calc

class Calctest ( SimpleTestCase):

    def test_add_numbers(self):

        res = calc.add(5,6)

        self.assertEqual(res ,12)

    def test_subtract_number(self):
        res = calc.subtract( 20,10)

        self.assertEquals(res,10)
        
            
