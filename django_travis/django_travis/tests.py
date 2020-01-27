from django.test import TestCase


class SimpleTests(TestCase):

    def test_first_test(self):
        self.assertIs(False, False)

    def test_second_test(self):
        print('On second test')
        self.assertIs(False, True)