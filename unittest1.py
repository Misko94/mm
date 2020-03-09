# testiranje "main" koda u "unittest1"
import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        test_parm = 10
        result = main.do_stuff(test_parm)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_parm = 'misko'
        result = main.do_stuff(test_parm)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_parm = None
        result = main.do_stuff(test_parm)
        self.assertEqual(result, 'plese enter number')

    def test_do_stuff4(self):
        test_parm = ''
        result = main.do_stuff(test_parm)
        self.assertEqual(result, 'plese enter number')

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()
