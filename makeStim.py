# Nicholas Judd
# 20230702
# njudd.com
import raven_gen
import raven_gen.attribute
from raven_gen import Matrix, MatrixType, RuleType
import matplotlib.pyplot as plt
from PIL import Image
import random
import numpy as np

#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
#  print(x)


raven_gen.attribute.SIZE_VALUES = (.4, .65, .9)
raven_gen.attribute.SIZE_MAX = 2

raven_gen.attribute.SIZE_MAX

ruleset1 = Ruleset(size_rules=[RuleType.PROGRESSION])
random.seed(55)
simpleRPM = Matrix.make(list(MatrixType)[2], n_alternatives = 0)
simpleRPM.gimme()
plt.plot(Image.fromarray(simpleRPM.ans_img), cmap='gray')

#plt.imshow(Image.fromarray(simpleRPM.ans_img), cmap='gray')
plt.savefig('~/Desktop/ct.png')





