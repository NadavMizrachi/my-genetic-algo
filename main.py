from my_genetic_algo.genetic_algo import GeneticAlgo

# Hyperparameters:
N_POP = 100
N_BITS = 11
N_ITER = 200
CROS_PROB = 0.9
MUTATE_PROB = 1.0 / N_BITS


def one_max_evaluation(list_of_bits):
    return -sum(list_of_bits)


def max_holes_evaluation(list_of_bits):
    holes = 0
    hole_started = list_of_bits[0] == 1
    inside_hole = False
    for i in range(1, len(list_of_bits)):
        if list_of_bits[i] == 1:
            if inside_hole:
                holes += 1
                inside_hole = False
                hole_started = True
            else:
                hole_started = True
        else:
            if hole_started:
                inside_hole = True
            # list_of_bits[i] is 0

    return -1 * holes

def main():
    genetic_algo = GeneticAlgo(fitness_evaluation=max_holes_evaluation,
                               n_bits=N_BITS,
                               n_pop=N_POP,
                               n_iter=N_ITER,
                               cros_prob=CROS_PROB,
                               mutate_prob=MUTATE_PROB)
    best, score = genetic_algo.find_minimum()
    print("Done!")
    print(f"Best solution = {best}. The evaluation is = {score}")
    # l = [1,0,0,1]
    # print(f"input = {l} res = {max_holes_evaluation(l)}")
    # l = [1, 0, 0, 1, 0]
    # print(f"input = {l} res = {max_holes_evaluation(l)}")
    # l = [0, 1, 1, 0]
    # print(f"input = {l} res = {max_holes_evaluation(l)}")
    # l = [1, 0, 0, 1, 0, 1]
    # print(f"input = {l} res = {max_holes_evaluation(l)}")
    # l = [1, 1, 1, 1]
    # print(f"input = {l} res = {max_holes_evaluation(l)}")
    # l = [0, 0, 0, 0]
    # print(f"input = {l} res = {max_holes_evaluation(l)}")
    # l = [1, 1, 1, 1]
    # print(f"input = {l} res = {max_holes_evaluation(l)}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
