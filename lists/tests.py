from django.test import TestCase

class SokeTest(TestCase):

    def test_bad_match(self):
        self.assertEqual(1+1,3)
        
