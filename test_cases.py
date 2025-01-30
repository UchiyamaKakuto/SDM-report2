#!/usr/bin/python3

import unittest
from calc_mul import calc
1000
# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        #a,b整数
        def test_sample01 (self):
                self.assertEqual (21, calc(3,7))
        #a0,b整数
        def test_sample02 (self):
                self.assertEqual (-1, calc(0,150))
        #a,b文字
        def test_sample03 (self):
                self.assertEqual (-1, calc('a','b'))
        #a整数以外,b整数
        def test_sample04 (self):
                self.assertEqual (-1, calc(0.1,999))

        #以下追加
        #a文字,b整数
        def test_sample05 (self):
                self.assertEqual (-1, calc('a',150))
        #a整数,b整数以外
        def test_sample06 (self):
                self.assertEqual (-1, calc(999,0.1))
        #a,b整数以外
        def test_sample07 (self):
                self.assertEqual (-1, calc(0.1,0.1))
        #a文字,b正数以外
        def test_sample08 (self):
                self.assertEqual (-1, calc('a',0.1))
        #a正数,b文字
        def test_sample09 (self):
                self.assertEqual (-1, calc(150,'b'))
        #a正数以外,b文字
        def test_sample10 (self):
                self.assertEqual (-1, calc(0.1,'b'))
        #a1,b正数
        def test_sample11 (self):
                self.assertEqual (150, calc(1,150))
        #a999,b正数
        def test_sample12 (self):
                self.assertEqual (1998, calc(999,2)) 
        #a1000,b正数
        def test_sample13 (self):
                self.assertEqual (-1, calc(1000,2)) 
        #a正数,b0
        def test_sample14 (self):
                self.assertEqual (-1, calc(150,0)) 
        #a正数,b1
        def test_sample15 (self):
                self.assertEqual (150, calc(150,1)) 
        #a正数,b999
        def test_sample16 (self):
                self.assertEqual (1998, calc(2,999)) 
        #a正数,b999
        def test_sample17 (self):
                self.assertEqual (-1, calc(2,1000)) 
                

