# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys
import copy
from classFile import ExpressionTemplate as expTemp


PI = np.pi
exp = []


def setup(numOfExp):
    for i in range(numOfExp):
        exp[i] = expTemp()

        print(i + 1 + '番目の式を設定していきます。')
        typeExp = input('式の種類を入力してください: ')
        minX = input('xの最小値を入力してください: ')
        maxX = input('xの最大値を入力してください: ')
        minY = input('yの最小値を入力してください: ')
        maxY = input('yの最大値を入力してください: ')
        dnum = input('分割数を入力してください: ')
        formExp = input('式を入力してください: ')

        exp[i].expRule(typeExp, minX, maxX, minY, maxY, dnum, formExp)

def drawGraph():
    canvas = plt.figure(figsize = (4, 4),
                        dpi = 100,
                        facecolor = 'w')




def main():
    print('README.pdfを読みましたか？')
    readFlag = input('Y/n: ')
    if readFlag == 'Y' or readFlag == 'y':
        print('入力する式の数を入力してください。')
        numOfExp = input('ここに入力してください: ')
    elif readFlag == 'n' or readFlag == 'N':
        print('READMEへもう一度目を通してから再度プログラムを起動してください。')
        sys.exit()
    else:
        print('Yかnで答えてください。')
        sys.exit()
    while True:
        setup(numOfExp)
