import pprint
import unittest
from my_genetic_algo import genetic_algo


class TestGenericAlgo(unittest.TestCase):
    def test_create_pop(self):
        n_pop = 10
        n_bits = 20
        pop = genetic_algo.create_pop(n_pop, n_bits)
        self.assertEqual(len(pop), 10, "Should equal 10")
        for l in pop:
            self.assertEqual(len(l), n_bits, "Bits in list should be equal " + str(n_bits))
        n_pop = 0
        n_bits = 10
        pop = genetic_algo.create_pop(n_pop, n_bits)
        for l in pop:
            self.assertEqual(len(l), n_bits, "Bits in list should be equal " + str(n_bits))
        n_pop = 1
        n_bits = 20
        pop = genetic_algo.create_pop(n_pop, n_bits)
        for l in pop:
            self.assertEqual(len(l), n_bits, "Bits in list should be equal " + str(n_bits))

    # def test_choose_parents(self):
    #     n_pop = 10
    #     n_bits = 20
    #     pop = genetic_algo.create_pop(n_pop, n_bits)
    #     parents = genetic_algo.select_parents(pop)
    #     self.assertEqual(len(parents), n_pop, "Parents = " + str(parents) + " should be in length " + str(len(parents)))
    #
    #     n_pop = 200
    #     n_bits = 10
    #     pop = genetic_algo.create_pop(n_pop, n_bits)
    #     parents = genetic_algo.select_parents(pop)
    #     self.assertEqual(len(parents), n_pop, "Parents = " + str(parents) + " should be in length " + str(len(parents)))

    def test_synthesis(self):
        p1 = [1, 2, 3, 4, 5]
        p2 = [5, 4, 3, 2, 1]
        c1, c2 = genetic_algo.synthesis_parents(p1, p2, 1)
        c1_expected = [1, 4, 3, 2, 1]
        c2_expected = [5, 2, 3, 4, 5]
        self.assertEqual(c1, c1_expected, "c1 = " + str(c1) + " but expected = " + str(c1_expected))
        self.assertEqual(c2, c2_expected, "c2 = " + str(c2) + " but expected = " + str(c2_expected))
        print("p1 = " + str(p1))
        print("p2 = " + str(p2))
        print("c1 = " + str(c1))
        print("c2 = " + str(c2))

        p1 = [1, 2, 3, 4, 5]
        p2 = [5, 4, 3, 2, 1]
        c1, c2 = genetic_algo.synthesis_parents(p1, p2, 3)
        c1_expected = [1, 2, 3, 2, 1]
        c2_expected = [5, 4, 3, 4, 5]
        self.assertEqual(c1, c1_expected, "c1 = " + str(c1) + " but expected = " + str(c1_expected))
        self.assertEqual(c2, c2_expected, "c2 = " + str(c2) + " but expected = " + str(c2_expected))
        print("p1 = " + str(p1))
        print("p2 = " + str(p2))
        print("c1 = " + str(c1))
        print("c2 = " + str(c2))

    # def test_create_childs_from_parents(self):
    #     n_pop = 10
    #     n_bits = 20
    #     pop = genetic_algo.create_pop(n_pop, n_bits)
    #     parents = genetic_algo.select_parents(pop)
    #     childs = genetic_algo.create_childs_from_parents(parents)
    #     self.assertEqual(len(parents), len(childs), "Parents length is " + str(len(parents)) + " but child len is " + str(len(childs)))
    #     print("Parents:")
    #     pprint.pprint(parents)
    #     print("Childs:")
    #     pprint.pprint(childs)

    def test_objective(self):
        sol = [1, 0, 0, 1]
        self.assertEqual(genetic_algo.objective(sol), -2, "Should equal -2")
        sol = [0, 0, 0, 0]
        self.assertEqual(genetic_algo.objective(sol), 0, "Should equal 0")
        sol = [1, 1, 1, 1]
        self.assertEqual(genetic_algo.objective(sol), -4, "Should equal -4")


if __name__ == "__main__":
    unittest.main()
