import raven_gen
from raven_gen import Matrix, MatrixType, Ruleset, RuleType
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np

#raven_gen.attribute.SIZE_VALUES; #raven_gen.attribute.COLOR_VALUES

# raven_gen.attribute.SIZE_VALUES = (.3, .5, .7, .9) # maybe do 4? .25, .5, .75 1
raven_gen.attribute.SIZE_VALUES = (.20, .45, .70, .95) # for layout 2 & 3 (4 stimuli)
raven_gen.attribute.SIZE_MAX = 3 # need to tell it the length of the new vector when it changes




### Naming of stimuli
#
# R = rule; P = Problem
## cl = color, sh = shape, sz = size, num = number, pos = position (all = all, r = rest)
### C = constant; P = progression; A = arithmetic; D = dist3
#
# the color is arithmetic (i.e., clA) this means color is noise
# Example:
# R4_aSZ_cR_P1_alternative2 (rule 1, arithmetic size, constant rest, Problem 1, Alternative 2)

#### There is a google doc called "MatrixStimuliNotes" as well

# Where is the noise attribute can you chanage that?
# ^^^ you can't making noise is possible (specifically by adding a rule in rule.py)
# yet... making alternatives with noise would require entirely different logic,
# because right now all of the alternatives "work"; so they can be subsitutited
# yet with noise, you can't pick another rule of the atribute (as the rule is NO rule)
#
# with "rulset" it will just pick four rules at random; not ideal behaviour?
# ^^^ this does not happen; the thing is 'number' and 'position' are linked they form 'configuration'

# ^ this only happens with list(MatrixType)[0] on the others it lists "position" and "num"

# while the others (color, sizzze, shape) are a different class (see the SI of paper)
# therefore the function does not allow non-constant rules to occur on both of the attributes
#
# Also importantly they exclude the arthmetic rule on Type, since it makes no sense
# since our function is no using color this is also the case with color (gray scale can increment)
# we have not yet hardcoded the function to not allow it; also distribute 3 is very hard in color
#
# I would fool around up the alternatives count;
# The alternatives by definition don't follow the rule set;
# so you might have to figure out a way to make reasonable(ish) alternatives?
# ^^^ we have decided to make 8 and manually pick 3; this is something we should expand if we get the OSF grant



# all constant
R1 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])
R1d = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])
R1a = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])


R2 = Ruleset(size_rules=[RuleType.PROGRESSION], # R2_szP_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R2d = Ruleset(size_rules=[RuleType.PROGRESSION], # R2_szP_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R2a = Ruleset(size_rules=[RuleType.PROGRESSION], # R2_szP_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])

R3 = Ruleset(size_rules=[RuleType.DISTRIBUTE_THREE], # R3_szD_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R3d = Ruleset(size_rules=[RuleType.DISTRIBUTE_THREE], # R3_szD_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R3a = Ruleset(size_rules=[RuleType.DISTRIBUTE_THREE], # R3_szD_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])


R4 = Ruleset(size_rules=[RuleType.ARITHMETIC], # R4_szA_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R4d = Ruleset(size_rules=[RuleType.ARITHMETIC], # R4_szA_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R4a = Ruleset(size_rules=[RuleType.ARITHMETIC], # R4_szA_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])


R5 = Ruleset(size_rules=[RuleType.CONSTANT], # R5_shP_rC
                  shape_rules=[RuleType.PROGRESSION],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R5d = Ruleset(size_rules=[RuleType.CONSTANT], # R5_shP_rC
                  shape_rules=[RuleType.PROGRESSION],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R5a = Ruleset(size_rules=[RuleType.CONSTANT], # R5_shP_rC
                  shape_rules=[RuleType.PROGRESSION],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])


R6 = Ruleset(size_rules=[RuleType.CONSTANT], # R6_shD_rC
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R6d = Ruleset(size_rules=[RuleType.CONSTANT], # R6_shD_rC
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R6a = Ruleset(size_rules=[RuleType.CONSTANT], # R6_shD_rC
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])

rules1 = {'R1_clD_rC':R1d,'R2_szP_clD_rC':R2d, 'R3_szD_clD_rC':R3d, 'R4_szA_clD_rC':R4d, 'R5_shP_clD_rC':R5d, 'R6_shD_clD_rC':R6d,
          'R1_clA_rC':R1a,'R2_szP_clA_rC':R2a, 'R3_szD_clA_rC':R3a, 'R4_szA_clA_rC':R4a, 'R5_shP_clA_rC':R5a, 'R6_shD_clA_rC':R6a}

#### rules for layouts 2 & 3

# I think these will work for layout 1 as well!
R7d = Ruleset(size_rules=[RuleType.PROGRESSION], # R7_szP_shD
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R7a = Ruleset(size_rules=[RuleType.PROGRESSION],
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])


R8d = Ruleset(size_rules=[RuleType.ARITHMETIC], # R8_szA_shD
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])
R8a = Ruleset(size_rules=[RuleType.ARITHMETIC],
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])

rules2 = {'R7_szP_shD_clD_rA':R7d,'R7_szP_shD_clA_rA':R7a,
          'R8_szA_shD_clD_rA':R8d, 'R8_szA_shD_clA_rA':R8a}


# rules with number and position yet matching
R9d = Ruleset(size_rules=[RuleType.CONSTANT], # R9_numP_posP
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.PROGRESSION],
                  position_rules=[RuleType.PROGRESSION])
R9a = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.PROGRESSION],
                  position_rules=[RuleType.PROGRESSION])


R10d = Ruleset(size_rules=[RuleType.CONSTANT], # R10_numD_posD
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.DISTRIBUTE_THREE],
                  position_rules=[RuleType.DISTRIBUTE_THREE])
R10a = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.DISTRIBUTE_THREE],
                  position_rules=[RuleType.DISTRIBUTE_THREE])


R11d = Ruleset(size_rules=[RuleType.CONSTANT], # R11_numA_posA
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.ARITHMETIC],
                  position_rules=[RuleType.ARITHMETIC])
R11a = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.ARITHMETIC],
                  position_rules=[RuleType.ARITHMETIC])

# now making it harder by messing with size & shape as well
# inspired by rules R7 & R8

R12a = Ruleset(size_rules=[RuleType.PROGRESSION],
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.PROGRESSION],
                  position_rules=[RuleType.PROGRESSION])
R13a = Ruleset(size_rules=[RuleType.ARITHMETIC],
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.PROGRESSION],
                  position_rules=[RuleType.PROGRESSION])



rules3 = {'R9_xP_clD':R9d, 'R9_xP_clA':R9a,
          'R10_xD_clD':R10d, 'R10_xD_clA':R10a,
          'R11_xA_clD':R11d, 'R11_xA_clA':R11a,
          'R12_xP_szP_shD_clA':R12a,
          'R13_xP_szA_sh_D_clA':R13a}

# rules with number and position matching plus dist 3 size & shape



##### new rules
# not sure if these are good
# SEE NOTES!!!

ruleset_13_mix_numArith_shapeProg = Ruleset(number_rules=[RuleType.ARITHMETIC],
                                             shape_rules=[RuleType.PROGRESSION])




# using dicts instead of lists https://stackoverflow.com/questions/4326658/how-to-index-into-a-dictionary
# rules = {'R1_allC':R1,'R2_szP_rC':R2, 'R3_szD_rC':R3, 'R1_clD_rC':R1d,'R2_szP_clD_rC':R2d, 'R3_szD_clD_rC':R3d,# first_key = list(rules)[0] # first_val = list(rules.values())[0]
#          'R4_szA_rC':R4, 'R5_shP_rC':R5, 'R6_shD_rC':R6, 'R4_szA_clD_rC':R4d, 'R5_shP_clD_rC':R5d, 'R6_shD_clD_rC':R6d}




# good new rules (add arth color as noise)

# color dist 3 with other rules???

# color dist 3 constant
# color dist 3 shape dist 3
# color dist 3 with num

# size arth & shap progression
# num arth & size arth

# type, size and color DIST 3
# type, size and color DIST 3 with postiion arithmetic (this is good also number arth)


# maybe have SHAPE as progression to make noise (or make shapes harder)

import raven_gen
from raven_gen import Matrix, MatrixType, Ruleset, RuleType
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np

R6 = Ruleset(size_rules=[RuleType.CONSTANT], # R6_shD_rC
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.DISTRIBUTE_THREE],
                  position_rules=[RuleType.DISTRIBUTE_THREE])

rules = {'R6_shD_clD_rC':R6}

rpm = Matrix.make(list(MatrixType)[2], ruleset=R6, n_alternatives=7)
print("POSITION" in str(rpm.rules.components_rules[0]))
print("NUMBER" in str(rpm.rules.components_rules[0]))

# progression & ARTH doesn't make senes for color



# os.getcwd()
# os.chdir('/Users/njudd/surfdrive/Shared/ravenStim/rpms_new_CT')

# I could do a for look with 3 but I want different rule sets so I will just hardcode
# os.mkdir('/Users/njudd/surfdrive/Shared/ravenStim/rpms_new_CT/layout1')
# os.chdir('/Users/njudd/surfdrive/Shared/ravenStim/rpms_new_CT/layout1')

# this should stop rotation noise
# raven_gen.attribute.UNI_VALUES = (False, False, False)
# raven_gen.attribute.UNI_MIN = 0
# raven_gen.attribute.UNI_MAX = len(raven_gen.attribute.UNI_VALUES) - 1


# Okay I made all the sims rules 1-6 in layout 1
# I than made R7 & 8 in Layout 1
# plus rules 7-13 in layout's 2 & 3

# we decided that rules 1, 4 & 5 would be good in layout's 2 & 3
# I decided that R2d, would be good & chanced the size attributes to reflect this

missed_rulesLAYOUTS23 = {'R1_rC':R1, 'R1_clD_rC':R1d, 'R1_clA_rC':R1a,
                         'R2_szP_clD_rC':R2d,
                         'R4_szA_clA_rC':R4a,
                         'R5_shP_clA_rC':R5a}
# we also noticed there is no rule that is shape progression & size progression
# so I will do that with layout's 1,2 & 3

# R14a = Ruleset(size_rules=[RuleType.PROGRESSION],
#                   shape_rules=[RuleType.PROGRESSION],
#                   color_rules=[RuleType.ARITHMETIC],
#                   number_rules=[RuleType.CONSTANT],
#                   position_rules=[RuleType.CONSTANT])



# os.chdir('/Users/njudd/surfdrive/Shared/ravenStim/rpm_take2')


# layout_list = {"L1":0, "L2":1,"L3":2}
# layout_list = {"L1":0}

# rules = {}
# rules = {**rules1, **rules2} #omfg python 3.5 ftw!!
# rules = missed_rulesLAYOUTS23
# rules = {'R14_szP_shP_clA_rC':R14a}

layout_list = {"L2":1,"L3":2}

rules = missed_rulesLAYOUTS23

os.chdir("/Users/njudd/surfdrive/Shared/ravenStim/rpm_take2/")

os.chdir("/Users/njudd/Desktop/temp")
for ll in range(len(layout_list)): # ll = layout loop index
    os.mkdir("Layout_" + list(layout_list)[ll])
    os.chdir("Layout_" + list(layout_list)[ll])
    # now go over the vector of rules
    for w in range(len(rules)):
        os.mkdir("rpm" + list(rules)[w])
        os.chdir("rpm" + list(rules)[w])
        # now make a certian number of problems
        stim_tries = 20
        while stim_tries != 0:
            loopname = ("rpm" + list(rules)[w])
            loopname += ("_P" + str(stim_tries))  # plus one to get rid of Python indexing

            rpm = "starting empty"
            try:
                rpm = Matrix.make(list(MatrixType)[list(layout_list.values())[ll]], ruleset=list(rules.values())[w], n_alternatives=7)
            except:
                pass

            if type(rpm) != str:
                loopname = list(layout_list)[ll] + loopname
                os.mkdir(loopname)  # making a dir for the rpm problem stuff
                probname = loopname  # making the problem name start with the type of layout
                rpm.save(loopname + "/.", probname)  # going in that dir, also naming the stimuli by the loopname

                with open(loopname + "/" + probname + "_output.txt",
                          "a") as f:  # going into the folder and making an output per item
                    print(rpm.rules, file=f)

                with open("Global_output.txt", "a") as f:  # going into the folder and making an output per item
                    print(rpm.rules, file=f)
                stim_tries -= 1
            else:
                print("this is an error")
        os.chdir("..")

        # barf rules
        with open("Global_rules.txt", "a") as f:  # going into the folder and making an output per item
            print(list(rules)[w], file=f)

    os.chdir("..")


###########                                             ###########
###########  Making sure it chooses POSITION or NUMBER  ###########
###########                                             ###########


# so I want to do the rules times 2; so I end up with R9_numP & R9_posP
# using rules3

layout_list = {"L2":1,"L3":2}
os.chdir("/Users/njudd/Desktop/temp/")
for ll in range(len(layout_list)): # ll = layout loop index
    os.mkdir("Layout_" + list(layout_list)[ll])
    os.chdir("Layout_" + list(layout_list)[ll])
    # now go over the vector of rules
    for w in range(len(rules3)):
        os.mkdir("rpm" + list(rules3)[w])
        os.chdir("rpm" + list(rules3)[w])
        stim_triesPOS = 10
        stim_triesNUM = 10
        # now make a certian number of problems

        counter = stim_triesPOS + stim_triesNUM
        while counter > 0:
            # get around the error
            rpm = "starting empty"
            try:
                rpm = Matrix.make(list(MatrixType)[list(layout_list.values())[ll]],
                                  ruleset=list(rules3.values())[w], n_alternatives=7)
            except:
                pass

            if type(rpm) != str: # if it is actually a rpm obj
                if "POSITION" in str(rpm.rules.components_rules[0]) and stim_triesPOS > 0:
                    loopname = ("rpm" + list(rules3)[w] + "_xPOS")
                    loopname += ("_P" + str(stim_triesPOS))  # plus one to get rid of Python indexing
                    os.mkdir(loopname)  # making a dir for the rpm stuff
                    probname = (list(layout_list)[ll] + loopname)  # making the problem name start with the type of layout
                    rpm.save(loopname + "/.", probname)  # going in that dir, also naming the stimuli by the loopname

                    with open(loopname + "/" + probname + "_output.txt",
                                "a") as f:  # going into the folder and making an output per item
                        print(rpm.rules, file=f)

                    with open("Global_output.txt", "a") as f:  # going into the folder and making an output per item
                        print(rpm.rules, file=f)
                    stim_triesPOS -= 1
                elif "NUMBER" in str(rpm.rules.components_rules[0]) and stim_triesNUM > 0:
                    loopname = ("rpm" + list(rules3)[w] + "_xNUM")
                    loopname += ("_P" + str(stim_triesNUM))  # plus one to get rid of Python indexing
                    os.mkdir(loopname)  # making a dir for the rpm stuff
                    probname = (list(layout_list)[ll] + loopname)  # making the problem name start with the type of layout
                    rpm.save(loopname + "/.", probname)  # going in that dir, also naming the stimuli by the loopname

                    with open(loopname + "/" + probname + "_output.txt",
                            "a") as f:  # going into the folder and making an output per item
                        print(rpm.rules, file=f)

                    with open("Global_output.txt", "a") as f:  # going into the folder and making an output per item
                        print(rpm.rules, file=f)
                    stim_triesNUM -= 1
                else:
                    print("needing more of one type")
            else:
                print("this is an error")
            counter = stim_triesPOS + stim_triesNUM
        os.chdir("..")  # going back in rules dir
        # barf rules
        with open("Global_rules.txt", "a") as f:  # going into the folder and making an output per item
            print(list(rules3)[w], file=f)

    os.chdir("..") # going back in layout dir

###########                         ###########
########### known issues!!!!!!!!!!  ###########
###########                         ###########

########### 1
# the biggest is when you try to make more than alternative>3 the function just breaks
# I beleive this is becausae of an error when itterating thru alternatives
# yet the whole handingly of alternatives is subpar and not 'human' friendly

# Example code
# with 3 alternatives it seems fine but with 5 it starts fucking up around 2nd layout
# it seems like with more alternatives this rare bug pops up

# this one is very much a bitch
# THE ERROR COMES UP A LOT
# ct = Matrix.make(list(MatrixType)[1], ruleset=R9_numA_rC, n_alternatives=1)
# ct.gimme()
# plt.imshow(ct.ans_img, cmap='gray')
# plt.show()

########### 2

# this should stop rotation noise, but it seems to not???
# raven_gen.attribute.UNI_VALUES = (True, True, False, False)
# raven_gen.attribute.UNI_MIN = 0
# raven_gen.attribute.UNI_MAX = len(raven_gen.attribute.UNI_VALUES) - 1

########### 3

# it doesn't seem posible to feed NA's to the rules arguemnt
# color, size and type need to have one always...
# yet it would be nice functionality to have an arg like num = T or pos = T which gives that rules
# similar to the look I make to catch them




# now you can make another one just for the rules you don't use in all layouts


# list(rules.values())[4] possibly because there are less than 8 shapes with the alternatives
# has no issue when you generate 3 alternatives
# this is partially off (the num of alts matter but not rules?); the patter is list(MatrixType)[1] and it seems a bit random
# happens in earlier rules if I up the num of stimuli I make

### it is not size, seems also to not be uni_values...


# so generating 8 doesn't work for
testing_rules = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.ARITHMETIC],
                  color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])
ct = Matrix.make(list(MatrixType)[1], ruleset=R1, n_alternatives=3)
ct.save(".", "ct.png")
#
# ct.gimme()
# plt.imshow(ct.ans_img, cmap='gray')
# plt.show()


# line 96 in attribute.py
import raven_gen
from raven_gen import Matrix, MatrixType, Ruleset, RuleType
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np
ct = Matrix.make(list(MatrixType)[0], n_alternatives=0)
ct.gimme()
plt.imshow(ct.ans_img, cmap='gray')
plt.show()


# ^^^ the error occasionally just comes up in this
# see if it happens on their clean version


# as you up the alternatives you run into a hardcore error...





# making an empty grid
ct = Matrix.make(list(MatrixType)[0], ruleset=list(rules.values())[0])
ct.save("/Users/njudd/Desktop/", "temp.png")
# col 1
ct.ans_img[5:245,5:245] = np.reshape([255] * 240**2 * 3,[int(240), int(240), 3])
ct.ans_img[5:245,255:495] = np.reshape([255] * 240**2 * 3,[int(240), int(240), 3])
ct.ans_img[5:245,505:745] = np.reshape([255] * 240**2 * 3,[int(240), int(240), 3])
# col 2
ct.ans_img[255:495,5:245] = np.reshape([255] * 240**2 * 3,[int(240), int(240), 3])
ct.ans_img[255:495,255:495] = np.reshape([255] * 240**2 * 3,[int(240), int(240), 3])
ct.ans_img[255:495,505:745] = np.reshape([255] * 240**2 * 3,[int(240), int(240), 3])
# col 3
ct.ans_img[505:745,5:245] = np.reshape([255] * 240**2 * 3,[int(240), int(240), 3])
ct.ans_img[505:745,255:495] = np.reshape([255] * 240**2 * 3,[int(240), int(240), 3])
ct.ans_img[505:745,505:745] = np.reshape([255] * 240**2 * 3,[int(240), int(240), 3])

ct.ans_img = Image.fromarray(ct.ans_img)

plt.imshow(ct.ans_img, cmap='gray')
plt.show()
ct.ans_img.save("/Users/njudd/Desktop/blankStim.png")



# maybe make a panda's dataframe of the rules as well?


# only doing gimme so I can take a look at it without saving
#rpm.gimme()
#plt.imshow(Image.fromarray(rpm.ans_img), cmap='gray')
#plt.axis('off')
#plt.show()
print(rpm.rules)
#print(rpm)



