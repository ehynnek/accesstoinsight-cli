import os
import requests #for grabbing webpages
import bs4 #beautiful soup
import re #for filtering text

### From what I can tell, Access to Insight does not have a robots.txt page, and considering this is basically just a \
### different way of browing the website one page at a time, I decided to go ahead with this program.

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


def show_copy():
    print("Copyright " + cyear + " " + cname.title())
    print("The text of this page is licensed under a Creative Commons Attribution-NonCommercial 4.0 International "
          "License. To view a copy of the license, visit www.creativecommons.org/licenses/by-nc/4.0.")
    print("From Access to Insight: www.accesstoinsight.org.")


choice = input("What would you like to see? Options are: help, copyright, sutta. ")
if choice == 'sutta':
    sutta_choice = input('Please enter a letter to display a section of the index corresponding to that letter. ')
    snum1 = ord('%s' % sutta_choice)
    snum = snum1 - 58 # Index of Suttas starts with the html nth-child at 7, so we need to write an equation to get A to equal 7.
    sindex = requests.get('https://www.accesstoinsight.org/index-sutta.html') #sets var equal to webpage
    sindex.raise_for_status()
    playFile = open('SuttaIndex.html', 'wb') #renames and opens the html file from index-sutta.html to SuttaIndex.html
    for chunk in sindex.iter_content(100000): #saves the file
        playFile.write(chunk)
    playFile.close()
    indexsoup = bs4.BeautifulSoup(sindex.text, 'html.parser')
    elems = indexsoup.select('ul.index:nth-child(%s)' % snum)
    for elem in elems:
        cleanedindex = re.sub(r'<(.*?)>', '', str(elems))
        print(cleanedindex.strip())
    # TODO: Finish this section, which will grab the link associated with the text selected in specific.sutta
    specific_sutta = input("Please type the name of one of the suttas linked above to see the text of that sutta. ")
    sutta_link = bs4.BeautifulSoup(sindex.text, "html.parser").find_all(lambda t: t.name == "a" and t.text.startswith(specific_sutta))
    print([a["href"] for a in sutta_link])
    full_link = 'https://www.accesstoinsight.org/' + str(sutta_link)
    response = requests.get('%s' % full_link)
    response.raise_for_status()
    stext_soup = bs4.BeautifulSoup(response.text, 'html.parser')
    stext = stext_soup.select('.chapter') # TODO: Grab the right parts of the code for the actual text. Maybe by using a children of .chapter function?
    print(stext)
if choice == 'help':
    print("options")
if choice == 'source':
    print("ph")
if choice == 'copyright':
    show_copy()
else:
    print(
        'An input was detected that was not among those listed by the program; if you wish to exit the program, '
        'you can interrupt the process by pressing ctrl+c.')