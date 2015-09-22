# Dictionary for translating triplets to amino acids
STANDARD_GENETIC_CODE = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UCU': 'Ser', 'UCC': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UGU': 'Cys', 'UGC': 'Cys',
    'UUA': 'Leu', 'UCA': 'Ser', 'UAA': None, 'UGA': None,
    'UUG': 'Leu', 'UCG': 'Ser', 'UAG': None, 'UGG': 'Trp',
    'CUU': 'Leu', 'CUC': 'Leu', 'CCU': 'Pro', 'CCC': 'Pro',
    'CAU': 'His', 'CAC': 'His', 'CGU': 'Arg', 'CGC': 'Arg',
    'CUA': 'Leu', 'CUG': 'Leu', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAA': 'Gln', 'CAG': 'Gln', 'CGA': 'Arg', 'CGG': 'Arg',
    'AUU': 'Ile', 'AUC': 'Ile', 'ACU': 'Thr', 'ACC': 'Thr',
    'AAU': 'Asn', 'AAC': 'Asn', 'AGU': 'Ser', 'AGC': 'Ser',
    'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
    'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
    'GUU': 'Val', 'GUC': 'Val', 'GCU': 'Ala', 'GCC': 'Ala',
    'GAU': 'Asp', 'GAC': 'Asp', 'GGU': 'Gly', 'GGC': 'Gly',
    'GUA': 'Val', 'GUG': 'Val', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAA': 'Glu', 'GAG': 'Glu', 'GGA': 'Gly', 'GGG': 'Gly'
}

dna_seq = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
protein_seq = 'IRTNGTHMQPLLKLMKFQKFLLELFTLQKRKPEKGYNLPIISLNQ'


def dna_to_rna(dna):
    return dna.replace('T', 'U')


def protein_translation(dna_seq):
    """ This function translates a nucleic acid sequence into a
    protein sequence, until the end or until it comes across
    a stop codon """
    # Make sure we have RNA sequence
    dna_seq = dna_to_rna(dna_seq)

    protein_seq = []
    i = 0
    while i + 2 < len(dna_seq):
        codon = dna_seq[i:i + 3]
        amino_acid = STANDARD_GENETIC_CODE[codon]
        # Found stop codon
        if amino_acid is None:
            break
        protein_seq.append(amino_acid)
        i += 3
    return protein_seq


def estimate_mol_mass(seq, mol_type='protein'):
    """Calculate the molecular weight of a biological sequence assuming
    normal isotopic ratios and protonation/modification states
    """
    residue_masses = \
        {
            "DNA":
                {"G": 329.21, "C": 289.18, "A": 323.21, "T": 304.19, },
            "RNA":
                {"G": 345.21, "C": 305.18, "A": 329.21, "U": 302.16, },
            "protein":
                {"A": 71.07, "R": 156.18, "N": 114.08, "D": 115.08,
                 "C": 103.10, "Q": 128.13, "E": 129.11, "G": 57.05,
                 "H": 137.14, "I": 113.15, "L": 113.15, "K": 128.17,
                 "M": 131.19, "F": 147.17, "P": 97.11, "S": 87.07,
                 "T": 101.10, "W": 186.20, "Y": 163.17, "V": 99.13}
        }

    mass_dict = residue_masses[mol_type]

    # Begin with mass of extra end atoms H + OH
    mol_mass = 18.02
    for letter in seq:
        mol_mass += mass_dict[letter]
    return mol_mass
