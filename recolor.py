from raven_gen import Matrix, MatrixType
import matplotlib.pyplot as plt
from PIL import Image
import random
import numpy as np

# code before the function
random.seed(55)
simpleRPM_1 = Matrix.make(list(MatrixType)[2], n_alternatives = 0)
#simpleRPM_1.save(".", "_test", image_size = 750)
simpleRPM_1.gimme()

# code to make into a function
whole_img = simpleRPM_1.ans_img
#step 1 make multiply into colors values (three's)
whole_img = np.repeat(whole_img[:, :, np.newaxis], 3, axis=2)

# step 2; target and change the values
M = int(whole_img[whole_img == [168,168,168]].shape[0]/3)
whole_img[whole_img == [168,168,168]] = [40,114,247]*M

plt.imshow(Image.fromarray(whole_img), cmap='gray')
plt.show()


# values to recode
# 224, (255, 235, 59)
# 196, (251, 140, 0)
# 168, (211, 47, 47)
# 140, (186, 104, 200)
# 112, (30, 136, 229)
# 84, (0, 188, 212)
# 56, (56, 142, 60)
# 28, (46, 204, 113)