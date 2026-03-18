import sys
from stats import report

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_genomes>")
        sys.exit(1)
        
    a = report(sys.argv[1])
    print(a)

main()