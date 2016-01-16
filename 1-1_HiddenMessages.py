# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:22:55 2013
@author: Joshua

Frequent Words Problem: Find the most frequent k-mers in a string.
Input:      A string Text and an integer k.
Output:     All most frequent k-mers in Text.
"""
#%% Read files
# load = open("Rosalind_hiddenWords_11mer.txt")
# seq = load.read()
# k = raw_input('Put the k in k-mer. k = ')
# k = int(k) #Convert input to integer

#%% Input variables
seq = 'AAGGCGAGGAAGGCGAGGCACTCAGAAGGCGAGGTACCGAGAACACTCAGAAGGCGAGGAAGGCGAGGACGAGGAAGGCGAGGAAGGCGAGGCACTCAGTACCGAGAAAAGGCGAGGTACCGAGAAACGAAACGAGGAAGGCGAGGTACCGAGAAACGAAAAGGCGAGGAAGGCGAGGCACTCAGACGAGGACGAATACCGAGAACACTCAGACGAGGAAGGCGAGGCACTCAGACGAGGTACCGAGAACACTCAGACGAAACGAGGCACTCAGTACCGAGAACACTCAGTACCGAGAAACGAGGACGAAACGAGGACGAGGACGAGGTACCGAGAAACGAAACGAGGCACTCAGAAGGCGAGGACGAGGACGAGGCACTCAGACGAAAAGGCGAGGACGAAACGAGGACGAGGACGAACACTCAGCACTCAGAAGGCGAGGACGAGGACGAAACGAATACCGAGAATACCGAGAAACGAGGACGAAAAGGCGAGGACGAGGCACTCAGACGAAACGAGGCACTCAGCACTCAGACGAAACGAAACGAAAAGGCGAGGACGAACACTCAGACGAGGCACTCAGACGAGGACGAGGACGAGGACGAAACGAGGACGAGGAAGGCGAGGAAGGCGAGGTACCGAGAACACTCAGTACCGAGAAAAGGCGAGGCACTCAGACGAGGCACTCAGACGAATACCGAGAATACCGAGAATACCGAGAAACGAAACGAATACCGAGAAACGAGGTACCGAGAAACGAACACTCAGACGAGGCACTCAGCACTCAGAAGGCGAGGACGAAAAGGCGAGGACGAGGAAGGCGAGGACGAGGTACCGAGAAAAGGCGAGGTACCGAGAAACGAGGACGAA'
k = 11 # Define "k" in k-mer

#%% Define frequent hidden words function
def freqKmer(seq, k):
    '''
    Function to find the most frequent k-mers in a string.
    Input:      A string Text and an integer k.
    Output:     All most frequent k-mers in Text.
    '''
    n = 0 # Start at beginning of sequence
    counts = {} # Make an empty dictionary
    for i in seq:
        kmer = seq[n:n+k]
        if kmer in counts: # Add each k-mer to dictionary & count repeats
            counts[kmer] += 1
        else:
            counts[kmer] = 1
        n = n+1 # move initial position to next nucleotide
    for w in sorted(counts, key=counts.get, reverse=True):
        # print w, counts[w] # Sort and print k-mers by frequency

        highest = max(counts.values())
        print [i for i,v in counts.items() if v == highest]

#%% Do it!
freqKmer(seq, k)

#%%
from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(counts)
counts.plot(kind='barh', rot=0)