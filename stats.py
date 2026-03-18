def filter_the_headlines(Genome):
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

def combine_the_GENOME(Genome):
    the_lines = filter_the_headlines(Genome)
    GENOME = ""
    for lines in the_lines:
        lines = lines.strip()
        GENOME = GENOME + lines
    return GENOME

def find_the_ATG(Genome):
    GENOME = combine_the_GENOME(Genome)
    ATG_position = []
    for i in range(len(GENOME)):
        if GENOME[i:i+3] == "ATG":
            ATG_position.append(i)
        else:
            pass
    return ATG_position 

def find_the_Genes(Genome):
    Gene_Begins = find_the_ATG(Genome)
    Gene_Dic = {}
    GENOME = combine_the_GENOME(Genome)
    count = 0
    a = len(GENOME)-2
    for Begins in Gene_Begins:
        i = Begins + 3
        count += 1
        Gene_Dic[count] = "ATG"
        while GENOME[i:i+3] not in ["TAA", "TAG", "TGA"] and i < a:
            Gene_Dic[count] += GENOME[i:i+3]
            i += 3
        else:
            if GENOME[i:i+3] in ["TAA", "TAG", "TGA"]:
              Gene_Dic[count] += GENOME[i:i+3]
            else:
                Gene_Dic[count] = "No stop sequence can be found"
                pass
    return Gene_Dic
                

def count(Genome):
    a = find_the_ATG(Genome)
    print(a)
