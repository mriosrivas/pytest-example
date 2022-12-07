import numpy as np


def distance(x1, x2):
    return np.sqrt(np.sum(np.square(x2 - x1)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(distance(5,10))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
