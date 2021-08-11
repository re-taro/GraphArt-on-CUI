# -*- coding: utf-8 -*-
import sys


class ExpressionTemplate:
    def __init__(self):
        self.expType = '--'
        self.xmin = -100
        self.xmax = 100
        self.ymin = -100
        self.ymax = 100
        self.divisionNumber = 1000
        self.expFormula = '--'

    def expRule(self, expType, xmin, xmax, ymin, ymax, divisionNumber, expFormula):
        if expType == '--':
            print('式の種類を入力してください。')
            print('プログラムが正常に動作しないため動作を停止します。')
            sys.exit()
        else:
            self.expType = expType
        if xmin == '--':
            pass
        else:
            self.xmin = xmin
        if xmax == '--':
            pass
        else:
            self.xmax = xmax
        if ymin == '--':
            pass
        else:
            self.ymin = ymin
        if ymax == '--':
            pass
        else:
            self.ymax = ymax
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

    def echoType(self):
        return self.expType

    def echoXmin(self):
        return self.xmin

    def echoXmax(self):
        return self.xmax

    def echoYmin(self):
        return self.ymin

    def echoYmax(self):
        return self.ymax

    def echodnum(self):
        return self.divisionNumber

    def echoFormula(self):
        return self.expFormula