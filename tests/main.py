#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest

def discover_tests():
    loader = unittest.loader.TestLoader()
    this_dir = os.path.dirname(__file__)
    return loader.discover(start_dir=this_dir, pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(discover_tests())
