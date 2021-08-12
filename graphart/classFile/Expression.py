# -*- coding: utf-8 -*-
import sys


class ExpressionTemplate:
    def __init__(self):
        self.xmin = -100
        self.xmax = 100
        self.ymin = -100
        self.ymax = 100
        self.divisionNumber = 1000
        self.expFormula = '--'

    def expRule(self, xmin, xmax, divisionNumber, expFormula):
        if xmin == '--':
            pass
        else:
            self.xmin = xmin
        if xmax == '--':
            pass
        else:
            self.xmax = xmax
        if divisionNumber == '--':
            pass
        else:
            self.divisionNumber = divisionNumber
        if expFormula == '--':
            print('式の形を入力してください。')
            print('プログラムが正常に動作しないため動作を停止します。')
            sys.exit()
        else:
            self.expFormula = expFormula

    def echoXmin(self):
        return self.xmin

    def echoXmax(self):
        return self.xmax

    def echodnum(self):
        return self.divisionNumber

    def echoFormula(self):
        return self.expFormula