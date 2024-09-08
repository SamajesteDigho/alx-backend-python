import sys
import unittest


class MyLib:
    __version__ = (1, 3)

mylib = MyLib()

def external_resource_available():
    return False

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase('test_nothing'))
    suite.addTest(MyTestCase('test_format'))
    suite.addTest(MyTestCase('test_windows_support'))
    suite.addTest(MyTestCase('external_resource_available'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())