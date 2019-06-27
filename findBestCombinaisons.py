# -*- coding: utf-8 -*-

import os
import cProfile

combinaisonsFilepath = os.path.join(os.path.dirname(__file__), 'valid_combinaisons_no_underscore_no_semicolon.txt')

PLAYERS = (
    (618.22, 'axel.tran'),
    (264.59, 'nicola.lugnani'),
    (83.45, 'renaud.danflous'),
    (22.16, 'bastien.laby'),
    (18.72, 'vincent.kauffman'),
    (13.78, 'pierre.bustingory'),
    (8, 'maxime.philippon'),
    (1.99, 'samuel.durand'),
)


PAIRS_AVERAGES = []


def getAverage(idx1, idx2):
    global PAIRS_AVERAGES
    try:
        return PAIRS_AVERAGES[idx1][idx2]
    except IndexError:
        for i in range(0, 8):
            PAIRS_AVERAGES.append([])
            for j in range(0, 8):
                PAIRS_AVERAGES[i].append((PLAYERS[i][0] + PLAYERS[j][0]) / 2.0)
        return PAIRS_AVERAGES[idx1][idx2]


def getRounds(combinaisonStr):
    return [[0, 2, 1, 3, 4, 7, 5, 6], [0, 4, 1, 5, 2, 6, 3, 7], [0, 7, 1, 6, 2, 5, 3, 4], [0, 1, 2, 3, 4, 6, 5, 7], [0, 3, 1, 2, 4, 5, 6, 7], [0, 5, 1, 4, 2, 7, 3, 6], [0, 6, 1, 7, 2, 4, 3, 5]]
    # return [[int(i) - 1 for i in combinaisonStr[k:k+8]] for k in [0, 8, 16, 24, 32, 40, 48]]


def getCombinaisonScore(combinaisonStr):
    score = 0
    for r in getRounds(combinaisonStr):
        # score += abs(getAverage(r[0], r[1]) - getAverage(r[2], r[3])) + abs(getAverage(r[4], r[5]) - getAverage(r[6], r[7]))
        score += 0
    return score


def main():

    combinaisons = []
    with open(combinaisonsFilepath, 'r') as f:
        combinaisons = f.readlines()

    combinaisonsScores = []
    for c, combinaison in enumerate(combinaisons):
        combinaisonsScores.append(getCombinaisonScore(combinaison))
        if not c % 10000:
            print c * 100 / float(len(combinaisons))

    minScore = min(combinaisonsScores)
    maxScore = max(combinaisonsScores)
    bestCombinaison = combinaisons[combinaisonsScores.index(minScore)]

    print 'maxScore', maxScore, '(%s)' % bestCombinaison.strip('\n')
    print 'minScore', minScore, '(%s)' % combinaisons[combinaisonsScores.index(minScore)].strip('\n')

    for r, pairs in enumerate(getRounds(bestCombinaison)):
        print 'Round %s' % r
        print '\t%s / %s VS %s / %s' % (PLAYERS[pairs[0]][1], PLAYERS[pairs[1]][1], PLAYERS[pairs[2]][1], PLAYERS[pairs[3]][1])
        print '\t%s / %s VS %s / %s' % (PLAYERS[pairs[4]][1], PLAYERS[pairs[5]][1], PLAYERS[pairs[6]][1], PLAYERS[pairs[7]][1])

    #TODO :
    # - Build UI with inputs for PLAYERS and score
    # - Add automatic score review ('https://badiste.fr/rechercher-joueur-badminton?todo=search&nom=laby&prenom=bastien&Submit=Rechercher')

if __name__ == '__main__':
    cProfile.run('main()')
