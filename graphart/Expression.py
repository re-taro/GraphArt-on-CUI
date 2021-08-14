# -*- coding: utf-8 -*-
import sys

from numpy import character


class ExpressionTemplate:
    def __init__(self):
        self.xmin = -100
        self.xmax = 100
        self.divisionNumber = 1000000
        self.expFormula = '000'

    def expRule(self, xmin, xmax, divisionNumber, expFormula):
        if xmin == '000':
            pass
        else:
            self.xmin = xmin
        if xmax == '000':
            pass
        else:
            self.xmax = xmax
        if divisionNumber == '000':
            pass
        else:
            self.divisionNumber = divisionNumber
        if expFormula == '000':
            print('式の形を入力してください。')
            print('プログラムが正常に動作しないため動作を停止します。')
            sys.exit()
        else:
            self.expFormula = expFormula

    def echoXmin(self):
        return int(self.xmin)

    def echoXmax(self):
        return int(self.xmax)

    def echodnum(self):
        return int(self.divisionNumber)

    def echoFormula(self):
        return self.expFormula