#parse a docx file to find [submit]s without timers
from docx import Document
import os, re

#print os.path.dirname(os.path.abspath(__file__)) 
#doc2 = Document(os.path.dirname(os.path.abspath(__file__))+'\demo.docx')


def removeBracketed(text):
    '''Remove text enclosed in square brackets.  Regexes can't really handle
    nested brackets, so this does it manually.'''
    bc = 0
    temp = ''
    for char in text:
        if char == '[':
            bc += 1
        if bc == 0: temp += char
        if char == ']':
            bc -= 1
    return temp

	
text1 = 'T2  Here\'s some text with a [bracket], [submit, 0], and a [submit active]. This is then followed by a [submit clicked]. [submit clicked, 2:00] and [submit active]. This is followed by a [popup] and some words.'

text2 = 'T3  And now here [submit active] is some text [popup]'

#print removeBracketed(text1)
#print re.sub('^[A-Z][0-9]* ','',text1).split('/ /')[0]

sa = []
sb = []
if 'submit active' in text1.lower():
	#print re.findall('submit', text1)
	#print re.finditer('submit', text1)
	satemp = [[m.start(0), m.end(0), 'sa'] for m in re.finditer('submit active', text1)]
	#if re.search('[0-9]+:[0-9][0-9]',text1):
		#print re.search('[0-9]+:[0-9][0-9]', text1).group(0)
if 'submit clicked' in text1.lower():
	sctemp = [[m.start(0), m.end(0), 'sc'] for m in re.finditer('submit clicked', text1)]

sac = satemp + sctemp
sac = sorted(sac)
print sac

saclist = [elem[2] for elem in sac]
print saclist

if saclist[0] == 'sc':
	print 'missing [submit active] at the beginning'
if saclist[-1] == 'sa':
	print 'missing [submit clicked] at the end'
print len(saclist)

sactest = [] #list of perfect submit active-clicked list
for i in range(len(saclist)/2):
	sactest.extend(['sa', 'sc'])

if 'popup' in text2.lower():
	if not re.search('submit active', text2):
		print 'possible missing submit active'
	