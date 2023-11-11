# OLD tasks for Maud & Ann... but I just did them in this sorted branch
# could be useful for when I want to look back later at what was changed




from raven_gen import Matrix, MatrixType
import matplotlib.pyplot as plt
from PIL import Image
import random
import raven_gen
import numpy as np

raven_gen.attribute.SIZE_VALUES
raven_gen.attribute.COLOR_VALUES
# constants are assumed to represent strictly increasing or decreasing sequences.
# If this assumption is violated rules may have an incoherent presentation.

random.seed(42)
simpleRPM = Matrix.make(list(MatrixType)[2], n_alternatives = 1)
simpleRPM.save(".", "simple", background_color=100)

# you have to call save for it to work; which is less than ideal

# we have a new attribute on the saved object "self.ans_ImageNum"
# you can see I added this on matrix.py line 149
plt.imshow(Image.fromarray(simpleRPM.ans_img), cmap='gray')
plt.show()



##### ##### #####
# @Ann
# can you identify the possible vector to target white values & make them all red?
# you'll need to replicate everything into BGR values first
# note you might wanna go back to no background color for this

ct = simpleRPM.ans_ImageNum
ct = np.repeat(ct[:, :, np.newaxis], 3, axis=2)
ct[ct == [0,0,0]] = [100, 150, 22]*ct[ct == [0,0,0]].shape[0]

plt.imshow(Image.fromarray(ct), cmap='gray')
plt.show()

# https://stackoverflow.com/questions/10465747/how-to-create-a-white-image-in-python
img = np.zeros([100,100,3],dtype=np.uint8)
img.fill(255) # or img[:] = 255

# so one row works
#img[2] = [[100,100,100]]*img[2].shape[0]

# if there are more it becomes tricky

index = 10

img[:index] = [[[100,100,100]]*img[:index].shape[1]]*img[:index].shape[0]

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


# okay so now it works!!!
# lets find the [100, 100,100] values & get to them!

M = img[img == [100,100,100]].shape[0]/3
M = int(M) # need to be an int
img[img == [100,100,100]] = [66,200,78]*M
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# lets make DO IT
redRPM = Matrix.make(list(MatrixType)[2], n_alternatives = 1)
redRPM.ans_ImageNum



plt.imshow(Image.fromarray(redRPM.ans_ImageNum), cmap='gray')
plt.show()










#################### notes

img.shape
img[2].shape
[[1,2,3]]*3
[2,3,4]*10


img[:2]
# https://stackoverflow.com/questions/12881926/create-a-new-rgb-opencv-image-using-python
# https://stackoverflow.com/questions/32171917/how-to-copy-a-2d-array-into-a-3rd-dimension-n-times




results= np.array([[100,100],
                   [0,0],
                   [100,100]])
#results = results.astype('unit8')
results = np.repeat(results[:, :, np.newaxis], 3, axis=2)

# so I am close
# indexing the right ones... yet, indexes as a vec
results[results == [0,0,0]]

# while np.repeat also give a vec, but repeats wrong
#results[results == [0,0,0]] = np.repeat([200,44,66], 2)

# how to np.repeat in a sequence...?
results[results == [0,0,0]] = [100, 150, 22]*results[results == [0,0,0]].shape[0]


results = results.astype('object')
results.dtype

np.repeat(results[:, :, np.newaxis], 3, axis=2)



# uint8 array for images

results = ct

for i in range(0,results.shape[0]):
    #print("i printed")
    for p in range(0, results.shape[1]):
        results[i,p] = [[results[i,p]]*3]
        #print("p printed")
        print("------")

        #print(results[i,p])






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
