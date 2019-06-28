# -*- coding: utf-8

import pickle
import re
import logging as log

log.basicConfig(format="[%(asctime)s] %(levelname)8s| %(message)s (%(filename)s:%(funcName)s:%(lineno)d)", level=log.INFO)


log.info('Parsing combinaisons ...')

combinaisons = []
with open('E:/Bastien/bad/valid_combinaisons_nounderscore2.txt', 'r') as src:
    srcLines = src.readlines()
    lineCount = len(srcLines)
    for l, line in enumerate(srcLines):
        combinaisons += [[int(i) - 1 for i in c] for c in re.findall('.{8}', line)]
        if not (l+1) % 100000:
            print(100 * (l + 1) / float(lineCount))

log.info('Parsing combinaisons done.')

log.info('Pickling to file ...')
output = 'E:/Bastien/bad/valid_combinaisons_pickle.pic'
savePickle(combinaisons, output)
log.info('Pickling to file done.')

log.info('Loading Pickle ...')
print(len(loadPickle(output)))
log.info('Loading Pickle done.')


# [
#     [[0, 2, 1, 3, 4, 7, 5, 6], [0, 4, 1, 5, 2, 6, 3, 7], [0, 7, 1, 6, 2, 5, 3, 4], [0, 1, 2, 3, 4, 6, 5, 7], [0, 3, 1, 2, 4, 5, 6, 7], [0, 5, 1, 4, 2, 7, 3, 6], [0, 6, 1, 7, 2, 4, 3, 5]],
#     [[0, 2, 1, 3, 4, 7, 5, 6], [0, 5, 1, 4, 2, 6, 3, 7], [0, 7, 1, 6, 2, 5, 3, 4], [0, 1, 2, 3, 4, 6, 5, 7], [0, 4, 1, 5, 2, 7, 3, 6], [0, 3, 1, 2, 4, 5, 6, 7], [0, 6, 1, 7, 2, 4, 3, 5]],
#     [[0, 2, 1, 3, 4, 7, 5, 6], [0, 7, 1, 6, 2, 4, 3, 5], [0, 4, 1, 5, 2, 6, 3, 7], [0, 3, 1, 2, 4, 6, 5, 7], [0, 6, 1, 7, 2, 5, 3, 4], [0, 5, 1, 4, 2, 7, 3, 6], [0, 1, 2, 3, 4, 5, 6, 7]],
#     [[0, 2, 1, 3, 4, 7, 5, 6], [0, 7, 1, 6, 2, 4, 3, 5], [0, 5, 1, 4, 2, 6, 3, 7], [0, 3, 1, 2, 4, 6, 5, 7], [0, 6, 1, 7, 2, 5, 3, 4], [0, 4, 1, 5, 2, 7, 3, 6], [0, 1, 2, 3, 4, 5, 6, 7]]
# ]
