##D# pairs:
#   Primer pairs are listed in a file, one per line.
#   Forward and reverse primers on each line are separated by a space. Ignore
#   anything after the first two space separated “words” on each line.
#       e.g. Example input file: here
#   Print the reverse complement of each primer of the pair in the same format
#   as the input file.
#   Hint: Use open(…).read() to read the entire contents of the file into a
#   string…

import sys

HW4Examples = sys.argv[1]
examples = ''.join(open(HW4Examples).read())
examples = examples.upper()

def complement(nuc):
    """Return the complement of a single nucleotide."""
    nucleotides = 'ACGT'
    complements = 'TGCA'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

def reverse_complement(primer):
    """Return the reverse complement of a DNA primer."""
    reverse_comp = []  # Empty list to build reverse complement
    for nuc in reversed(primer):  # Iterate through the reversed seq
        reverse_comp.append(complement(nuc))  # append the list with the reversed seq
    return ''.join(reverse_comp) #join the list back again as a string

for line in examples.splitlines(): #split file into its lines
    primers = line.split()[:2] #only take the first two things in each line
    forward = reverse_complement(primers[0]) #position0 = forward primer
    reverse = reverse_complement(primers[1]) #position1 = reverse primer
    print(forward, reverse)
