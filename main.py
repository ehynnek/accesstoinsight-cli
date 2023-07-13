import os
import requests
import bs4

welcome_mantra = """The non-doing of any evil,
the performance of what's skillful,
the cleansing of one's own mind:
    this is the teaching
    of the Awakened."""
copy = ['thanissaro bhikku', '1997']
cname = copy[0]
cyear = copy[1]

welcome = "Welcome to the unofficial terminal client for Access to Insight; for resources on using this application, " \
          "you just have to type 'help'.\n\nTo view copyright on a passage, simply type 'copyright', which will " \
          "display copyright information on the last passage you viewed."

# There is likely be a better way to add a line break without the blank print command.
print(welcome)
print()
print(welcome_mantra)
print()


def copy():
    print("Copyright " + cyear + " " + cname.title())
    print("The text of this page is licensed under a Creative Commons Attribution-NonCommercial 4.0 International "
          "License. To view a copy of the license, visit www.creativecommons.org/licenses/by-nc/4.0.")
    print("From Access to Insight: www.accesstoinsight.org.")


choice = input("What would you like to see? Options are: help, copyright, sutta.")
if choice == 'sutta':
    sutta_choice = input('Please enter a letter to display a section of the index corresponding to that letter.')
    if sutta_choice == 'A':
        print("Retrieving...")
if choice == 'help':
    print("options")
if choice == 'source':
    print("ph")
if choice == 'copyright':
    copy()
else:
    print(
        'An input was detected that was not among those listed by the program; if you wish to exit the program, '
        'you can interrupt the process by pressing ctrl+c.')

# Index of Suttas starts with the html nth-child at 7, so we need to write an equation to get A to equal 7.
suttanum = ( - 58)
print(suttanum)


def getnum(suttanum):
    snum = ord('%s' % sutta_choice)
    snum = snum - 58


def indexselect(snum):
    indexsoup.select('ul.index:nth-child(%s)' % suttanum)

sindex = requests.get('https://www.accesstoinsight.org/index-sutta.html')
sindex.raise_for_status()
playFile = open('SuttaIndex.html', 'wb')
for chunk in sindex.iter_content(100000):
    playFile.write(chunk)
playFile.close()
indexsoup = bs4.BeautifulSoup(sindex.text, 'html.parser')
getnum(sutta_choice)
elems = indexselect(suttanum)