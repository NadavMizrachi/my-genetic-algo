import random
# Terms:
#   Population - Set of solutions (solutions represented as bits string).
#   Fitness - Function that evaluates the solution (we assume that we look for minimum).
#   Genetic recombination - Take two solutions (parents) and makes new solution set (childs).
#   Mutation - Takes solution and creates new solution (by flipping bits)
#   Hyperparameter - Constant determined and tunes the genetic algo (for example, how many iterations
#                       the algo will be executed).


# Psudo of genetic algo:
#   1. Create random population
#   2. Foreach iteration:
#       2.1  Update best solution until now
#       2.2. P <- "Choose" best solutions (evaluate with fitness function) as "parents".
#       2.3. C <- Take pairs from P, and for each pair, create two children (by recombination).
#       2.4. Foreach child in C, apply the mutation.
#   3. return solution


class GeneticAlgo:
    """
    This class represents genetic algorithm for finding solution to optimization problems.
    The solutions are represented as binary string.
    """
    def __init__(self, fitness_evaluation, n_bits, n_pop, n_iter, cros_prob, mutate_prob):
        """
        :param fitness_evaluation: Function that evaluates the fitness value of list of binary values {0, 1}.
        :param n_bits: How many bits in solution.
        :param n_pop: Size of population.
        :param n_iter: How many iterations the algorithm will run.
        :param cros_prob: Fraction between 0 to 1 to represent the probability of making new childs by crossover.
        :param mutate_prob: Fraction between 0 to 1 to represent the probability of mutate one bit for each bit in
                            a solution.
        """
        self.fitness_evaluation = fitness_evaluation
        self.n_bits = n_bits
        self.n_pop = n_pop
        self.n_iter = n_iter
        self.cros_prob = cros_prob
        self.mutate_prob = mutate_prob

    def find_minimum(self):
        """
        Finds solution closest to minimum fitness evaluation
        :return: Pair [best, score] , where best is the best solution and score is fitness_evaluation(best).
        """
        # Create initial population
        pop = self.create_pop(self.n_pop, self.n_bits)
        # Init best solution and evaluation
        best_eval = self.fitness_evaluation(pop[0])
        best_sol = None
        # Iterate N_ITER generations
        for gen in range(self.n_iter):
            fitness_scores = [self.fitness_evaluation(s) for s in pop]
            # Update best solution until now
            for i in range(len(pop)):
                if fitness_scores[i] < best_eval:
                    best_eval = fitness_scores[i]
                    best_sol = pop[i]
                    print(f"Found new best solution. Generation = {gen} Solution = {best_sol}. (Fitness = {best_eval})")
            parents = self.select_parents(pop, fitness_scores)
            childs = self.create_childs_from_parents(parents)
            mutations_childs = self.mutate_childs(childs)
            pop = mutations_childs
        return [best_sol, best_eval]

    def create_pop(self, n_pop, n_bits):
        """
        Creates list in length of n_pop. Each element is list of 1 or 0 in length of n_bits.
        :param n_pop: Size of population
        :param n_bits: Size of bits for each element
        :return:
        """
        return [[random.randint(0, 1) for _ in range(self.n_bits)] for _ in range(self.n_pop)]

    def select_parents(self, population, fitness_scores):
        """
        Choosing parents based on the fitness function.
        :param population:
        :param fitness_scores: Scores of each element in population (fitness_scores[i] is the score of population[i]).
        :return: List of elements from population
        """
        return [self.select_parent(population, fitness_scores) for _ in population]

    def select_parent(self, population, fitness_scores, k=3):
        """
        Select one element from population by tournament selection, with best fitness value.
        :param population:
        :param fitness_scores:
        :param k:
        :return: One element from population
        """
        min_fitness = float('inf')
        smallest_idx = -1
        for _ in range(k):
            rand_idx = random.randint(0, len(population) - 1)
            if fitness_scores[rand_idx] < min_fitness:
                min_fitness = fitness_scores[rand_idx]
                smallest_idx = rand_idx
        return population[smallest_idx]

    def create_childs_from_parents(self, parents):
        children = list()
        for i in range(0, len(parents), 2):
            childs = self.crossover(parents[i], parents[i+1])
            for child in childs:
                children.append(child)
        return children

    def crossover(self, p1, p2):
        c1, c2 = p1.copy(), p2.copy()
        if random.random() < self.cros_prob:
            # Random position inside the solution (not first/last position)
            rand_slice_pos = random.randint(1, len(p1) - 2)
            return self.synthesis_parents(p1, p2, rand_slice_pos)
        else:
            return [c1, c2]

    def synthesis_parents(self, p1, p2, position):
        c1 = p1[:position] + p2[position:]
        c2 = p2[:position] + p1[position:]
        return [c1, c2]

    def mutate_childs(self, childs):
        mutated_childs = list()
        for c in childs:
            mutation = self.mutate(c)
            mutated_childs.append(mutation)
        return mutated_childs

    def mutate(self, element):
        res = element.copy()
        for bit_idx in res:
            if random.random() < self.mutate_prob:
                res[bit_idx] = 1 - element[bit_idx]
        return res

