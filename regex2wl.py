#!/usr/bin/env python3
__author__      = "0x25"
__copyright__   = "GNU General Public Licence"


import exrex
import os, sys, argparse
import time
from datetime import datetime
import itertools

defaultPattern = '[Pp][aA4][sS5]w[O0o]rd'

description ="\033[1;31m Generate Worldlist from regex \033[0m"
epilog="\033[0;35m If you like this tool you can send me some monero \o/ { 4Ahnr36hZQsJ3P6jowXvs7cLkSVbkq2KyfQBVURYVftcj9tDoA592wT1jskroZEk2QDEZFPYMLqVvJWZHecFwQ9nL15SzRG } \033[0m"

# parse args
parser = argparse.ArgumentParser(description=description, epilog=epilog)
parser.add_argument('-i','--pfile', help='File with one pattern line by line')
parser.add_argument('-p','--pattern', default=defaultPattern, help='regex pattern based on exrex lib')
parser.add_argument('-v','--verbose', action='store_true', help='verbose mode')
parser.add_argument('-o','--output', help='file to save result')

args = parser.parse_args()
verbose = False

def main(args):

    patterns = []
    wordlist = []
    global verbose

    pattern = args.pattern
    pfilename = args.pfile
    verbose = args.verbose
    outputfilename = args.output

    if pfilename is not None:
        if not os.path.isfile(pfilename):
            print('Error: pattern file not exist')
            sys.exit()
        else:
            file = open(pfilename,'r')
            tmp = file.read().splitlines()
            patterns = [l.strip('\n\r') for l in tmp]
            pattern = None

    if pattern is not None:
        patterns.append(pattern)

    if verbose:
        print('Info: Nb pattern: {}'.format(len(patterns)))

    out = []
    for pattern in patterns:
        
        nb_iterration = exrex.count(pattern)  

        if verbose:
            print('Info: pattern {:.30} ...'.format(pattern))
            print('Info: nb iteration {:,}'.format(nb_iterration).replace(',',' '))

        # takes sometimes depend of your pattern 
        values = list(exrex.generate(pattern))
        
        if verbose:
            print('Start [{}] .. to [{}]'.format(values[0],values[-1]))
        wordlist.extend(values)

    if outputfilename is not None:
        f = open(outputfilename,'a')
        for pwd in wordlist:
            f.write(pwd + "\n")
        f.close()
    else:
        for pwd in wordlist:
            print(pwd)
    
if __name__ == "__main__":
    main(args)
    
