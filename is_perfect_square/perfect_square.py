import math
import cmath
from decimal import *


def is_perfect_square(num, *, complex=False):
    if complex:
        if len(str(cmath.sqrt(num)).split('.')) > 1:
            return False
    else:
        if num < 0:
            return False
        if num <= 1:
            return True
        if len(str(Decimal(num).sqrt()).split('.')) > 1:
            return False

    return True


if __name__ == '__main__':
    print(f'{is_perfect_square(25)}')
