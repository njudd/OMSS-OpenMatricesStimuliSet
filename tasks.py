from raven_gen import Matrix, MatrixType
import matplotlib.pyplot as plt
from PIL import Image
import random
import raven_gen
raven_gen.attribute.SIZE_VALUES
raven_gen.attribute.COLOR_VALUES
# constants are assumed to represent strictly increasing or decreasing sequences.
# If this assumption is violated rules may have an incoherent presentation.

random.seed(42)
simpleRPM = Matrix.make(list(MatrixType)[2], n_alternatives = 1)
simpleRPM.save(".", "simple", background_color=100)

# we have a new attribute on the saved object "self.ans_ImageNum"
# you can see I added this on matrix.py line 149
plt.imshow(Image.fromarray(simpleRPM.ans_ImageNum), cmap='gray')
plt.show()

##### ##### #####
# @Ann
# can you identify the possible vector to target white values & make them all red?
# you'll need to replicate everything into BGR values first
# note you might wanna go back to no background color for this








# ps here is the way to only get the 3-by-3 matricies
# 4 & 5 are not 6by6; 6 & 7 is possible to complicated for kids
options = list(MatrixType)[0:3] #limiting to 4 options
choice = np.random.choice(options) # lets grab a random choice
relevantRPM = Matrix.make(choice)
# or less verbosely
# rpm = Matrix.make(np.random.choice(list(MatrixType)[0:3])
relevantRPM.save(".", "append", background_color=130)



##### ##### #####
# @Maud
# can you check out matrix.py and somehow have the alternatives saving as well
# this is a harder task, you will need to save them seperately and you won't know how many
# potentially within the for loop use a string manipulation tools to name the alteratives (e.g., alt"_i")
# this is already a quite advanced task in R, ask if you need help!

# Note, you will need to save a variable as an evaluated class rather than a string.
# in R is is done with eval() and the bangbang oppertors