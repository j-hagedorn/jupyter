# -*- coding: utf-8 -*-
"""
Created on Sat Dec 07 20:07:39 2013

@author: jhagedorn
"""

#%%
def import_FASTA(url):
    '''A function to 1. import a FASTA (.fna) file into Python as a list the 
    comprised of the nucleotide sequence 2. Save a local version of the .fna 
    file for future use.
    '''
    import urllib2
    geturl = urllib2.urlopen(url)
    seq = geturl.read()
    entries = seq.split('>')[1:]     # skip blank first entry
    partitioned_entries = [entry.partition('\n') for entry in entries]
    pairs = [(entry[0], entry[2]) for entry in partitioned_entries]  # omit '>'
    pairs2 = [(pair[0], pair[1].replace('\n', '')) for pair in pairs]
    result = [pair[1] for pair in pairs2]
    result2 = [(pair[0].split('|'), pair[1]) for pair in pairs2]
    filename = str({info[4] for info, seq in result2}) + '.fna' # Use metadata from .fna file as title
    import urllib2
    geturl = urllib2.urlopen(url)
    seq = geturl.read()
    local_file = open(filename,"w")     # Open a local file for writing
    local_file.write(seq)               # Write to our local file
    local_file.close()
    return result
    
#%%
def read_FASTA(filename):
    '''A function to read a FASTA (.fna) file into Python as a list with two 
    parts: 1. metadata related to the sequence, 2. the sequence itself
    '''
    with open(filename) as file:
        contents = file.read()            # only statement inside the with
    entries = contents.split('>')[1:]     # skip blank first entry
    partitioned_entries = [entry.partition('\n') for entry in entries]
    pairs = [(entry[0], entry[2]) for entry in partitioned_entries]  # omit '>'
    pairs2 = [(pair[0], pair[1].replace('\n', '')) for pair in pairs]
    result = [(pair[0].split('|'), pair[1]) for pair in pairs2]
    return result
#%%

