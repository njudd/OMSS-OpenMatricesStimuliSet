import raven_gen
from raven_gen import Matrix, MatrixType, Ruleset, RuleType
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np

#raven_gen.attribute.SIZE_VALUES; #raven_gen.attribute.COLOR_VALUES

raven_gen.attribute.SIZE_VALUES = (.3, .5, .7, .9) # maybe do 4? .25, .5, .75 1
raven_gen.attribute.SIZE_MAX = 3 # need to tell it the length of the new vector when it changes


### Naming of stimuli
# The ordering matters; this is for saving and not naming because Py doesn’t like the dot
#
# R = rule; P = Problem
## cl = color, sh = shape, sz = size, num = number, pos = position (all = all, r = rest)
### C = constant; P = progression; A = arithmetic; D = dist3
#
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

R1c = Ruleset(size_rules=[RuleType.CONSTANT],
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

R2c = Ruleset(size_rules=[RuleType.PROGRESSION], # R2_szP_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.DISTRIBUTE_THREE],
                  position_rules=[RuleType.CONSTANT])

R2a = Ruleset(size_rules=[RuleType.PROGRESSION], # R2_szP_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.DISTRIBUTE_THREE],
                  position_rules=[RuleType.CONSTANT])

R3 = Ruleset(size_rules=[RuleType.DISTRIBUTE_THREE], # R3_szD_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])

R3c = Ruleset(size_rules=[RuleType.DISTRIBUTE_THREE], # R3_szD_rC
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

R4c = Ruleset(size_rules=[RuleType.ARITHMETIC], # R4_szA_rC
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

R5c = Ruleset(size_rules=[RuleType.CONSTANT], # R5_shP_rC
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

R6c = Ruleset(size_rules=[RuleType.CONSTANT], # R6_shD_rC
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])

R6a = Ruleset(size_rules=[RuleType.CONSTANT], # R6_shD_rC
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])


######## Take 2 on rules
# since number & position are so linked we will generate with them both the same

# this should stop rotation noise, but it seems to not???
raven_gen.attribute.UNI_VALUES = (True, True, False, False)
raven_gen.attribute.UNI_MIN = 0
raven_gen.attribute.UNI_MAX = len(raven_gen.attribute.UNI_VALUES) - 1




R7_numP_posP_rC = Ruleset(size_rules=[RuleType.CONSTANT], # R7_numP_posP_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
                  number_rules=[RuleType.PROGRESSION], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.PROGRESSION])

R7_numD_posD_rC = Ruleset(size_rules=[RuleType.CONSTANT], # R7_numD_posD_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
                  number_rules=[RuleType.DISTRIBUTE_THREE], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.DISTRIBUTE_THREE])

R7_numA_posA_rC = Ruleset(size_rules=[RuleType.CONSTANT], # R7_numA_posA_rC
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
                  number_rules=[RuleType.ARITHMETIC], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.ARITHMETIC])






######## ^^^^^are these okay...?




#####
# these rules are problematic, I think because you are trying to change
# number and position independently (which doesn't work)
# could try making them both the same rule?

# R8_numD_rC = Ruleset(size_rules=[RuleType.CONSTANT],
#                   shape_rules=[RuleType.CONSTANT],
#                   color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
#                   number_rules=[RuleType.DISTRIBUTE_THREE], # if you only do single stimulis this isn't an issue
#                   position_rules=[RuleType.CONSTANT])
#
# R9_numA_rC = Ruleset(size_rules=[RuleType.CONSTANT],
#                   shape_rules=[RuleType.CONSTANT],
#                   color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
#                   number_rules=[RuleType.ARITHMETIC], # if you only do single stimulis this isn't an issue
#                   position_rules=[RuleType.CONSTANT])
#
# R10 = Ruleset(size_rules=[RuleType.CONSTANT],
#                   shape_rules=[RuleType.CONSTANT],
#                   color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
#                   number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
#                   position_rules=[RuleType.PROGRESSION])
#
# R11 = Ruleset(size_rules=[RuleType.CONSTANT],
#                   shape_rules=[RuleType.CONSTANT],
#                   color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
#                   number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
#                   position_rules=[RuleType.DISTRIBUTE_THREE])




##### new rules
# not sure if these are good
# SEE NOTES!!!


Rn1c = Ruleset(size_rules=[RuleType.PROGRESSION], # R6_shD_rC
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])

Rn1a = Ruleset(size_rules=[RuleType.PROGRESSION], # R6_shD_rC
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])

Rn2c = Ruleset(size_rules=[RuleType.ARITHMETIC], # R6_shD_rC
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])

Rn2a = Ruleset(size_rules=[RuleType.ARITHMETIC], # R6_shD_rC
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])





ruleset_13_mix_numArith_shapeProg = Ruleset(number_rules=[RuleType.ARITHMETIC],
                                             shape_rules=[RuleType.PROGRESSION])




# using dicts instead of lists https://stackoverflow.com/questions/4326658/how-to-index-into-a-dictionary
# rules = {'R1_allC':R1,'R2_szP_rC':R2, 'R3_szD_rC':R3, 'R1_clD_rC':R1c,'R2_szP_clD_rC':R2c, 'R3_szD_clD_rC':R3c,# first_key = list(rules)[0] # first_val = list(rules.values())[0]
#          'R4_szA_rC':R4, 'R5_shP_rC':R5, 'R6_shD_rC':R6, 'R4_szA_clD_rC':R4c, 'R5_shP_clD_rC':R5c, 'R6_shD_clD_rC':R6c}


rules = {'R1_clA_rC':R1a,'R2_szP_clA_rC':R2a, 'R3_szD_clA_rC':R3a,# first_key = list(rules)[0] # first_val = list(rules.values())[0]
         'R4_szA_clA_rC':R4a, 'R5_shP_clA_rC':R5a, 'R6_shD_clA_rC':R6a}


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
                  number_rules=[RuleType.CONSTANT],
                  position_rules=[RuleType.CONSTANT])

rules = {'R6_shD_clD_rC':R6}

rpm = Matrix.make(list(MatrixType)[2], ruleset=R6, n_alternatives=7)

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



# to do; try these all rules with color progression (makes no sense)

# os.chdir('/Users/njudd/surfdrive/Shared/ravenStim/rpm_take2')


# layout_list = {"L1":0, "L2":1,"L3":2}
# layout_list = {"L1":0}

# layout_list = {"L2":1,"L3":2}

os.chdir("/Users/njudd/Desktop/temp/")
for ll in range(len(layout_list)): # ll = layout loop index
    os.mkdir("Layout_" + list(layout_list)[ll])
    os.chdir("Layout_" + list(layout_list)[ll])
    # now go over the vector of rules
    for w in range(len(rules)):
        os.mkdir("rpm" + list(rules)[w])
        os.chdir("rpm" + list(rules)[w])
        # now make a certian number of problems
        stim_tries = 10
        while stim_tries != 0:
            loopname = ("rpm" + list(rules)[w])
            loopname += ("_P" + str(stim_tries))  # plus one to get rid of Python indexing

            rpm = "starting empty"
            try:
                rpm = Matrix.make(list(MatrixType)[list(layout_list.values())[ll]], ruleset=list(rules.values())[w], n_alternatives=7)
            except:
                pass

            if type(rpm) != str:
                os.mkdir(loopname)  # making a dir for the rpm stuff
                probname = (list(layout_list)[ll] + loopname)  # making the problem name start with the type of layout
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



# with 3 alternatives it seems fine but with 5 it starts fucking up around 2nd layout
# it seems like with more alternatives this rare bug pops up

# this one is very much a bitch
# THE ERROR COMES UP A LOT
# ct = Matrix.make(list(MatrixType)[1], ruleset=R9_numA_rC, n_alternatives=1)
# ct.gimme()
# plt.imshow(ct.ans_img, cmap='gray')
# plt.show()






##### go into the rabbit hole of position = NA.




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



