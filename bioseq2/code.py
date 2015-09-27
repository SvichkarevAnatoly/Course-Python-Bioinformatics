def identify(s1, s2):
    abs_matching = 0
    len_alignment = min(len(s1), len(s2))
    alignment = ""
    for i in range(len_alignment):
        if s1[i] == s2[i]:
            abs_matching += 1
            alignment += '*'
        else:
            alignment += ' '
    percent = abs_matching * 100.0 / len_alignment
    return abs_matching, len_alignment, percent, alignment


DNA_2 = {
    'G': {'G': 1, 'C': -3, 'A': -3, 'T': -3, 'N': 0},
    'C': {'G': -3, 'C': 1, 'A': -3, 'T': -3, 'N': 0},
    'A': {'G': -3, 'C': -3, 'A': 1, 'T': -3, 'N': 0},
    'T': {'G': -3, 'C': -3, 'A': -3, 'T': 1, 'N': 0},
    'N': {'G': 0, 'C': 0, 'A': 0, 'T': 0, 'N': 0}
}


def similarity_dna(s1, s2):
    score = 0
    for i in range(len(s1)):
        score += DNA_2[s1[i]][s2[i]]
    return score
