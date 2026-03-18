def count_the_GENOME(Genome):
    with open(Genome) as f:
        file = f.readlines()
        genome = []
        append = None
    for line in file:
        if line[0] == ">":
            append = False
        if append == False:
            append = None
        else:
            genome.append(line)
    return genome

def count(Genome):
    a = count_the_GENOME(Genome)
    print(a)
