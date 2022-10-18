import pprint
import random
import sys

from my_genetic_algo.genetic_algo import *


def main():
    # args = sys.argv[1:]
    # n_pop = args[0]
    # print("n_pop is " + n_pop)
    # n_bits = args[1]
    # print("n_bits is " + n_bits)
    # pop = create_pop(int(n_pop), int(n_bits))
    # pprint.pprint(pop)
    print(random.random())
    print(random.random())
    print(random.random())
    print(random.random())
    pop = create_pop(10, 4)
    for i in range(len(pop)):
        print(" ================== ")
        print("Original element :")
        print(pop[i])
        print("After mutation :")
        print(mutate(pop[i]))


if __name__ == '__main__':
    main()
