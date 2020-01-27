from django.test import TestCase


class SimpleTests(TestCase):

    def test_first_test(self):
        self.assertIs(False, False)

    