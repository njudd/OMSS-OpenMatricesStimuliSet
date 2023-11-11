# STILL useful as it shows some of the earlier raw code to go from numeric values to an actual plot
# here I am making some example tasks

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


PROGRESSION


ruleset = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.DISTRIBUTE_THREE],
                  position_rules=[RuleType.CONSTANT])


#ruleset = Ruleset(size_rules=[RuleType.CONSTANT, RuleType.PROGRESSION], shape_rules=list(RuleType))
rpm = Matrix.make(list(MatrixType)[2], ruleset=ruleset)

#simpleRPM = Matrix.make(list(MatrixType)[2], n_alternatives = 0, ruleset=ruleset2)

os.getcwd()
#rpm.save(".", "Hmmmm")
rpm.gimme()
plt.imshow(Image.fromarray(rpm.ans_img), cmap='gray')
plt.axis('off')
plt.show()
print(rpm.rules) #print(rpm)

# rename to recolor()



# Make default def save in 750








random.seed(42)
os.chdir('/Users/njudd/Desktop/matrix_stim/bw_hold/')

list(RuleType)

raven_gen.attribute.COLOR_VALUES = (224, 168, 112, 56, 28)
raven_gen.attribute.COLOR_MAX = len(raven_gen.attribute.COLOR_VALUES) - 1

ruleset = Ruleset(size_rules=[RuleType.PROGRESSION],
                  shape_rules=[RuleType.PROGRESSION],
                  color_rules=[RuleType.PROGRESSION],
                  number_rules=[RuleType.PROGRESSION],
                  position_rules=[RuleType.PROGRESSION])
ruleset1 = Ruleset(size_rules=[RuleType.PROGRESSION])

# random.seed(55)
simpleRPM_1 = Matrix.make(list(MatrixType)[2], n_alternatives = 3)
#simpleRPM_1.save(".", "_test", image_size = 750)
simpleRPM_1.gimme()
print(simpleRPM_1)

plt.imshow(Image.fromarray(simpleRPM_1.ans_img), cmap='gray')
plt.grid(False)
plt.axis('off')
plt.show()

plt.imshow(Image.fromarray(simpleRPM_1.ans_img[325:,325:]), cmap='gray')
plt.grid(False)
plt.axis('off')
plt.show()


random.seed(69)
simpleRPM_2 = Matrix.make(list(MatrixType)[0], n_alternatives = 3, ruleset=ruleset)
simpleRPM_2.save(".", "_2", image_size = 750)
random.seed(44)
simpleRPM_3 = Matrix.make(list(MatrixType)[0], n_alternatives = 3, ruleset=ruleset)
simpleRPM_3.save(".", "_3", image_size = 750)



random.seed(55)
simpleRPM_1 = Matrix.make(list(MatrixType)[2], n_alternatives = 0)
#simpleRPM_1.save(".", "_test", image_size = 750)
simpleRPM_1.gimme()

simpleRPM_1_bgr = simpleRPM_1.ans_img[325:, 325:]
plt.imshow(Image.fromarray(simpleRPM_1_bgr), cmap='gray')
plt.show()

simpleRPM_1_bgr[120:130,120:130]
simpleRPM_1_bgr = np.repeat(simpleRPM_1_bgr[:, :, np.newaxis], 3, axis=2)
simpleRPM_1_bgr[120:130,120:130]


plt.imshow(Image.fromarray(simpleRPM_1_bgr), cmap='gray')
plt.show()






M = simpleRPM_1_bgr[simpleRPM_1_bgr == [168,168,168]].shape[0]/3
M = int(M) # need to be an int
simpleRPM_1_bgr[simpleRPM_1_bgr == [168,168,168]] = [40,114,247]*M

simpleRPM_1_bgr[120:130,120:130]


plt.imshow(Image.fromarray(simpleRPM_1_bgr), cmap='gray')
plt.show()


# tring on the whole image targeting 168

whole_img = simpleRPM_1.ans_img
#step 1 make multiply into colors values (three's)
whole_img = np.repeat(whole_img[:, :, np.newaxis], 3, axis=2)

# step 2; target and change the values
M = int(whole_img[whole_img == [168,168,168]].shape[0]/3)
whole_img[whole_img == [168,168,168]] = [40,114,247]*M

plt.imshow(Image.fromarray(whole_img), cmap='gray')
plt.show()



# 224, (255, 235, 59)
# 196, (251, 140, 0)
# 168, (211, 47, 47)
# 140, (186, 104, 200)
# 112, (30, 136, 229)
# 84, (0, 188, 212)
# 56, (56, 142, 60)
# 28, (46, 204, 113)


color_ans = recolor(simpleRPM_1.ans_img)






raven_gen.attribute.COLOR_VALUES = (224, 168, 112, 56, 28)














# make a function that takes the gray scale values and changes it











#plt.imshow(Image.fromarray(simpleRPM_1_bgr), cmap='gray')
#plt.show()
np.unique(simpleRPM_1_bgr)
#simpleRPM_1_bgr[100,][55:66]

M = simpleRPM_1_bgr[simpleRPM_1_bgr == [140,140,140]].shape[0]/3
M = int(M) # need to be an int
simpleRPM_1_bgr[simpleRPM_1_bgr == [140,140,140]] = [40,114,247]*M


M2 = simpleRPM_1_bgr[simpleRPM_1_bgr == [196,196,196]].shape[0]/3
M2 = int(M2) # need to be an int
simpleRPM_1_bgr[simpleRPM_1_bgr == [196,196,196]] = [40,52,244]*M2


M3 = simpleRPM_1_bgr[simpleRPM_1_bgr == [84,84,84]].shape[0]/3
M3 = int(M3) # need to be an int
simpleRPM_1_bgr[simpleRPM_1_bgr == [84,84,84]] = [40,255,244]*M3

plt.imshow(Image.fromarray(simpleRPM_1_bgr), cmap='gray')
plt.show()



M4 = simpleRPM_1_bgr[simpleRPM_1_bgr == [112,112,112]].shape[0]/3
M4 = int(M4) # need to be an int
simpleRPM_1_bgr[simpleRPM_1_bgr == [112,112,112]] = [247,200,40]*M4

M5 = simpleRPM_1_bgr[simpleRPM_1_bgr == [168,168,168]].shape[0]/3
M5 = int(M5) # need to be an int
simpleRPM_1_bgr[simpleRPM_1_bgr == [168,168,168]] = [247,40,235]*M5

plt.imshow(cv2.cvtColor(simpleRPM_1_bgr, cv2.COLOR_BGR2RGB)) #
plt.show()

raven_gen.attribute.COLOR_VALUES




np.unique(simpleRPM_1.ans_ImageNum)

simpleRPM_1.ans_Imagenum
