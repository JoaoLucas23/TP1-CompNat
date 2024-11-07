class GeneticProgramming:
    def __init__(self, population_size,num_generations,crossover_probsover_prob,mutation_prob,tournament_size,elitism,max_individual_size):
        self.population_size = population_size
        self.num_generations = num_generations
        self.crossover_prob = crossover_probsover_prob
        self.mutation_prob = mutation_prob
        self.tournament_size = tournament_size
        self.elitism = elitism
        self.max_individual_size = max_individual_size

        