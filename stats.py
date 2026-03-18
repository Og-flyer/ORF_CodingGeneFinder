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

def reverse_the_GENOME(Genome):
    rawGenome = combine_the_GENOME(Genome)
    reverseGenome = ""
    for bp in rawGenome[::-1]:
        if bp == "A":
            reverseGenome = reverseGenome + "T"
        elif bp == "T":
            reverseGenome = reverseGenome + "A"
        elif bp == "G":
            reverseGenome = reverseGenome + "C"
        elif bp == "C":
            reverseGenome = reverseGenome + "G"
        else:
            reverseGenome = reverseGenome + bp
    return reverseGenome

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
    nested_ORF = 0
    a = len(GENOME)-2
    for Begins in Gene_Begins:
        if nested_ORF < Begins:
            i = Begins + 3
            count += 1
            Gene_Dic[count] = "ATG"
            while GENOME[i:i+3] not in ["TAA", "TAG", "TGA"] and i < a:
                Gene_Dic[count] += GENOME[i:i+3]
                i += 3
            else:
                if GENOME[i:i+3] in ["TAA", "TAG", "TGA"]:
                    Gene_Dic[count] += GENOME[i:i+3]
                    nested_ORF = i + 3
                else:
                    Gene_Dic[count] = "No stop sequence can be found"
                    pass
        else:
            pass
    delete_list = []
    for m in Gene_Dic.keys():
        if Gene_Dic[m] == "No stop sequence can be found":
            pass
        elif len(Gene_Dic[m]) < 300:
            delete_list.append(m)
        else:
            pass
    for n in delete_list:
        del Gene_Dic[n]
    return Gene_Dic

def count(Genome):
    genes = find_the_Genes(Genome)
    fail_count = 0
    success_count = 0
    for gene in genes:
        if genes[gene] == "No stop sequence can be found":
            fail_count += 1
        else:
            success_count +=1
    return success_count, fail_count

def rev_find_the_ATG(Genome):
    GENOME = reverse_the_GENOME(Genome)
    ATG_position = []
    for i in range(len(GENOME)):
        if GENOME[i:i+3] == "ATG":
            ATG_position.append(i)
        else:
            pass
    return ATG_position 

def rev_find_the_Genes(Genome):
    Gene_Begins = rev_find_the_ATG(Genome)
    Gene_Dic = {}
    GENOME = reverse_the_GENOME(Genome)
    count = 0
    nested_ORF = 0
    a = len(GENOME)-2
    for Begins in Gene_Begins:
        if nested_ORF < Begins:
            i = Begins + 3
            count += 1
            Gene_Dic[count] = "ATG"
            while GENOME[i:i+3] not in ["TAA", "TAG", "TGA"] and i < a:
                Gene_Dic[count] += GENOME[i:i+3]
                i += 3
            else:
                if GENOME[i:i+3] in ["TAA", "TAG", "TGA"]:
                    Gene_Dic[count] += GENOME[i:i+3]
                    nested_ORF = i + 3
                else:
                    Gene_Dic[count] = "No stop sequence can be found"
                    pass
        else:
            pass
    delete_list = []
    for m in Gene_Dic.keys():
        if Gene_Dic[m] == "No stop sequence can be found":
            pass
        elif len(Gene_Dic[m]) < 300:
            delete_list.append(m)
        else:
            pass
    for n in delete_list:
        del Gene_Dic[n]
    return Gene_Dic

def rev_count(Genome):
    genes = rev_find_the_Genes(Genome)
    fail_count = 0
    success_count = 0
    for gene in genes:
        if genes[gene] == "No stop sequence can be found":
            fail_count += 1
        else:
            success_count +=1
    return success_count, fail_count

def sort_on(items):
    return items["numbp"] 

def sorted_list(Genome):
    dic = find_the_Genes(Genome)
    rev_dic = rev_find_the_Genes(Genome)
    final_list = []
    fails = []
    for genes in dic:
        if dic[genes] == "No stop sequence can be found":
            fail = {"gene":f"gene number {genes}", "numbp": "failed"}
            fails.append(fail)
            fail = {}
        else:  
            order = {"gene":f"gene number {genes}", "numbp":f"{len(dic[genes])} bps"}
            final_list.append(order)
            order = {}
    for genes in rev_dic:
        if rev_dic[genes] == "No stop sequence can be found":
            fail = {"gene":f"gene number {genes}", "numbp": "failed"}
            fails.append(fail)
            fail = {}
        else:  
            order = {"gene":f"gene number {genes}", "numbp":f"{len(rev_dic[genes])} bps"}
            final_list.append(order)
            order = {}
    final_list.sort(reverse=True, key=sort_on)
    return final_list, fails

def report(Genome):
    print(f"============ GENE FINDER ============")
    print(f"Analyzing GENOME found at {Genome}...")
    print(f"----------- Gene Count ----------")
    print(f"Found {len(find_the_Genes(Genome)) + len(rev_find_the_Genes(Genome))} genes")
    print(f"--------- BP Count -------")
    a, b = sorted_list(Genome)
    for genes in a:
        print(f"{genes["gene"]}: {genes["numbp"]}")
    for failed in b:
        print(f"{failed["gene"]}: {failed["numbp"]}")
    c, d = count(Genome)
    e, f = rev_count(Genome)
    print(f"{c + e} genes have been found")
    print(f"{d + f} times failed to found the genes")
    
    
