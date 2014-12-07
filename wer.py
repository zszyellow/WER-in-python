#-*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy

def wer(r, h):
    """
    This function is the main function of calculate the WER. It uses a popular module called numpy.
    The type of r and h is list.
    """
    d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8).reshape((len(r)+1, len(h)+1))
    for i in range(len(r)+1):
        for j in range(len(h)+1):
            if i == 0: d[0][j] = j
            elif j == 0: d[i][0] = i
    for i in range(1,len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                substitute = d[i-1][j-1] + 1
                insert = d[i][j-1] + 1
                delete = d[i-1][j] + 1
                d[i][j] = min(substitute, insert, delete)

    x = len(r)
    y = len(h)
    list = []
    while True:
        if x == 0 and y == 0: 
            break
        else:
            if d[x][y] == d[x-1][y-1]: 
                list.append("e")
                x = x-1
                y = y-1
            elif d[x][y] == d[x][y-1]+1:
                list.append("i")
                x = x
                y = y-1
            elif d[x][y] == d[x-1][y-1]+1:
                list.append("s")
                x = x-1
                y = y-1
            else:
                list.append("d")
                x = x-1
                y = y
    list = list[::-1]

    print list

if __name__ == '__main__':
    wer("who is there".split(), "is there".split())      