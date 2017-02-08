import unittest
import FileSize
from decimal import (Decimal, ROUND_DOWN)
class TestFileSize1000_3(unittest.TestCase):
    def test_999(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = 999
        self.assertEqual(self.__target.Get(actual), "999 B")
    def test_1000(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = 1000
        self.assertEqual(self.__target.Get(actual), "1 KB")
    def test_1023(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = 1023
        self.assertEqual(self.__target.Get(actual), "1.02 KB")
    def test_1024(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = 1024
        self.assertEqual(self.__target.Get(actual), "1.02 KB")

    def test_1000KB_1(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = 1000 * 1000 - 1
        self.assertEqual(self.__target.Get(actual), "999.99 KB")
    def test_1MB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = 1000 * 1000
        self.assertEqual(self.__target.Get(actual), "1 MB")

    def test_1000MB_1(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = ((1000 ** 2) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 MB")
    def test_1GB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = ((1000 ** 2) * 1000)
        self.assertEqual(self.__target.Get(actual), "1 GB")

    def test_1000GB_1(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = ((1000 ** 3) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 GB")
    def test_1TB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = ((1000 ** 3) * 1000)
        self.assertEqual(self.__target.Get(actual), "1 TB")

    def test_1000TB_1(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = ((1000 ** 4) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 TB")
    def test_1PB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = ((1000 ** 4) * 1000)
        self.assertEqual(self.__target.Get(actual), "1 PB")

    def test_1000PB_1(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = Decimal((1000 ** 5) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 PB")
    def test_1EB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = Decimal((1000 ** 5) * 1000)
        self.assertEqual(self.__target.Get(actual), "1 EB")

    def test_1000EB_1(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = Decimal((1000 ** 6) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 EB")
    def test_1ZB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = Decimal((1000 ** 6) * 1000)
        self.assertEqual(self.__target.Get(actual), "1 ZB")

    def test_1000ZB_1(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = Decimal((1000 ** 7) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 ZB")
    def test_1YB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = Decimal((1000 ** 7) * 1000)
        self.assertEqual(self.__target.Get(actual), "1 YB")

    def test_1000YB_1(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = Decimal((1000 ** 8) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 YB")
    def test_1YB(self):
        self.__target = FileSize.FileSize(byte_size_of_unit=1000, integral_figure_num=3)
        actual = Decimal((1000 ** 7) * 1000)
        self.assertEqual(self.__target.Get(actual), "1 YB")

