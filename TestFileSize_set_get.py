import unittest
import FileSize
from decimal import (Decimal, ROUND_DOWN)
class TestFileSize_set_get(unittest.TestCase):

    def test_set_unit_999(self):
        with self.assertRaises(Exception) as e:
            unit=999;
            self.__target = FileSize.FileSize(byte_size_of_unit=unit)
            self.assertEqual('単位あたりのByte数は1000または1024のみ有効です。無効値: {0}'.format(unit), e.exception.args[0])
    def test_set_unit_1001(self):
        with self.assertRaises(Exception) as e:
            unit=1001;
            self.__target = FileSize.FileSize(byte_size_of_unit=unit)
            self.assertEqual('単位あたりのByte数は1000または1024のみ有効です。無効値: {0}'.format(unit), e.exception.args[0])
    def test_set_unit_1023(self):
        with self.assertRaises(Exception) as e:
            unit=1023;
            self.__target = FileSize.FileSize(byte_size_of_unit=unit)
            self.assertEqual('単位あたりのByte数は1000または1024のみ有効です。無効値: {0}'.format(unit), e.exception.args[0])
    def test_set_unit_1025(self):
        with self.assertRaises(Exception) as e:
            unit=1025;
            self.__target = FileSize.FileSize(byte_size_of_unit=unit)
            self.assertEqual('単位あたりのByte数は1000または1024のみ有効です。無効値: {0}'.format(unit), e.exception.args[0])

    def test_get_unit_name_B(self):
        unit=1000;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit)
        self.assertEqual(self.__target.GetByteOfUnitName(), "B")
    def test_get_unit_name_iB(self):
        unit=1024;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit)
        self.assertEqual(self.__target.GetByteOfUnitName(), "iB")

    def test_get_unit_full_name_Byte(self):
        unit=1000;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit)
        self.assertEqual(self.__target.GetByteOfUnitFullName(), "Byte")
    def test_get_unit_full_name_iByte(self):
        unit=1024;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit)
        self.assertEqual(self.__target.GetByteOfUnitFullName(), "iByte")

    def test_get_standard_name_english_1000(self):
        unit=1000;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit)
        self.assertEqual(self.__target.GetByteOfUnitStandardName_English(), "SI")
    def test_get_standard_name_english_1024(self):
        unit=1024;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit)
        self.assertEqual(self.__target.GetByteOfUnitStandardName_English(), "BinaryPrefix")
    def test_get_standard_name_japanese_1000(self):
        unit=1000;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit)
        self.assertEqual(self.__target.GetByteOfUnitStandardName_Japanese(), "国際単位系")
    def test_get_standard_name_japanese_1024(self):
        unit=1024;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit)
        self.assertEqual(self.__target.GetByteOfUnitStandardName_Japanese(), "2進接頭辞")

    def test_get_unit_description_1000(self):
        unit=1000;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit)
        self.assertEqual(self.__target.GetByteOfUnitDescription(), "https://ja.wikipedia.org/wiki/%E5%9B%BD%E9%9A%9B%E5%8D%98%E4%BD%8D%E7%B3%BB")
    def test_get_unit_description_1024(self):
        unit=1024;
        self.__target = FileSize.FileSize(byte_size_of_unit=unit)
        self.assertEqual(self.__target.GetByteOfUnitDescription(), "https://ja.wikipedia.org/wiki/2%E9%80%B2%E6%8E%A5%E9%A0%AD%E8%BE%9E")

