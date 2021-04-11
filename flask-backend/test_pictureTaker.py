import unittest

class TestServer(unittest.TestCase):

    def test_tests(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_takePicture(self):
        

if __name__ == '__main__':
    unittest.main()