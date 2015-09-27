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
