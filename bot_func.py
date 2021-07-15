import discord
import numpy as np
import random


def random(option, probability):
    rand = np.random.choice(option, size=1, p=probability)
    return rand[0]