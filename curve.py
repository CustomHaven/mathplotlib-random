# https://www.codecademy.com/courses/learn-python-3/lessons/modules-python/exercises/modules-python-namespaces
# import codecademylib3_seaborn
# Should run pipenv install these imports ...

# Not part of this but other modules to consider
# from decimal import Decimal
# from datetime import datetime

# Add your code below:
from matplotlib import pyplot as plt # fix import issue
import random

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
# print(numbers_b)


plt.plot(numbers_a, numbers_b)


plt.show()
