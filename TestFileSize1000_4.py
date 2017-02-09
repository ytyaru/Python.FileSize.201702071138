import unittest
import FileSize
from decimal import Decimal
class TestFileSize1000_4(unittest.TestCase):
    def test_999(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = 999
        self.assertEqual(self.__target.Get(actual), "999 B")
    def test_1000(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = 1000
        self.assertEqual(self.__target.Get(actual), "1000 B")
    def test_1023(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = 1023
        self.assertEqual(self.__target.Get(actual), "1023 B")
    def test_1024(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = 1024
        self.assertEqual(self.__target.Get(actual), "1024 B")
    def test_9999(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = 9999
        self.assertEqual(self.__target.Get(actual), "9999 B")
    def test_10000(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = 10000
        self.assertEqual(self.__target.Get(actual), "10 KB")

    def test_9999KB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = (1000 ** 2 * 10) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 KB")
    def test_10MB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = (1000 ** 2) * 10
        self.assertEqual(self.__target.Get(actual), "10 MB")
    def test_9999MB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = ((1000 ** 2) * 10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 MB")
    def test_10GB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = ((1000 ** 2) * 10000)
        self.assertEqual(self.__target.Get(actual), "10 GB")
    def test_9999GB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = ((1000 ** 3) * 10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 GB")
    def test_10TB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = ((1000 ** 3) * 10000)
        self.assertEqual(self.__target.Get(actual), "10 TB")
    def test_9999TB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = ((1000 ** 4) * 10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 TB")
    def test_10PB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = ((1000 ** 4) * 10000)
        self.assertEqual(self.__target.Get(actual), "10 PB")
    def test_9999PB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = (Decimal(1000 ** 5) * 10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 PB")
    def test_10EB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = (Decimal(1000 ** 5) * 10000)
        self.assertEqual(self.__target.Get(actual), "10 EB")
    def test_9999EB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = (Decimal(1000 ** 6) * 10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 EB")
    def test_10ZB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = (Decimal(1000 ** 6) * 10000)
        self.assertEqual(self.__target.Get(actual), "10 ZB")
    def test_9999ZB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = (Decimal(1000 ** 7) * 10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 ZB")
    def test_10YB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = (Decimal(1000 ** 7) * 10000)
        self.assertEqual(self.__target.Get(actual), "10 YB")
    def test_9999YB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=4)
        actual = (Decimal(1000 ** 8) * 10000) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 YB")

