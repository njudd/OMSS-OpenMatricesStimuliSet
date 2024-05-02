import raven_gen
from raven_gen import Matrix, MatrixType, Ruleset, RuleType
import numpy as np

counter = 100 #lets generate a 100 problems
while counter > 0:
    c = Matrix.make(np.random.choice(list(MatrixType)), n_alternatives=7)
    print("problem:", counter)
    counter -= 1
# it breaks quickly

# trying with 5 alternatives
counter = 100 #lets generate a 100 problems
while counter > 0:
    c = Matrix.make(np.random.choice(list(MatrixType)), n_alternatives=5)
    print("problem:", counter)
    counter -= 1
# it breaks

# trying with 4 alternatives
counter = 1000 #lets UP the counter
while counter > 0:
    c = Matrix.make(np.random.choice(list(MatrixType)), n_alternatives=4)
    print("problem:", counter)
    counter -= 1
# it broke at prob 480

# trying with 3 alternatives
counter = 5000 #lets UP the counter AGAIN
while counter > 0:
    c = Matrix.make(np.random.choice(list(MatrixType)), n_alternatives=3)
    print("problem:", counter)
    counter -= 1
# it works