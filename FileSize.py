#!python3
#encoding:utf-8
import math
import decimal
from decimal import (Decimal, ROUND_DOWN)
class FileSize:
    """
    コンストラクタ。
    @param {integer}          byte_size_of_unitはK,M,Gなどの単位を1000か1024かのいずれかで指定する。
    @param {integer}          integral_figure_numは桁上がりするまでの整数部の桁数を指定する。3か4のいずれか。
    @param {integer}          imaginary_figure_numは虚数部の桁数を指定する。0,1,2,3のいずれか。
    @param {decimal.rounding} roundingは算出時の丸め方式である。decimalの丸め方式を指定する。
    @param {boolean}          is_hidden_imaginary_all_zeroは虚数部がすべてゼロの場合に非表示にするか否かを指定する。
    """
    def __init__(self, 
                 byte_size_of_unit=1024, 
                 integral_figure_num=4, 
                 imaginary_figure_num=2, 
                 rounding=decimal.ROUND_DOWN, 
                 is_hidden_imaginary_all_zero=True):
        # 単位あたりのByte数
        self.SetByteOfUnitSize(byte_size_of_unit)
        # 桁上がりするまでの桁数
        self.SetCarryFigureNum(integral_figure_num)
        # 丸め方式
        self.__rounding = rounding
        # 虚数部の表示桁数
        self.__img_figs = ['1.', '.1', '.01', '.001']
        self.SetImaginaryFigureNum(imaginary_figure_num)
        # 虚数部がすべてゼロなら非表示にする
        self.is_hidden_imaginary_all_zero = is_hidden_imaginary_all_zero

    """
    単位あたりのByteサイズを設定する。
    @param {integer} unit_size 1000または1024のいずれかのみ。
    """
    def SetByteOfUnitSize(self, unit_size):
        if 1000 == unit_size or 1024 == unit_size:
            self.__byte_size_of_unit = unit_size
        else:
            raise Exception('単位あたりのByte数は1000または1024のみ有効です。無効値: ' + str(unit_size))

    """
    単位名を取得する。
    """
    def GetByteOfUnitName(self):
        if 1000 == self.__byte_size_of_unit:
            return "B"
        elif 1024 == self.__byte_size_of_unit:
            return "iB"
        else:
            raise Exception('単位あたりのByte数は1000または1024のみ有効です。無効値: ' + str(self.__byte_size_of_unit))

    """
    単位名を取得する。
    """
    def GetByteOfUnitFullName(self):
        if 1000 == self.__byte_size_of_unit:
            return "Byte"
        elif 1024 == self.__byte_size_of_unit:
            return "iByte"
        else:
            raise Exception('単位あたりのByte数は1000または1024のみ有効です。無効値: ' + str(self.__byte_size_of_unit))

    """
    規格名を取得する。(英語)
    """
    def GetByteOfUnitStandardName_English(self):
        if 1000 == self.__byte_size_of_unit:
            return "SI"
        elif 1024 == self.__byte_size_of_unit:
            return "BinaryPrefix"
        else:
            raise Exception('単位あたりのByte数は1000または1024のみ有効です。無効値: ' + str(self.__byte_size_of_unit))
    """
    規格名を取得する。(日本語)
    """
    def GetByteOfUnitStandardName_Japanese(self):
        if 1000 == self.__byte_size_of_unit:
            return "国際単位系"
        elif 1024 == self.__byte_size_of_unit:
            return "2進接頭辞"
        else:
            raise Exception('単位あたりのByte数は1000または1024のみ有効です。無効値: ' + str(self.__byte_size_of_unit))

    """
    各単位の説明URLを返す。
    """
    def GetByteOfUnitDescription(self):
        if 1000 == self.__byte_size_of_unit:
            return "https://ja.wikipedia.org/wiki/%E5%9B%BD%E9%9A%9B%E5%8D%98%E4%BD%8D%E7%B3%BB"
        elif 1024 == self.__byte_size_of_unit:
            return "https://ja.wikipedia.org/wiki/2%E9%80%B2%E6%8E%A5%E9%A0%AD%E8%BE%9E"
        else:
            raise Exception('単位あたりのByte数は1000または1024のみ有効です。無効値: ' + str(self.__byte_size_of_unit))

    """
    整数部の表示桁数を指定する。
    @param {integer} integral_figure_num。3か4のみ。
    """
    def SetCarryFigureNum(self, integral_figure_num):
        if 3 == integral_figure_num or 4 == integral_figure_num:
            self.__integral_figure_num = integral_figure_num
        else:
            raise Exception('桁上がりするまでの桁数は3または4のみ有効です。無効値: ' + str(integral_figure_num))

    """
    虚数部の表示桁数を指定する。
    @param {integer} img_fig。0,1,2,3のいずれか。
    """
    def SetImaginaryFigureNum(self, img_fig):
        if 0 <= img_fig and img_fig < len(self.__img_figs):
            self.__img_fig = img_fig
        else:
            raise Exception('虚数部の桁数は0〜{0}までの整数値のみ有効です。無効値: {1}'.format(len(self.__img_figs) - 1, img_fig))

    """
    ファイルサイズを取得する。
    @param  {bytesize} Byte値
    @return {string}   ファイルサイズ表現文字列
    """
    def Get(self, bytesize):
        exponent = 0
        byte_unit_name = self.GetByteOfUnitName()
        for size_unit_name in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']:
            base_size = self.__byte_size_of_unit ** exponent
            if self.__integral_figure_num < len(str(bytesize // base_size)):
                exponent = exponent + 1
                continue
            return "{0} {1}{2}".format(self.__GetValue(bytesize, base_size), size_unit_name, byte_unit_name)

    """
    ファイルサイズ値の文字列を取得する。
    設定に応じた形式で。
    @param  {decimal} bytesize は算出したいファイルサイズのByte数である。
    @param  {decimal} base_size はbytesizeを割る数である。
    @return {string}  ファイルサイズ値の文字列
    """
    def __GetValue(self, bytesize, base_size):
        value = str(Decimal((bytesize / base_size)).quantize(Decimal(self.__img_figs[self.__img_fig]), rounding=self.__rounding))
        if 0 == self.__img_fig:
            return value
        else:
            if self.is_hidden_imaginary_all_zero:
                zero = "." + ("0" * self.__img_fig)
                return value.replace(zero, "")
            else:
                return value

