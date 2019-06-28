# -*- coding: utf-8 -*-

import os
import cProfile

combinaisonsFilepath = os.path.join(os.path.dirname(__file__), 'valid_combinaisons_nomultiplemeetings.txt')


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
        'HOMMES - Débutant - Poule A',
        Player('Olivier HERBIN', 0),
        Player('Enguerran BERNARD', 0),
        Player('Cédric PETIT GALLEY', 0),
        Player('Stevens BARGOT', 0),
        Player('Denis TRIPIER', 0),
        Player('Gérard LE GOUIL', 0),
        Player('VIDE1', 0),
        Player('VIDE2', 0)
    ),
    Pool(
        'HOMMES - Intermédiaire - Poule A',
        Player('Bruno DE BASTIANI', 0),
        Player('Jean-Marc BARBAGGIO', 0),
        Player('Maxime RAGOT', 0),
        Player('Thierry BRIEN', 0),
        Player('Aurélien BRAULT', 0),
        Player('Nouredine SALEH', 0),
        Player('Guillaume LESPAGNOL', 0),
        Player('Mickaël DHOURY', 0)
    ),
    Pool(
        'FEMMES - Intermédiaire - Poule A',
        Player('Marie BOURE', 0),
        Player('Corinne BERTHELOT', 0),
        Player('Yilin ZHOU', 0),
        Player('Noémie PAJOT', 0),
        Player('Pierrette MILOT', 0),
        Player('Isabelle LOREAL', 0),
        Player('VIDE1', 0),
        Player('VIDE2', 0)
    ),
    Pool(
        'HOMMES - Compétition - Poule A',
        Player('Axel TRAN', 618.22),
        Player('Nicola LUGNAGNI', 264.59),
        Player('Renaud DANFLOUS', 83.45),
        Player('Bastien LABY', 22.16),
        Player('Jules BARBAGGIO', 18.72),
        Player('Pierre BUSTINGORY', 13.78),
        Player('Maxime PHILIPPON', 8),
        Player('Julien LEBOIS', 7.48)
    ),
    Pool(
        'HOMMES - Compétition - Poule B',
        Player('Daniel MARIN', 278.63),
        Player('Renaud AGNASSE', 217.13),
        Player('Bernard LAM VAN BA', 167.43),
        Player('Théo DESAGNAT', 27.47),
        Player('Emmanuel PATEYRON', 21.92),
        Player('Vincent KAUFFMANN', 18.72),
        Player('Pierre SIAUGE', 11.32),
        Player('Samuel DURAND', 1.99)
    ),
    Pool(
        'FEMMES - Compétition - Poule A',
        Player('Lucile PATEYRON', 528.57),
        Player('Astrid GALY-DEJEAN', 395.84),
        Player('Myriam DIEMER', 358.66),
        Player('Mégane SIMON', 191.9),
        Player('Aude MIGLIASSO', 73.03),
        Player('Tiphaine CHOTEAU', 22.31),
        Player('Margaux VERDIER', 12.58),
        Player('VIDE1', 10) #TODO moyenne du tableau ici
    ),
)


def main():

    combinaisons = []
    with open(combinaisonsFilepath, 'r') as f:
        combinaisons = f.readlines()

    for pool in POOLS:
        pool.computeAverages()
        for c, combinaison in enumerate(combinaisons):
            pool.considerCombinaison(combinaison)
        pool.printResults()

    #TODO :
    # - Build UI with inputs for PLAYERS and score
    # - Add automatic score review ('https://badiste.fr/rechercher-joueur-badminton?todo=search&nom=laby&prenom=bastien&Submit=Rechercher')

if __name__ == '__main__':
    cProfile.run('main()')
