# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys
import copy


class Expression:
    def __init__(self):
        self.

def setup(numOfExp):


def drawGraph():
    canvas = plt.figure(figsize = (1.920, 1.080),
                        dpi = 1000,
                        facecolor = 'w')
    



def main():
    print('README.PDFを読みましたか？')
    readFlag = input('Y/n ')
    if readFlag == 'Y' or readFlag == 'y':
        print('入力する式の数を入力してください。')
        numOfExp = input('ここに入力してください: ')
    elif readFlag == 'n' or readFlag == 'N':
        print('もう一度目を通してから再度プログラムを起動してください。')
        sys.exit()
    else:
        print('Yかnで答えてください。')
        sys.exit()
    while True:
        setup(numOfExp)
