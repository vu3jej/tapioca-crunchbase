# coding: utf-8

import unittest

from tapioca_crunchbase import Crunchbase


class TestTapiocaCrunchbase(unittest.TestCase):

    def setUp(self):
        self.wrapper = Crunchbase()


if __name__ == '__main__':
    unittest.main()
