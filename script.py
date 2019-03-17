# -*- coding: utf-8 -*-

import binascii
import os
import warnings

import numpy as np
from skimage import io
from tqdm import tqdm

warnings.filterwarnings('ignore')

BLOCK = 512
ZH_NUMBER = 3755
SIZE = 64

DEFAULT_SAVE_PATH = 'data/images'

ascii_dic = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
    'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
}


def main(filename):
    path = os.path.join('data/hcl/', filename)
    with open(path, 'rb') as f:
        f.read(BLOCK)
        for index in tqdm(range(ZH_NUMBER)):
            word = np.zeros((SIZE, SIZE), dtype=int)
            for i in range(SIZE):
                for j in range(8):
                    bit = binascii.hexlify(f.read(1))
                    data = ascii_dic[chr(bit[0])] + ascii_dic[chr(bit[1])]
                    for k in range(8):
                        word[i][j*8+k] = (1-int(data[k]))*255

            save_path = os.path.join(
                DEFAULT_SAVE_PATH,
                os.path.split(filename)[1].split('.')[0])

            if not os.path.exists(save_path):
                os.mkdir(save_path)

            io.imsave(os.path.join(save_path, str(index)+'.jpg'), word)

    print('Done.')


if __name__ == '__main__':
    main('hh001.hcl')
