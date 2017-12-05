def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    a=0
    for char in dna:
        a=a+1
    return a

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if get_length(dna1) > get_length(dna2):
        return True
    return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    b=0
    for char in dna:
        if char in nucleotide:
            b=b+1
    return b

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1.find(dna2) >= 0:
        return True
    return False


def is_valid_sequence(s):
    '''(str) -> bool

     Return True if and only if the DNA sequence is valid
     (that is, it contains no characters other than 'A', 'T', 'C' and 'G').

      >>> is_valid_sequence('AGTACT')
      True
      >>> is_valid_sequence('AGTACF')
      False
      >>> is_valid_sequence(ÁGTACt)
      False
      '''
    x=0
    for char in s:
        if char not in('A','T','G','C') or char.islower():
            x=x+1
    if x==0:
        return True
    return False

def insert_sequence(s1, s2, index):
    '''(str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>> insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>>insert_sequence ('CCGG','AT',1)
    'CATCGG'
    >>> insert_sequence('CCGG','AT',0)
    'ATCCGG'
    '''

    return s1[0:index]+s2+s1[index:get_length(s1)]

def get_complement (n):
    ''' (str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    '''

    if not is_valid_sequence(n) or not get_length(n) == 1:
        return False

    if n == 'A':
        return 'T'
    if n == 'T':
        return 'A'
    if n == 'G':
        return 'C'
    if n == 'C':
        return 'G'

def get_complementary_sequence(dna):
    ''' (str) -> str

     Return the DNA sequence that is complementary to the given DNA sequence.

     >>> get_complementary_sequence('AT')
     'TA'
     >>> get_complementary_sequence('GCAT')
     'CGTA'
     '''

    r=''
    if not is_valid_sequence(dna):
        return False

    for char in dna:
        r=r+get_complement(char)
    return r

