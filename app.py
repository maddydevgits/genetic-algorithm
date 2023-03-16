# built-in library in python to create a random data
import random

# number of individuals in each generation
population_size=100

# valid genes - ascii chart
genes='''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

# target string
target='Sacet Chirala'

# represeting individual
class Individual(object):
    # create a constructor
    def __init__(self,chromosome):
        self.chromosome=chromosome
        self.fitness=self.cal_fitness()
    
    @classmethod
    def mutated_genes(self):
        # create mutation for genes
        global genes
        gene=random.choice(genes)
        return gene
    
    @classmethod
    def create_gnome(self):
        # creating chromosome
        global target
        gnome_len=len(target)
        return [self.mutated_genes() for _ in range(gnome_len)]
    
    def mate(self,par2):
        # perform mating and produce new offspring

        # chromosome for offspring
        child_chromosome=[]
        for gp1,gp2 in zip(self.chromosome,par2.chromosome):

            # random value
            prob=random.random()

            if prob<0.45: # prob value is less than 0.45, then parent1 chromosome will be selected
                child_chromosome.append(gp1)
            elif prob<0.90: # prob value is less than 0.90, then parent2 chromosome will be selected
                child_chromosome.append(gp2)
            else: # if both values get failed, mutated the genes - (combining the genes of both parents)
                child_chromosome.append(self.mutated_genes())
        return Individual(child_chromosome)
    
    def cal_fitness(self):
        global target
        fitness=0
        for gs,gt in zip(self.chromosome,target): # zipping the child chromosome and target and compare them
            if gs!=gt:
                fitness+=1
        return fitness # fitness value is zero, then it is the perfect match

def main():
    global population_size

    # current generation
    generation=1

    found=False
    population=[]

    # create initial population
    for i in range(population_size):
        gnome=Individual.create_gnome()
        population.append(Individual(gnome))
    
    while not found:

        # sort the population in increasing order of fitness score
        population=sorted(population,key=lambda x:x.fitness)

        if population[0].fitness<=0: # if the fitness score is zero, offspring is what we targeted
            found=True
            break

        # otherwise we have to new offspring(child)
        new_generation=[]

        #perform elitism, that means 10% of fitness population
        s=int((10*population_size)/100)
        new_generation.extend(population[:s]) # extending the generation to the new value

        s=int((90*population_size)/100) # to mate to produce new off spring
        for i in range(s):
            parent1=random.choice(population[:50]) # from 50% of population, individuals will be selected as parents
            parent2=random.choice(population[:50])
            child=parent1.mate(parent2) # mating to generate child
            new_generation.append(child)
        
        population=new_generation # older generations will get die 

        print("Generation: {}\tString: {}\tFitness: {}".format(generation,"".join(population[0].chromosome),population[0].fitness))
        generation+=1
    
    print("Generation: {}\tString: {}\tFitness: {}".format(generation,"".join(population[0].chromosome),population[0].fitness))

if __name__=="__main__":
    main()
