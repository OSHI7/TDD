import unittest

class SomeTests(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_CanDo99(self):
        print("test99")

    def test_CanDo1(self):
        print("test1")

    def test_CanDo2(self):
        print("test2")
        self.assertIn('in', 'in')

if __name__=="__main__":
    print('name == main')
    unittest.main()
    print("Done")
else:
    print('name !=main')

# exec(open('test_some_unittest_Stuff.py').read())