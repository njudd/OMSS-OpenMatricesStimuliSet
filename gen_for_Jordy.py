import raven_gen
from raven_gen import Matrix, MatrixType, Ruleset, RuleType
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np


#raven_gen.attribute.SIZE_VALUES
#raven_gen.attribute.COLOR_VALUES

raven_gen.attribute.SIZE_VALUES = (.4, .65, .9)
raven_gen.attribute.SIZE_MAX = 2

ruleset1 = Ruleset(size_rules=[RuleType.CONSTANT])
#PROGRESSION


ruleset = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.DISTRIBUTE_THREE],
                  position_rules=[RuleType.CONSTANT])


#ruleset = Ruleset(size_rules=[RuleType.CONSTANT, RuleType.PROGRESSION], shape_rules=list(RuleType))
rpm = Matrix.make(list(MatrixType)[2], ruleset=ruleset, n_alternatives=3)

#simpleRPM = Matrix.make(list(MatrixType)[2], n_alternatives = 0, ruleset=ruleset2)

os.getcwd()
os.chdir('/Users/njudd/Desktop')
rpm.save(".", "test")

# only doing gimme so I can take a look at it without saving
#rpm.gimme()
#plt.imshow(Image.fromarray(rpm.ans_img), cmap='gray')
#plt.axis('off')
#plt.show()
print(rpm.rules)
#print(rpm)
