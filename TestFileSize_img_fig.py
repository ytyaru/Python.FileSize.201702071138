import unittest
import FileSize
from decimal import (Decimal, ROUND_DOWN)
class TestFileSize_img_fig(unittest.TestCase):

    def test_9999_999KiB_4_3(self):
        unit=1024; int_fig=4; img_fig=3;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig)
        actual = ((unit ** 1) * (10 ** int_fig)) - 1
        self.assertEqual(self.__target.Get(actual), "9999.999 KiB")
    def test_9999_99KiB_4_2(self):
        unit=1024; int_fig=4; img_fig=2;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig)
        actual = ((unit ** 1) * (10 ** int_fig)) - 1
        self.assertEqual(self.__target.Get(actual), "9999.99 KiB")
    def test_9999_9KiB_4_1(self):
        unit=1024; int_fig=4; img_fig=1;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig)
        actual = ((unit ** 1) * (10 ** int_fig)) - 1
        self.assertEqual(self.__target.Get(actual), "9999.9 KiB")
    def test_9999KiB_4_0(self):
        unit=1024; int_fig=4; img_fig=0;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig)
        actual = ((unit ** 1) * (10 ** int_fig)) - 1
        self.assertEqual(self.__target.Get(actual), "9999 KiB")

    def test_9999_999KiB_3_3(self):
        unit=1024; int_fig=3; img_fig=3;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig)
        actual = ((unit ** 1) * (10 ** int_fig)) - 1
        self.assertEqual(self.__target.Get(actual), "999.999 KiB")
    def test_9999_99KiB_3_2(self):
        unit=1024; int_fig=3; img_fig=2;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig)
        actual = ((unit ** 1) * (10 ** int_fig)) - 1
        self.assertEqual(self.__target.Get(actual), "999.99 KiB")
    def test_9999_9KiB_3_1(self):
        unit=1024; int_fig=3; img_fig=1;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig)
        actual = ((unit ** 1) * (10 ** int_fig)) - 1
        self.assertEqual(self.__target.Get(actual), "999.9 KiB")
    def test_9999KiB_3_0(self):
        unit=1024; int_fig=3; img_fig=0;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig)
        actual = ((unit ** 1) * (10 ** int_fig)) - 1
        self.assertEqual(self.__target.Get(actual), "999 KiB")

    def test_10_000KiB_4_3_zero(self):
        unit=1024; int_fig=4; img_fig=3; zero=False;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = ((unit ** 1) * (10))
        self.assertEqual(self.__target.Get(actual), "10.000 KiB")
    def test_10_00KiB_4_2_zero(self):
        unit=1024; int_fig=4; img_fig=2; zero=False;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = ((unit ** 1) * (10))
        self.assertEqual(self.__target.Get(actual), "10.00 KiB")
    def test_10_0KiB_4_1_zero(self):
        unit=1024; int_fig=4; img_fig=1; zero=False;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = ((unit ** 1) * (10))
        self.assertEqual(self.__target.Get(actual), "10.0 KiB")
    def test_10KiB_4_0_zero(self):
        unit=1024; int_fig=4; img_fig=0; zero=False;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = ((unit ** 1) * (10))
        self.assertEqual(self.__target.Get(actual), "10 KiB")

    def test_1_000KiB_3_3_zero(self):
        unit=1024; int_fig=3; img_fig=3; zero=False;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = (unit ** 1)
        self.assertEqual(self.__target.Get(actual), "1.000 KiB")
    def test_1_00KiB_3_2_zero(self):
        unit=1024; int_fig=3; img_fig=2; zero=False;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = (unit ** 1)
        self.assertEqual(self.__target.Get(actual), "1.00 KiB")
    def test_1_0KiB_3_1_zero(self):
        unit=1024; int_fig=3; img_fig=1; zero=False;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = (unit ** 1)
        self.assertEqual(self.__target.Get(actual), "1.0 KiB")
    def test_1KiB_3_0_zero(self):
        unit=1024; int_fig=3; img_fig=0; zero=False;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = (unit ** 1)
        self.assertEqual(self.__target.Get(actual), "1 KiB")

    def test_10KiB_4_3(self):
        unit=1024; int_fig=4; img_fig=3; zero=True;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = ((unit ** 1) * (10))
        self.assertEqual(self.__target.Get(actual), "10 KiB")
    def test_10KiB_4_2(self):
        unit=1024; int_fig=4; img_fig=2; zero=True;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = ((unit ** 1) * (10))
        self.assertEqual(self.__target.Get(actual), "10 KiB")
    def test_10KiB_4_1(self):
        unit=1024; int_fig=4; img_fig=1; zero=True;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = ((unit ** 1) * (10))
        self.assertEqual(self.__target.Get(actual), "10 KiB")
    def test_10KiB_4_0(self):
        unit=1024; int_fig=4; img_fig=0; zero=True;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = ((unit ** 1) * (10))
        self.assertEqual(self.__target.Get(actual), "10 KiB")

    def test_1KiB_3_3(self):
        unit=1024; int_fig=3; img_fig=3; zero=True;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = (unit ** 1)
        self.assertEqual(self.__target.Get(actual), "1 KiB")
    def test_1KiB_3_2(self):
        unit=1024; int_fig=3; img_fig=2; zero=True;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = (unit ** 1)
        self.assertEqual(self.__target.Get(actual), "1 KiB")
    def test_1KiB_3_1(self):
        unit=1024; int_fig=3; img_fig=1; zero=True;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = (unit ** 1)
        self.assertEqual(self.__target.Get(actual), "1 KiB")
    def test_1KiB_3_0(self):
        unit=1024; int_fig=3; img_fig=0; zero=True;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit, integral_figure_num=int_fig, imaginary_figure_num=img_fig, is_hidden_imaginary_all_zero=zero)
        actual = (unit ** 1)
        self.assertEqual(self.__target.Get(actual), "1 KiB")

