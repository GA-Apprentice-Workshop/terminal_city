from sys import argv
# Level 1: The crime scene
# Player will inspect the crime scene.
# File will print out at the end of the level.
city = '''
     //o
                                           /:s
                                           :/y
                                          odddh`
                                          sosoM.
                                          y+s+N.
                                          h+o/N.
                                        +dd+o/msy.
                                        oh:+s/y.N.
                                        oh:+y/s`N.
                                        oy-+y/o`N.
                                        ss.+y:o`N`         :++///
                           :hsoys.      oy/yhsy:N`         dh--sM`
         .:::::--`         /N``sm:      +y/-+/s-N`         dy  oN`
         +d///:/m-       .+ym  yN/      os://:o.N`         dy  sN`
     oo+ohm.    h-::::/. :dsm  ym+     /do:+/:o`mo       //my  yN/+.
    `m:.ssdds   d-N+:/Ny`:h/m -sm+     +s`:++/+ /N`      mo:y  s:-N:
    +d` /ssoM.  d-N- `yN-:h-o /:d/.----sy-/++/o -N`      d+.y  s``N-
    m/  +sy:M.  d:N- `sN-/h .-oomoyhs++oo/ds+/s -moooos` d/`s  s` N.    ++//////
    m:  +ss:M`  d/N- `sN-/h odo+o+hos++o/ sdsos+`--+ysN+/ds/+  s` N-```.N/------
    m:  +ys-N`  d/N- `smsoy:yh:.:.oos:oo+ hy  `y/oohh--odhyyo++y-`so++::N/--.
    N-  +yy-Nsoodymss+sh+---yh:./-sos:oo+ hy..-dhh--.  +d./+:s-m/ohoods-N/
   `N-  +yy-N``-----dhy:----yh. :-hs/-:yo`sdooooms     /d :+.y d/so  -++oN`
 ://N+::shy+m:.Mo+++++++ooooohm.NsshM::+/-//:-.odh+++++ym+o. ` m/s+     `N`
:++++//////::::M/:::-  :NhhhhhdhN:yhMy+++     `m-osssssss-N./+/yoso:.   `N.
//::::::::::::::///ym  :N``     +:+ys.`-N     `m`ydhyyyy+ N.            `y`
 `.-++++-::. --.+++od.`/y++++`  +- /o -oh++::::s-..`      m.
.+--    -.`:/--:    `/:-     ` .ys+sh+//:::......-.
===========================================================================
----------                     TERMINAL CITY                    -----------
'''
print city
print '''
There's been a crime in Terminal City. It's up to you to solve it.

Since you're a rookie detective here's some information to help you
get around the command line.

* Type `man cat` to learn about reading files.
* Type `man grep` to learn about searching files.

To crack the case you will want to collect CLUEs from the crimescene.
If you need a hint, type HINT.
'''

level = open('crimescene', 'r')
hint_count = 0

def response():
    res = raw_input('> ')
    return res

print "Search: "
response()

# open modes:
# r = read, w = overwrite, r+ = read and write, a = append
notebook = open('notebook.txt', 'r+')
level1 = open('levels.txt', 'r')

print "Find the contents of the file ..."

def responseQ(res, level):
    for line in level:
        if res in line:
            print line
            notebook.write(line)
    print "You should save this information to your notebook."

def show_notes():
    print 'cat notebook.txt'

responseQ(response, level1)

print "We're done here."
notebook.close()
