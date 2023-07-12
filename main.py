# Press Shift+F10 to execute it or replace it with your code.
import os

welcome_mantra = """The non-doing of any evil,
the performance of what's skillful,
the cleansing of one's own mind:
    this is the teaching
    of the Awakened."""
copy = ['thanissaro bhikku', 1997]
cname = copy[0]
cyear = copy[1]

welcome = "Welcome to the unofficial terminal client for Access to Insight; for resources on using this application, " \
          "use the command ati --help.\n\nTo view copyright on a passage, use the command ati --c, which will " \
          "display copyright information on the last passage you viewed."

# There is likely be a better way to add a line break without the blank print command.
print(welcome)
print()
print(welcome_mantra)

choice = input("What would you like to see? Options are: help, copyright, sutta.")
if choice == 'sutta':
    sutta_choice = input("Please enter a letter to display a section of the index corresponding to that letter.")
if choice == 'help':
    print("options")
if choice == 'copyright':
    print("Copyright " + cyear + cname.title())
else:
    print(
        'An input was deteced that was not among those listed by the program; if you wish to exit the program, you can interruprt the process by pressing cntrl+c.')

if sutta_choice == 'a':
    sutta_a = input("Please select one from the following:")