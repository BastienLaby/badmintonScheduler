# -*- coding: utf-8 -*-

import os
import cProfile

combinaisonsFilepath = os.path.join(os.path.dirname(__file__), 'valid_combinaisons_no_underscore_no_semicolon.txt')


def getCombinaisonRounds(combinaisonStr):
    '''
    Return the string combinaison into a list of list of integers.
    '''
    return [[int(i) - 1 for i in combinaisonStr[k:k+8]] for k in [0, 8, 16, 24, 32, 40, 48]]


    score = 0
    for r in getCombinaisonRounds(combinaisonStr):
        score += abs(self.getAverage(r[0], r[1]) - self.getAverage(r[2], r[3])) + abs(self.getAverage(r[4], r[5]) - self.getAverage(r[6], r[7]))
        # score += 0
    if not self.bestCombinaison or score < self.bestCombinaisonScore:
        self.bestCombinaison = combinaisonStr
        self.bestCombinaisonScore = score



def main():

    combinaisons = []
    with open(combinaisonsFilepath, 'r') as f:
        combinaisons = f.readlines()

    outputCombinaisons = []

    for c, combinaison in enumerate(combinaisons):

        meetings = []
        for i in xrange(0, 8):
            meetings.append([])
            for j in xrange(0, 8):
                meetings[i].append(0)

        for p1, p2, p3, p4, p5, p6, p7, p8 in getCombinaisonRounds(combinaison):
            meetings[p1][p3] += 1
            meetings[p1][p4] += 1
            meetings[p2][p3] += 1
            meetings[p2][p4] += 1
            meetings[p3][p1] += 1
            meetings[p3][p2] += 1
            meetings[p4][p1] += 1
            meetings[p4][p2] += 1
            meetings[p5][p7] += 1
            meetings[p5][p8] += 1
            meetings[p6][p7] += 1
            meetings[p6][p8] += 1
            meetings[p7][p5] += 1
            meetings[p7][p6] += 1
            meetings[p8][p5] += 1
            meetings[p8][p6] += 1

        combinaisonIsValid = True
        for playerMeetings in meetings:
            if max(playerMeetings) > 4:
                combinaisonIsValid = False
                break
            playerMeetings.remove(0) # itself
            if min(playerMeetings) == 0:
                combinaisonIsValid = False
                break

        if combinaisonIsValid:
            outputCombinaisons.append(combinaison)

    print len(combinaisons)
    print len(outputCombinaisons)

    with open(os.path.join(os.path.dirname(__file__), 'valid_combinaisons_nomultiplemeetings.txt'), 'w') as f:
        f.writelines(outputCombinaisons)

    #TODO :
    # - Build UI with inputs for PLAYERS and score
    # - Add automatic score review ('https://badiste.fr/rechercher-joueur-badminton?todo=search&nom=laby&prenom=bastien&Submit=Rechercher')

if __name__ == '__main__':
    cProfile.run('main()')
