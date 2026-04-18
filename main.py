import sys
from stats import report, ShineDalgarno_Finder,find_the_Genes, count, find_the_ATG, combine_the_GENOME

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_genomes>")
        sys.exit(1)
        
    c, d = count((sys.argv[1]))
    print(f"{c} genes have been found")

main()