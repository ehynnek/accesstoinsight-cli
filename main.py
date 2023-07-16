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
copy = ['©1997 Thanissaro Bhikku']
cleancopy = copy

welcome = "Welcome to the unofficial terminal client for Access to Insight; for resources on using this application, " \
          "just type 'help'.\n\nTo view copyright on a passage, simply type 'copyright', which will " \
          "display copyright information on the last passage you viewed."

# There is likely be a better way to add a line break without the blank print command.
print(welcome)
print()
print(welcome_mantra)
print()


def show_copy():
    print(cleancopy.strip(" []"))
    print()
    print("The text of this page is licensed under a Creative Commons Attribution-NonCommercial 4.0 International "
          "License. To view a copy of the license, visit www.creativecommons.org/licenses/by-nc/4.0.")
    print()
    print("From Access to Insight: www.accesstoinsight.org.")

while True:
    choice = input("What would you like to see? Options are: help, copyright, sutta. ")
    if choice == 'sutta':
        sutta_choice = input('Please enter a letter to display a section of the index corresponding to that letter. ')
        if sutta_choice == 'A' or 'a':
            snum = 7
        if sutta_choice == 'B' or 'b':
            snum = 9
        if sutta_choice == 'C' or 'c':
            snum = 11
        if sutta_choice == 'D' or 'd':
            snum = 13
        if sutta_choice == 'E' or 'e' or 'F' or 'f':
            snum = 15
        if sutta_choice == 'G' or 'g':
            snum = 17
        if sutta_choice == 'H' or 'h':
            snum = 19
        if sutta_choice == 'I' or 'i':
            snum = 21
        if sutta_choice == 'J' or 'j':
            snum = 23
        if sutta_choice == 'K' or 'k':
            snum = 25
        if sutta_choice == 'L' or 'l':
            snum = 27
        if sutta_choice == 'M' or 'm':
            snum = 29
        if sutta_choice == 'N' or 'n':
            snum = 31
        if sutta_choice == 'O' or 'o':
            snum = 32
        if sutta_choice == 'P' or 'p' or 'Q' or 'q':
            snum = 34
        if sutta_choice == 'R' or 'r':
            snum = 36
        if sutta_choice == 'S' or 's':
            snum = 38
        if sutta_choice == 'T' or 't':
            snum = 40
        if sutta_choice == 'U' or 'u':
            snum = 42
        if sutta_choice == 'V' or 'v':
            snum = 44
        if sutta_choice == 'W' or 'w' or 'X' or 'x' or 'Y' or 'y' or 'Z' or 'z':
            snum = 46
        sindex = requests.get('https://www.accesstoinsight.org/index-sutta.html') #sets var equal to webpage
        sindex.raise_for_status()
        indexsoup = bs4.BeautifulSoup(sindex.text, 'html.parser')
        elems = indexsoup.select('ul.index:nth-child(%s)' % snum)
        for elem in elems:
            cleanedindex = re.sub(r'<(.*?)>', '', str(elems))
            print(cleanedindex.strip())
        specific_sutta = input("Please type the name of one of the suttas linked above to see the text of that sutta. ")
        sutta_link = bs4.BeautifulSoup(sindex.text, "html.parser").find_all(lambda t: t.name == "a" and t.text.startswith(specific_sutta))
        pure_link = [a["href"] for a in sutta_link]
        full_link = 'https://www.accesstoinsight.org/' + str(pure_link[0])
        response = requests.get('%s' % full_link)
        response.raise_for_status()
        stext_soup = bs4.BeautifulSoup(response.text, 'html.parser')
        stexts = stext_soup.select('.chapter')
        for stext in stexts:
            slashp1 = re.sub(r'</p>', '\n', str(stext))
            slashp = re.sub(r'&amp;', '&', str(slashp1))
            cleaned_stext = re.sub(r'<(.*?)>', '', str(slashp))
            print(cleaned_stext.rstrip('\n'))
        copyraw = indexsoup.select('#F_sourceCopy')
        for copy in copyraw:
            cleancopy = re.sub(r'<(.*?)>', '', str(copyraw))
        # TODO: Separate the "Notes" section from the usual text section of the suttas.
    if choice == 'help':
        print("options")
    if choice == 'source':
        print("ph")
    if choice == 'copyright':
        show_copy()