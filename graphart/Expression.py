import sys


class Expression:
    def __init__(self):
        self.expType = None
        self.xmin = -100
        self.xmax = 100
        self.ymin = -100
        self.ymax = 100
        self.divisionNumber = 1000

    def expRule(self, expType, xmin, xmax, ymin, ymax, divisionNumber, expFormula):
        if expType is None:
            print("式の種類を入力してください。")
            print("プログラムが正常に動作しないため動作を停止します。")
            sys.exit()
        else:
            self.expType = expType
        if xmin is None:
            pass
        else:
            self.xmin = xmin
        if xmax is None:
            pass
        else:
            self.xmax = xmax
        if ymin is None:
            pass
        else:
            self.ymin = ymin
        if ymax is None:
            pass
        else:
            self.ymax = ymax
        if divisionNumber is None:
            pass
        else:
            self.divisionNumber = divisionNumber
        if expFormula is None:
            print("式の形を入力してください。")
            print("プログラムが正常に動作しないため動作を停止します。")
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