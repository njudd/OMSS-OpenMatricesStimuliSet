import raven_gen
from raven_gen import Matrix, MatrixType, Ruleset, RuleType
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np


#raven_gen.attribute.SIZE_VALUES
#raven_gen.attribute.COLOR_VALUES

raven_gen.attribute.SIZE_VALUES = (.3, .5, .7, .9)
raven_gen.attribute.SIZE_MAX = 3 # need to tell it the length of the new vector when it changes
# maybe do 4? .25, .5, .75 1
# idk what ever is sensible

# also maybe less colors?

# Where is the noise attribute can you chanage that?
# with "rulset" it will just pick four rules at random; not ideal behaviour?

#ruleset = Ruleset(size_rules=[RuleType.CONSTANT, RuleType.PROGRESSION], shape_rules=list(RuleType))


# I would fool around up the alternatives count;
# The alternatives by definition don't follow the rule set; so you might have to figure out a way to make reasonable(ish) alternatives?

#simpleRPM = Matrix.make(list(MatrixType)[2], n_alternatives = 0, ruleset=ruleset2)


# all constant
ruleset_1 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_2 = Ruleset(size_rules=[RuleType.PROGRESSION],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_3 = Ruleset(size_rules=[RuleType.DISTRIBUTE_THREE],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_4 = Ruleset(size_rules=[RuleType.ARITHMETIC],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_5 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.PROGRESSION],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_6 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_7 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.ARITHMETIC],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_8 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.PROGRESSION],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_9 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.DISTRIBUTE_THREE],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_10 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

# two sets with two changes
ruleset_11 = Ruleset(size_rules=[RuleType.PROGRESSION],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_12 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.ARITHMETIC],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

rules = [ruleset_1, ruleset_2, ruleset_3, ruleset_4, ruleset_5,
         ruleset_6, ruleset_8, ruleset_9, ruleset_10,
         ruleset_11, ruleset_12]


# because its only single pieces (i.e., list(MatrixType)[0])
# you can't change position

os.getcwd()
os.chdir('/Users/njudd/surfdrive/Shared/ravenStim/rpms')
for w in range(len(rules)):
    os.mkdir("rpm_rule" + str(w))
    os.chdir("rpm_rule" + str(w))
    #print(w)
    for i in range(10):
        loopname = "rpm_ct_"
        loopname += str(i)
        #print("innerloop")
        #print(i)
        rpm = Matrix.make(list(MatrixType)[0], ruleset=rules[w], n_alternatives=3)
        os.mkdir(loopname)  # making a dir for the rpm stuff
        rpm.save(loopname + "/.", loopname)  # going in that dir, also naming the stimuli by the loopname

        with open(loopname + "/" + loopname + "output.txt",
                  "a") as f:  # going into the folder and making an output per item
            print(rpm.rules, file=f)

        with open("Global_output.txt", "a") as f:  # going into the folder and making an output per item
            print(rpm.rules, file=f)
    os.chdir("..")

    # barf rules
    with open("Global_rules.txt", "a") as f:  # going into the folder and making an output per item
        print(rules[w], file=f)


os.getcwd()


os.chdir("/Users/njudd/Desktop/rpms_100rand")
# just making 100 randomly sampled
for i in range(100):
    loopname = "rpm_ct_"
    loopname += str(i)
    # print("innerloop")
    # print(i)
    rpm = Matrix.make(list(MatrixType)[0], n_alternatives=3)
    os.mkdir(loopname)  # making a dir for the rpm stuff
    rpm.save(loopname + "/.", loopname)  # going in that dir, also naming the stimuli by the loopname

    with open(loopname + "/" + loopname + "output.txt",
              "a") as f:  # going into the folder and making an output per item
        print(rpm.rules, file=f)

    with open("Global_output.txt", "a") as f:  # going into the folder and making an output per item
        print(rpm.rules, file=f)





# maybe make a panda's dataframe of the rules as well?


# only doing gimme so I can take a look at it without saving
#rpm.gimme()
#plt.imshow(Image.fromarray(rpm.ans_img), cmap='gray')
#plt.axis('off')
#plt.show()
print(rpm.rules)
#print(rpm)

with open("output.txt", "a") as f: # a is for append
  print("start")
  print(rpm.rules, file=f)
  print("end")




