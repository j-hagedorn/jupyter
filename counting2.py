#!/usr/bin/python

from re import compile
print "Move the file you want to count into the same directory as the python file."
print "When Prompted for the inout file type file name plus extension"
print "Name your Output File test.txt"
l=compile("([\w,.'\x92]*\w)").findall(open(raw_input('Input file: '),'r').read().lower())
f=open(raw_input('Output file: '),'w')
print "Counting The Frequency of the Words....................................."
print "..............................." * 10
print "..............................." * 100
print "..............................." * 10000


for word in set(l):
    print>>f, word, '\t', l.count(word)
    
txt = open('test.txt')

print "Here's your file:"
print txt.read()
f.close()
