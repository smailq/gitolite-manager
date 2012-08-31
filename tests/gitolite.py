import unittest

import gitolite_manager


class ConfigFileTestCase(unittest.TestCase):
    def setUp(self):
        self.gitolite = gitolite_manager.Gitolite()

    def tearDown(self):
        pass

    def test_add_repo(self):
        self.assertEqual('','')

    def test_rm_repo(self):
        self.assertEqual('','')

    def test_get_repo(self):
        self.assertEqual('','')


class SSHKeyTestCase(unittest.TestCase):
    def setUp(self):
        self.gitolite = gitolite_manager.Gitolite()

    def tearDown(self):
        pass

    def test_add_key(self):
        self.assertEqual('','')

    def test_rm_key(self):
        self.assertEqual('','')

    def test_get_keys(self):
        self.assertEqual('','')
