# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys
import copy
from classFile import Expression as exp


PI = np.pi


def setup(numOfExp):
    for i in range(numOfExp):
        

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
