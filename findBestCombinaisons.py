# -*- coding: utf-8 -*-

import os
import cProfile

combinaisonsFilepath = os.path.join(os.path.dirname(__file__), 'valid_combinaisons_no_underscore_no_semicolon.txt')


def getCombinaisonRounds(combinaisonStr):
    '''
    Return the string combinaison into a list of list of integers.
    '''
    return [[int(i) - 1 for i in combinaisonStr[k:k+8]] for k in [0, 8, 16, 24, 32, 40, 48]]


class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Pool(object):
    def __init__(self, poolName, p1, p2, p3, p4, p5, p6, p7, p8):
        self.name = poolName
        self.players = (p1, p2, p3, p4, p5, p6, p7, p8)
        self.bestCombinaison = None
        self.bestCombinaisonScore = None
        self.averages = []

    def computeAverages(self):
        for i in range(0, 8):
            self.averages.append([])
            for j in range(0, 8):
                self.averages[i].append((self.players[i].score + self.players[j].score) / 2.0)
    
    def getAverage(self, i, j):
        return self.averages[i][j]
    
    def considerCombinaison(self, combinaisonStr):
        '''
        Consider the given combinaison, and keep its results if this is a better combinaison than the one already stored.
        '''
        score = 0
        for r in getCombinaisonRounds(combinaisonStr):
            score += abs(self.getAverage(r[0], r[1]) - self.getAverage(r[2], r[3])) + abs(self.getAverage(r[4], r[5]) - self.getAverage(r[6], r[7]))
            # score += 0
        if not self.bestCombinaison or score < self.bestCombinaisonScore:
            self.bestCombinaison = combinaisonStr
            self.bestCombinaisonScore = score
    
    def printResults(self):

        print 'Pool %s' % self.name
        print 'Best combinaison : %s (%s)' % (self.bestCombinaison, self.bestCombinaisonScore)
        for r, pairs in enumerate(getCombinaisonRounds(self.bestCombinaison)):
            print 'Round %s' % r
            print '\t%s / %s VS %s / %s' % (self.players[pairs[0]].name, self.players[pairs[1]].name, self.players[pairs[2]].name, self.players[pairs[3]].name)
            print '\t%s / %s VS %s / %s' % (self.players[pairs[4]].name, self.players[pairs[5]].name, self.players[pairs[6]].name, self.players[pairs[7]].name)


POOLS = (
    Pool(
        'deb_hommes',
        Player('axel.tran', 618.22),
        Player('nicola.lugnani', 264.59),
        Player('renaud.danflous', 83.45),
        Player('bastien.laby', 22.16),
        Player('vincent.kauffman', 18.72),
        Player('pierre.bustingory', 13.78),
        Player('maxime.philippon', 8),
        Player('samuel.durand', 1.99) 
    ),
    # Pool(
    #     'int_hommes',
    #     Player('axel.tran', 618.22),
    #     Player('nicola.lugnani', 264.59),
    #     Player('renaud.danflous', 83.45),
    #     Player('bastien.laby', 22.16),
    #     Player('vincent.kauffman', 18.72),
    #     Player('pierre.bustingory', 13.78),
    #     Player('maxime.philippon', 8),
    #     Player('samuel.durand', 1.99) 
    # ),
    # Pool(
    #     'int_femmes',
    #     Player('axel.tran', 618.22),
    #     Player('nicola.lugnani', 264.59),
    #     Player('renaud.danflous', 83.45),
    #     Player('bastien.laby', 22.16),
    #     Player('vincent.kauffman', 18.72),
    #     Player('pierre.bustingory', 13.78),
    #     Player('maxime.philippon', 8),
    #     Player('samuel.durand', 1.99) 
    # ),
    # Pool(
    #     'comp_hommes_1',
    #     Player('axel.tran', 618.22),
    #     Player('nicola.lugnani', 264.59),
    #     Player('renaud.danflous', 83.45),
    #     Player('bastien.laby', 22.16),
    #     Player('vincent.kauffman', 18.72),
    #     Player('pierre.bustingory', 13.78),
    #     Player('maxime.philippon', 8),
    #     Player('samuel.durand', 1.99) 
    # ),
    # Pool(
    #     'comp_hommes_2',
    #     Player('axel.tran', 618.22),
    #     Player('nicola.lugnani', 264.59),
    #     Player('renaud.danflous', 83.45),
    #     Player('bastien.laby', 22.16),
    #     Player('vincent.kauffman', 18.72),
    #     Player('pierre.bustingory', 13.78),
    #     Player('maxime.philippon', 8),
    #     Player('samuel.durand', 1.99) 
    # ),
    # Pool(
    #     'comp_femmes',
    #     Player('axel.tran', 618.22),
    #     Player('nicola.lugnani', 264.59),
    #     Player('renaud.danflous', 83.45),
    #     Player('bastien.laby', 22.16),
    #     Player('vincent.kauffman', 18.72),
    #     Player('pierre.bustingory', 13.78),
    #     Player('maxime.philippon', 8),
    #     Player('samuel.durand', 1.99) 
    # ),
)


def main():

    combinaisons = []
    with open(combinaisonsFilepath, 'r') as f:
        combinaisons = f.readlines()

    for pool in POOLS:
        print 'Compute pool %s' % pool.name
        pool.computeAverages()
        for c, combinaison in enumerate(combinaisons):
            pool.considerCombinaison(combinaison)
            if not c % 10000:
                print c * 100 / float(len(combinaisons))
        pool.printResults()

    #TODO :
    # - Build UI with inputs for PLAYERS and score
    # - Add automatic score review ('https://badiste.fr/rechercher-joueur-badminton?todo=search&nom=laby&prenom=bastien&Submit=Rechercher')

if __name__ == '__main__':
    cProfile.run('main()')
