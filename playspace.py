# Nicholas Judd
# 20230407
# njudd.com


# https://pypi.org/project/raven-gen/
# https://github.com/shlomenu/raven-gen



# %%
from raven_gen import Matrix, MatrixType
import numpy as np
import os
import cv2
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
plt.imshow(Image.fromarray(simpleRPM.ans_ImageNum), cmap='gray')
plt.show()

# @Ann
# can you identify the possible vector to target white values & make them all red?


# @Maud
# can you check out matrix.py and somehow have the alternatives saving as well
# this is a harder task, you will need to save them seperately and you won't know how many
# potentially within the for loop use a string manipulation tools to name the alteratives (e.g., alt"_i")
# this is already a quite advanced task in R, ask if you need help!

# Note, you will need to save a variable as an evaluated class rather than a string.
# in R is is done with eval() and the bangbang oppertors




### random code chunks


# how to properly target the matricies we want
# 4 & 5 are not 6by6; 6 & 7 is possible to complicated for kids
options = list(MatrixType)[0:3] #limiting to 4 options
choice = np.random.choice(options) # lets grab a random choice
relevantRPM = Matrix.make(choice)
# or less verbosely
# rpm = Matrix.make(np.random.choice(list(MatrixType)[0:3])
relevantRPM.save(".", "append", background_color=130)



rpm = Matrix.make(np.random.choice(list(MatrixType)))
#rpm.save(".", "test")
print(rpm)
print(rpm.rules)
os.getcwd()

rpm.save(".", "test3")


from raven_gen import Ruleset, RuleType
ruleset = Ruleset(size_rules=[RuleType.CONSTANT, RuleType.PROGRESSION], shape_rules=list(RuleType))
rpm = Matrix.make(np.random.choice(list(MatrixType)), ruleset=ruleset)



from raven_gen import Matrix, MatrixType
import numpy as np

# 4 & 5 are not 6by6; 6 & 7 is possible to complicated for kids
options = list(MatrixType)[0:3] #limiting to 4 options
choice = np.random.choice(options) # lets grab a random choice
rpm = Matrix.make(choice)
# or less verbosely
# rpm = Matrix.make(np.random.choice(list(MatrixType)[0:3])
ct = rpm.save(".", "Hmm", background_color=130)

# class within a def in python
# https://stackoverflow.com/questions/4296677/creating-a-class-within-a-function-and-access-a-function-defined-in-the-containi


plt.imshow(rpm, cmap='gray')
plt.show()
plt.show(rpm)






# okay so just add a tuple of colors the similar lenght & see what happens

# they do length -1
# which might not work with a tuple



# you need to setup the package, load it and run the simple ass example with the color tuple










# %%
import numpy as np
import cv2
import matplotlib.pyplot as plt


# reads image 'opencv-logo.png' as grayscale

# img = cv2.imread('/Users/njudd/Desktop/stch.png', 0)
img = cv2.imread('/Users/njudd/Desktop/stch.jpeg') # the 0 made it not have color...?


o = (10, 10) # x1, y1
t = (100, 50) # x2 , y2

#cv2.rectangle(img, one, t, (255,0,0), 2)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.rectangle(img, o, t, 255, -2)
plt.imshow(img)
#plt.imshow(img[) # , cmap='gray'
plt.show()

a = np.ones((400,400), np.uint8) #* int(222, 33, 33)
plt.imshow(a, cmap='gray')
plt.show()



c = np.zeros((2,2),dtype='i,i,i')[1,1]


c = np.ones((2, 2, 3), int)
b = (3,44,200)

c = np.ones((20, 20, 3), np.uint8)
b = 255

b = (255,33,255)
c = c * b

plt.imshow(c, cmap='gray')
plt.show()

c =np.ones((300,300),dtype='i,i,i').tolist()
plt.imshow(c, cmap='gray')
plt.show()





np.ones((400,400), dtype= [[(0,0,0)])
print(a.dtype)

a = a.astype('float64')


# %%
import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('/Users/njudd/Desktop/stch.jpeg')

# Define the rectangle coordinates
x1, y1 = 100, 100
x2, y2 = 300, 300

cl = ((33,83,13), (123,44,120))

# Draw the rectangle
cv2.rectangle(img, (x1, y1), (x2, y2), 222, -30) # it does BGR

# somewhere in the script they are making the single values to 3 values for gray scale (222,222,222)

# Display the image with the rectangle
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# Make a symbolic linking of the scripts with line numbers




# Save the modified image
cv2.imwrite('/Users/njudd/Desktop/stchCT.jpeg', img)
# %%


# https://stackoverflow.com/questions/58215094/change-the-color-of-the-cv2-rectangle

# The color parameter of the cv2.rectangle expects a tuple of 3 integer representing the three color components, RGB.
# By calling the function the following way :

# OpenCV represents the images in BGR as opposed to the RGB we expect

ct =((33,83,73), (0,83,73), (33,8,73))
ct[1]




obj = (333,333,333)
isinstance(obj, tuple)
isinstance(obj, int)


cv2.rectangle(frame, (10, 10), (100, 50), (colour2), -1)

# %%


alts = {1,2,3}
ct = {} # here is an empty dict


a = {}
for name, values in alts():
    b = [ind for ind, val in enumerate(values) if np.isnan(val)]
    a[name] = b
# now the result is already correct!

a = {name: [i for i, x in enumerate(vals) if np.isnan(x)] for name, vals in tr.items()}


def save(self,  # so self is the object we assigned (i.e., rpm)
         path,  # argq
         puzzle_name,  # arg2
         background_color=255,  # arg4 with defaults... etc
         image_size=480,
         line_thickness=3,
         shape_border_thickness=2):
    image_size, background_color, line_thickness, shape_border_thickness = \
        int(abs(image_size)), int(abs(background_color)), int(abs(line_thickness)), int(abs(shape_border_thickness))
    assert (image_size != 0 and background_color <= 255)
    img = self.generate_matrix(self.answer, background_color, image_size,
                               line_thickness, shape_border_thickness)
    self.ans_ImageNum = img
    # class list: this doesn't work because it is WITHIN the function
    #    imgZ = img

    img = Image.fromarray(img)  # making it an image since I took it away form the return of generate_matrix
    # np.savetxt(os.path.join(path, puzzle_name + "_answerY.png"), img)
    img.save(os.path.join(path, puzzle_name + "_answer.png"))
    for i, alternative in enumerate(self.alternatives):
        img = self.generate_matrix(alternative, background_color,
                                   image_size, line_thickness,
                                   shape_border_thickness)
        img = Image.fromarray(img)  # making it an image
        img.save(os.path.join(path, puzzle_name + f"_alternative_{i}.png"))
