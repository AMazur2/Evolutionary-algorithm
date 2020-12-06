def test_select():
    pass
    # TODO fix this test
    # selector = rouletteParentSelector()
    # fitness = [0.2, 0.4, 0.5, 0.9]
    # population = [FloatingPointIndividual([1, 1, 1]), FloatingPointIndividual([2, 2, 2]),
    #               FloatingPointIndividual([3, 3, 3]), FloatingPointIndividual([4, 4, 4])]
    # i = 0
    # for el in population:
    #     el.setFitnessFunctionEvaluation(fitness[i])
    #     i = i + 1
    #
    # chosen = selector.chooseOne(population, fitness, 2.0)
    #
    # assert chosen in population
    #
    # marriages = selector.getParents(population)
    #
    # for el in marriages:
    #     for individual in el:
    #         assert individual in population
    #
    # selector = simpleParentSelector()
    # marriages = selector.getParents(population)
    #
    # temp = []
    # for i in range(len(population)):
    #     temp.append(population[i].getRepresentation())
    # for el in marriages:
    #     for individual in el:
    #         assert individual.getRepresentation() in temp
