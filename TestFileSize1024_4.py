import unittest
import FileSize
from decimal import (Decimal, ROUND_DOWN)
class TestFileSize1024_4(unittest.TestCase):
    def test_9999(self):
        self.__target = FileSize.FileSize()
        actual = 9999
        self.assertEqual(self.__target.Get(actual), "9999 iB")
    def test_10000(self):
        self.__target = FileSize.FileSize()
        actual = 10000
        self.assertEqual(self.__target.Get(actual), "9.76 KiB")
    def test_10239(self):
        self.__target = FileSize.FileSize()
        actual = (1024 * 10) - 1
        self.assertEqual(self.__target.Get(actual), "9.99 KiB")        
    def test_10240(self):
        self.__target = FileSize.FileSize()
        actual = 1024 * 10
        self.assertEqual(self.__target.Get(actual), "10 KiB")
    def test_102399(self):
        self.__target = FileSize.FileSize()
        actual = (1024 * 100) - 1
        self.assertEqual(self.__target.Get(actual), "99.99 KiB")        
    def test_102400(self):
        self.__target = FileSize.FileSize()
        actual = 1024 * 100
        self.assertEqual(self.__target.Get(actual), "100 KiB")

    def test_1023999(self):
        self.__target = FileSize.FileSize()
        actual = (1024 * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 KiB")
    def test_1024000(self):
        self.__target = FileSize.FileSize()
        actual = 1024 * 1000
        self.assertEqual(self.__target.Get(actual), "1000 KiB")

    def test_10239999(self):
        self.__target = FileSize.FileSize()
        actual = (1024 * 10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 KiB")
    def test_10240000(self):
        self.__target = FileSize.FileSize()
        actual = 1024 * 10000
        self.assertEqual(self.__target.Get(actual), "9.76 MiB")
    def test_10485759(self):
        self.__target = FileSize.FileSize()
        actual = (1024*1024*10) - 1
        self.assertEqual(self.__target.Get(actual), "9.99 MiB")
    def test_10485760(self):
        self.__target = FileSize.FileSize()
        actual = 1024*1024*10
        self.assertEqual(self.__target.Get(actual), "10 MiB")

    def test_10485759999(self):
        self.__target = FileSize.FileSize()
        actual = (1024*1024*10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 MiB")
    def test_10485760000(self):
        self.__target = FileSize.FileSize()
        actual = 1024*1024*10000
        self.assertEqual(self.__target.Get(actual), "9.76 GiB")
    def test_10485759999(self):
        self.__target = FileSize.FileSize()
        actual = (1024*1024*1024*10) - 1
        self.assertEqual(self.__target.Get(actual), "9.99 GiB")
    def test_10485760000(self):
        self.__target = FileSize.FileSize()
        actual = (1024*1024*1024*10)
        self.assertEqual(self.__target.Get(actual), "10 GiB")

    def test_9999GiB(self):
        self.__target = FileSize.FileSize()
        actual = (1024*1024*1024*10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 GiB")
    def test_976TiB(self):
        self.__target = FileSize.FileSize()
        actual = (1024*1024*1024*10000)
        self.assertEqual(self.__target.Get(actual), "9.76 TiB")
    def test_999TiB(self):
        self.__target = FileSize.FileSize()
        actual = (1024*1024*1024*1024*10) - 1
        self.assertEqual(self.__target.Get(actual), "9.99 TiB")
    def test_10TiB(self):
        self.__target = FileSize.FileSize()
        actual = (1024*1024*1024*1024*10)
        self.assertEqual(self.__target.Get(actual), "10 TiB")

    def test_9999TiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 TiB")
    def test_976PiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*10000)
        self.assertEqual(self.__target.Get(actual), "9.76 PiB")
    def test_999TiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*10) - 1
        self.assertEqual(self.__target.Get(actual), "9.99 PiB")
    def test_10PiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*10)
        self.assertEqual(self.__target.Get(actual), "10 PiB")

    def test_9999PiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 PiB")
    def test_976EiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*10000)
        self.assertEqual(self.__target.Get(actual), "9.76 EiB")
    def test_999EiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*1024*10) - 1
        self.assertEqual(self.__target.Get(actual), "9.99 EiB")
    def test_10EiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*1024*10)
        self.assertEqual(self.__target.Get(actual), "10 EiB")

    def test_9999EiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*1024*10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 EiB")
    def test_976ZiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*1024*10000)
        self.assertEqual(self.__target.Get(actual), "9.76 ZiB")
    def test_999ZiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*1024*1024*10) - 1
        self.assertEqual(self.__target.Get(actual), "9.99 ZiB")
    def test_10ZiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*1024*1024*10)
        self.assertEqual(self.__target.Get(actual), "10 ZiB")

    def test_9999ZiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*1024*1024*10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 ZiB")
    def test_976YiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*1024*1024*10000)
        self.assertEqual(self.__target.Get(actual), "9.76 YiB")
    def test_999YiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*1024*1024*1024*10) - 1
        self.assertEqual(self.__target.Get(actual), "9.99 YiB")
    def test_10YiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*1024*1024*1024*10)
        self.assertEqual(self.__target.Get(actual), "10 YiB")

    """
    # decimal.InvalidOperation: quotient too large in //, % or divmod
    def test_9999YiB(self):
        self.__target = FileSize.FileSize()
        actual = Decimal(1024*1024*1024*1024*1024*1024*1024*1024*10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 YiB")
    """

