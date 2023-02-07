
import sys
from BitVector import *

def stateArray():
    
    statearray = [[0 for x in range(4)] for x in range(4)]
    print(statearray)
    block = range(128)
    for i in range(4):
        for j in range(4):
            statearray[j][i] = block[32*i + 8*j:32*i + 8*(j+1)]
    print(statearray)
    print(len(statearray) * len(statearray[0]))

def get_encryption_key(keyFile):
    key = ""
    FILEIN = open(keyFile)
    
    key = BitVector(textstring = FILEIN.read())
    print(key)
    print(len(key))
    # key = key.permute(key_permutation_1)

    # print("Here is the 56-bit encryption key\n")
    # print(key)
    FILEIN.close
    return key

if __name__ == "__main__":
    args = sys.argv[1:]
    print(args)
    stateArray(args[0])
    