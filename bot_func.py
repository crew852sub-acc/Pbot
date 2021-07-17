import discord
import numpy as np
import random


def random(option, probability):
    rand = np.random.choice(option, size=1, p=probability)
    return rand[0]

class Constant:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise Exception('변수에 값을 할당할 수 없습니다.')
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise Exception('변수를 삭제할 수 없습니다.')