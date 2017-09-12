# Given a Master Index URL from EDGAR find the path of raw text filing (10-K) for a given year and CIK 
import urllib2
import time
import csv
import sys

CIK = '1018724' #AMAZON COM INC
Year = '2013'   #GIVEN
FILE='10-K'     #GIVEN


#####Get the Master Index File for the given Year


url='https://www.sec.gov/Archives/edgar/full-index/%s/QTR1/master.idx' %(Year)
response = urllib2.urlopen(url)

string_match1 = 'edgar/data/'
element2 = None
element3 = None
element4 = None


###Go through each line of the master index file and find given CIK and FILE (10-K) and extract the text file path
for line in response:
    if CIK in line and FILE in line:
        for element in line.split(' '):
            if string_match1 in element:
                element2=element.split('|')
                for element3 in element2:
                        if string_match1 in element3:
                                element4=element3


# The path of the 10-K filing
url3 = 'https://www.sec.gov/Archives/'+element4 
response3 = urllib2.urlopen(url3)


words = ['anticipate','believe', 'depend', 'fluctuate', 'indefinite', 'likelihood', 'possible', 'predict', 'risk', 'uncertain']

count={}
for elem in words:
    count[elem] = 0 

for line in response3:
    elements = line.split()
    for word in words:
        count[word] = count[word]+elements.count(word)

print (CIK)
print (Year)
print (url3)
print (count)
