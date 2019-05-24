###cd pycharmprojects/csc374 && call activate root && jupyter notebook
###cd Dropbox/CSC374 && call activate root && jupyter notebook
### This is just for me, don't look, shhh
from random import randint
from start import *
from KeepTrackOfAllMyThings import *
from start import remembertable

runtimes = 200
iterations = 150   ## Figured this is enough
dirtchance = int(input("Probability for dirt: "))   #######

KeepTrackOfAllMyThings.runs = runtimes

agentchoice = input("Enter Agent Name(Simple, Random, Table): ")    ###### simple_stats, random_stats, table_stats
agentstats = ''
program = ''
progname = ''

if agentchoice.lower() == 'simple':   ####### program_simple, program_random, program_remember
    agentstats = simple_stats
    program = program_simple
    progname = 'program_simple'  #####
elif agentchoice.lower() == 'random':
    agentstats = random_stats
    program = program_random
    progname = 'program_random'
elif agentchoice.lower() == 'table':
    agentstats = table_stats
    program = program_remember
    progname = 'program_remember'
else:
    print("-- Error: Agent Not Recognized --")
    quit()


def runitall():
    room = GraphicRoom(12, 12, color={'Vacuum': (200, 0, 0), 'Dirt': (0, 200, 200), 'Wall': (0, 0, 0), 'Bump': (200, 0, 200)})
    '''the wall is in 0 and location 11'''

    location = [randint(1, 10), randint(1, 10)]
    vac = Vacuum(program)
    room.add_thing(vac, location)
    remembertable.reset()

    def dirtyitup(totaldirt):
        row = 0
        col = 1

        for x in range(100):
            row += 1

            if row > 10:
                row = 1
                col += 1
            if random.randrange(0, 100) < dirtchance:
                room.add_thing(Dirt(), [row, col])
                totaldirt += 1
        return totaldirt

    totaldirt = dirtyitup(0)  # run with 10% chance of dirt
    agentstats.dirtcountadd(totaldirt)
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::\n"
          ":::::With a probability of {}%, {} blocks are dirty:::::\n"
          ":::::::::::::::::::::::::::::::::::::::::::::::::::::::".format(dirtchance, totaldirt))

    room.reveal()
    room.run(iterations, 0) #0 Speeds it up so fast it's so nice. Just take it out if you want it to go slow


for x in range(0, runtimes):

    KeepTrackOfAllMyThings.runnum += 1
    runitall()
    agentstats.show()

        # Ignore all these, they look ugly
finalaverages = agentstats.totals()        ###################Time to print out all the results we need
print("\n\n::::::::::::::::::::::::::::::::::::::\n"
      ":::::::::::::: RESULTS :::::::::::::::\n"
      "::::::::::::::::::::::::::::::::::::::\n"
      ":::: Run  {} times :::::::::::::::::::\n"
      ":::: With {} iterations each run :::::\n"
      ":::: And {}% probability for Dirt ::::\n"
      "::::::::::::::::::::::::::::::::::::::\n"
      "".format(runtimes, iterations, dirtchance))
print(":::::::::::::::::::::::::::::::::\n"
      ":::::::::::::  Totals  ::::::::::\n"
      "::: Total Dirty Spaces:   {} ::: \n"
      "::: Total Spaces Cleaned: {} :::\n"
      "::: Total Spaces Moved    {} :::\n"
      ":::::::::::::::::::::::::::::::::\n"
      "".format(finalaverages[0], finalaverages[1], finalaverages[2]))
print("/////////////////////////////////////\n"
      "////////////  Averages  /////////////\n"
      "/// Average Dirty Spaces:   {} /// \n"
      "/// Average Spaces Cleaned: {} ///\n"
      "/// Average Spaces Moved    {} ///\n"
      "/////////////////////////////////////\n"
      "".format((finalaverages[0]/runtimes), (finalaverages[1]/runtimes), (finalaverages[2]/runtimes)))
print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
      "!!!!!!! {}'s Average Performance !!!!!\n"
      "!!!!!!!!!!! Cleaned Spaces / Total Dirt !!!!!!!!!!!!\n"
      "!!!!!!!!!!!!!!!!!!!!!!! EQUALS !!!!!!!!!!!!!!!!!!!!!\n"
      "!!!!!!!!!!!!!!!!!!!!!!! {:.2f}% !!!!!!!!!!!!!!!!!!!!!\n"
      "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
      "".format(progname, (finalaverages[1]/finalaverages[0])*100))
