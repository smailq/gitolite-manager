import unittest

from tests.gitolite import ConfigFileTestCase
from tests.gitolite import SSHKeyTestCase

def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ConfigFileTestCase))
    suite.addTest(unittest.makeSuite(SSHKeyTestCase))
    return suite
