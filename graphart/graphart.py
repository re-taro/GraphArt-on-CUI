# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from classFile import ExpressionTemplate as expTemp


PI = np.pi
expdata = []
X = []
Y = []
outfile = '../OUTPUT/plot.png'


def setup(numOfExp):
    for i in range(numOfExp):
        expdata[i] = expTemp()
        print(i + 1 + '番目の式を設定していきます。')
        minX = input('xの最小値を入力してください: ')
        maxX = input('xの最大値を入力してください: ')
        dnum = input('分割数を入力してください: ')
        formExp = input('式を入力してください: ')

        expdata[i].expRule(minX, maxX, dnum, formExp)

def drawGraph(numOfExp):
    ax = plt.axes(label='xxx')
    ax.set_aspect('equal')
    plt.xticks(np.arange(-100, 100, 2))
    plt.yticks(np.arange(-100, 100, 2))
    plt.axis([0, 50, 0, 50])
    plt.grid(which='major', color='gray', linestyle='--')
    for i in range(numOfExp):
        X[i] = np.linspace(expdata[i].echoXmin, expdata[i].echoXmax, expdata[i].echodnum)
        Y[i] = expdata[i].echoFormula
        plt.plot(X[i], Y[i])
    if os.path.isfile(outfile):
        os.remove(outfile)
    plt.savefig(outfile)





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
        drawGraph(numOfExp)
        break
    sys.exit()