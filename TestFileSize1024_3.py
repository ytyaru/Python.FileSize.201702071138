import unittest
import FileSize
from decimal import (Decimal, ROUND_DOWN)
class TestFileSize1024_4(unittest.TestCase):
    def test_999(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = 999
        self.assertEqual(self.__target.Get(actual), "999 iB")
    def test_1000(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = 1000
        self.assertEqual(self.__target.Get(actual), "0.97 KiB")
    def test_1023(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = 1023
        self.assertEqual(self.__target.Get(actual), "0.99 KiB")
    def test_1024(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = 1024
        self.assertEqual(self.__target.Get(actual), "1 KiB")

    def test_1000KiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = (1024 * 1000) - 1
        # 1000 KiB未満
        self.assertEqual(self.__target.Get(actual), "999.99 KiB")
    def test_1MiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = (1024 ** 2) - 1
        # 1024 KiB未満
        self.assertEqual(self.__target.Get(actual), "0.99 MiB")
    def test_1MiB(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = (1024 ** 2)
        self.assertEqual(self.__target.Get(actual), "1 MiB")

    def test_1000MiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = ((1024 ** 2) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 MiB")
    def test_1GiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = (1024 ** 3) - 1
        self.assertEqual(self.__target.Get(actual), "0.99 GiB")
    def test_1GiB(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = (1024 ** 3)
        self.assertEqual(self.__target.Get(actual), "1 GiB")

    def test_1000GiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = ((1024 ** 3) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 GiB")
    def test_1TiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = (1024 ** 4) - 1
        self.assertEqual(self.__target.Get(actual), "0.99 TiB")
    def test_1TiB(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = (1024 ** 4)
        self.assertEqual(self.__target.Get(actual), "1 TiB")

    def test_1000TiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = ((1024 ** 4) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 TiB")
    def test_1PiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = (1024 ** 5) - 1
        self.assertEqual(self.__target.Get(actual), "0.99 PiB")
    def test_1PiB(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = (1024 ** 5)
        self.assertEqual(self.__target.Get(actual), "1 PiB")

    def test_1000PiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = Decimal((1024 ** 5) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 PiB")
    def test_1EiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = Decimal(1024 ** 6) - 1
        self.assertEqual(self.__target.Get(actual), "0.99 EiB")
    def test_1EiB(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = Decimal(1024 ** 6)
        self.assertEqual(self.__target.Get(actual), "1 EiB")

    def test_1000EiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = Decimal((1024 ** 6) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 EiB")
    def test_1ZiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = Decimal(1024 ** 7) - 1
        self.assertEqual(self.__target.Get(actual), "0.99 ZiB")
    def test_1ZiB(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = Decimal(1024 ** 7)
        self.assertEqual(self.__target.Get(actual), "1 ZiB")

    def test_1000ZiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = Decimal((1024 ** 7) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 ZiB")
    def test_1YiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = Decimal(1024 ** 8) - 1
        self.assertEqual(self.__target.Get(actual), "0.99 YiB")
    def test_1YiB(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = Decimal(1024 ** 8)
        self.assertEqual(self.__target.Get(actual), "1 YiB")

    def test_1000YiB_1(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = Decimal((1024 ** 8) * 1000) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 YiB")
    def test_1000YiB(self):
        self.__target = FileSize.FileSize(integral_figure_num=3)
        actual = Decimal(1024 ** 8) * 1000
#        self.assertEqual(self.__target.Get(actual), "1000 YiB")
        self.assertEqual(self.__target.Get(actual), None)

