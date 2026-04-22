import sys
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

RevGENOME = reverse_the_GENOME((sys.argv[1]))
GENOME = combine_the_GENOME((sys.argv[1]))

def find_the_ATG():
    ATG_position = []
    for i in range(len(GENOME)):
        if GENOME[i:i+3] == "ATG":
            ATG_position.append(i)
        else:
            pass
    return ATG_position 

def ShineDalgarno_Finder():
    ATG_position = find_the_ATG()
    valid_SD = []
    for ATG in ATG_position:
        window_start = max(0, ATG - 10)
        window = GENOME[window_start:ATG-2]
        if "AGG" in window:
            valid_SD.append(ATG)
    return valid_SD

def Gene_Former(Begins):
    Gene_Dic = {}
    a = len(GENOME)-2
    nested_ORF = 0
    count = 0
    i = 0
    for start in Begins:
        if nested_ORF < start:
            i = start + 3
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
    return Gene_Dic, i

def find_the_Genes():
    polycistronic_starts = ShineDalgarno_Finder()
    Gene_Dic = {}
    New_Gene_Dic = {}
    nested_ORF = 0
    a = len(GENOME)-2
    for Begins in polycistronic_starts:
        if Begins > nested_ORF:
            Gene_Dic, i = Gene_Former([Begins])
            last_valid_i = i
            New_Gene_Dic[Begins] = Gene_Dic[1]
            window = GENOME[i-1:i+5]
            #print(f"i={i}, window={window}, START")
            while "ATG" in window and i < a:
                pos_in_window = window.find("ATG")
                window_start = i -1
                #print(f"i={i}, window={window}, pos={pos_in_window}, shift={pos_in_window-4}")
                atg_start = window_start + pos_in_window
                Gene_Dic_2, i_new = Gene_Former([atg_start])
                if i_new > i + 3:
                    i = i_new
                    last_valid_i = i
                    New_Gene_Dic[atg_start] = Gene_Dic_2[1]
                    window = GENOME[i-1:i+5]
                    nested_ORF = i
                else:
                    nested_ORF = i
                    break
                continue
            else:
                i = last_valid_i
                nested_ORF = i
                Gene_Dic, i = Gene_Former([Begins])
                New_Gene_Dic[Begins] = Gene_Dic[1]
        else:
            pass
    delete_list = []
    for m in New_Gene_Dic.keys():
        if New_Gene_Dic[m] == "No stop sequence can be found":
            pass
        elif len(New_Gene_Dic[m]) < 90:
            delete_list.append(m)
        elif len(New_Gene_Dic[m]) > 7104:
            delete_list.append(m)
        else:
            pass
    #print(f"Gene_Dic size before delete: {len(New_Gene_Dic)}")
    for n in delete_list:
        del New_Gene_Dic[n]
    #print(f"Gene_Dic size after delete: {len(New_Gene_Dic)}")
    return New_Gene_Dic

def count():
    genes = find_the_Genes()
    fail_count = 0
    success_count = 0
    for gene in genes:
        if genes[gene] == "No stop sequence can be found":
            fail_count += 1
        else:
            success_count +=1
    return success_count, fail_count

def rev_find_the_ATG():
    ATG_position = []
    for i in range(len(RevGENOME)):
        if RevGENOME[i:i+3] == "ATG":
            ATG_position.append(i)
        else:
            pass
    return ATG_position 

def rev_ShineDalgarno_Finder():
    ATG_position = rev_find_the_ATG()
    valid_SD = []
    for ATG in ATG_position:
        window_start = max(0, ATG - 10)
        window = RevGENOME[window_start:ATG-2]
        if "AGG" in window:
            valid_SD.append(ATG)
    return valid_SD

def rev_Gene_Former(Begins):
    Gene_Dic = {}
    a = len(RevGENOME)-2
    nested_ORF = 0
    count = 0
    i = 0
    for start in Begins:
        if nested_ORF < start:
            i = start + 3
            count += 1
            Gene_Dic[count] = "ATG"
            while RevGENOME[i:i+3] not in ["TAA", "TAG", "TGA"] and i < a:
                Gene_Dic[count] += RevGENOME[i:i+3]
                i += 3
            else:
                if RevGENOME[i:i+3] in ["TAA", "TAG", "TGA"]:
                    Gene_Dic[count] += RevGENOME[i:i+3]
                    nested_ORF = i + 3          
                else:
                    Gene_Dic[count] = "No stop sequence can be found"
                    pass
        else:
            pass
    return Gene_Dic, i

def rev_find_the_Genes():
    polycistronic_starts = rev_ShineDalgarno_Finder()
    Gene_Dic = {}
    New_Gene_Dic = {}
    nested_ORF = 0
    a = len(RevGENOME)-2
    for Begins in polycistronic_starts:
        if Begins > nested_ORF:
            Gene_Dic, i = rev_Gene_Former([Begins])
            last_valid_i = i
            New_Gene_Dic[Begins] = Gene_Dic[1]
            window = GENOME[i-1:i+5]
            #print(f"i={i}, window={window}, START")
            while "ATG" in window and i < a:
                pos_in_window = window.find("ATG")
                window_start = i -1
                #print(f"i={i}, window={window}, pos={pos_in_window}, shift={pos_in_window-4}")
                atg_start = window_start + pos_in_window
                Gene_Dic_2, i_new = rev_Gene_Former([atg_start])
                if i_new > i + 3:
                    i = i_new
                    last_valid_i = i
                    New_Gene_Dic[atg_start] = Gene_Dic_2[1]
                    window = GENOME[i-1:i+5]
                    nested_ORF = i
                else:
                    nested_ORF = i
                    break
                continue
            else:
                i = last_valid_i
                nested_ORF = i
                Gene_Dic, i = Gene_Former([Begins])
                New_Gene_Dic[Begins] = Gene_Dic[1]
        else:
            pass
    delete_list = []
    for m in New_Gene_Dic.keys():
        if New_Gene_Dic[m] == "No stop sequence can be found":
            pass
        elif len(New_Gene_Dic[m]) < 90:
            delete_list.append(m)
        elif len(New_Gene_Dic[m]) > 7104:
            delete_list.append(m)
        else:
            pass
    #print(f"Rev_Gene_Dic size before delete: {len(New_Gene_Dic)}")
    for n in delete_list:
        del New_Gene_Dic[n]
    #print(f"Rev_Gene_Dic size after delete: {len(New_Gene_Dic)}")
    return New_Gene_Dic

def rev_count():
    genes = rev_find_the_Genes()
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

def sorted_list():
    dic = find_the_Genes()
    rev_dic = rev_find_the_Genes()
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
    print(f"Found {len(find_the_Genes()) + len(rev_find_the_Genes())} genes")
    print(f"--------- BP Count -------")
    a, b = sorted_list()
    for genes in a:
        print(f"{genes["gene"]}: {genes["numbp"]}")
    for failed in b:
        print(f"{failed["gene"]}: {failed["numbp"]}")
    c, d = count()
    e, f = rev_count()
    print(f"{c + e} genes have been found")
    print(f"{d + f} times failed to found the genes")
    
    
