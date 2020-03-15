#! /usr/bin/env python3

import sys
try:
    nub1 = int(sys.argv[1])
except ValueError:
    print("Parameter Error")
    sys.exit()

    nub2 = nub1 - 5000
    if nub2 <= 3000:
        nub3 = nub2 * 0.03 - 0
    elif nub2 > 3000 and nub2 <= 12000:
        nub3 = nub2 * 0.1 - 210
    elif nub2 > 12000 and nub2 <= 25000:
        nub3 = nub2 * 0.2 - 1410
    elif nub2 > 25000 and nub2 <= 35000:
        nub3 = nub2 * 0.25 - 2660
    elif nub2 > 35000 and nub2 <= 55000:
        nub3 = nub2 * 0.3 - 4410
    elif nub2 > 55000 and nub2 <= 80000:
        nub3 = nub2 * 0.35 - 7160
    elif nub2 > 80000:
        nub3 = nub2 * 0.45 - 15160
    print('{:.2f}'.format(nub3))


