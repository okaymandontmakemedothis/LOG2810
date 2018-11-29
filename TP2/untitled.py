#!/usr/bin/python

import sys
import pprint

def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        if arg == "-h":
        	print("╔═══════════════════════════════════════════════════════╗")
        	print("║ NAME                                                  ║")
        	print("║    TP2.py                                             ║")
        	print("╠═══════════════════════════════════════════════════════╣")
        	print("║ SYNOPSIS                                              ║")
        	print("║    python3 TP2.py [-h] source_lexique ...             ║")
        	print("╠═══════════════════════════════════════════════════════╣")
        	print("║ DESCRIPTION                                           ║")
        	print("║    1-Crée une Trie à partir du lexique voulu.         ║")
        	print("║    2-Permet à l'usager de rechercher un mot voulu     ║")
        	print("║    3-Compte de mots valides tapés et ce, sur commande ║")
        	print("╚═══════════════════════════════════════════════════════╝")
        elif arg == "lexique 1.txt"

        else:
        	print("Did you mean -h?")

if __name__ == "__main__":
    main()