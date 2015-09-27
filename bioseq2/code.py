def identify(s1, s2):
    abs_matching = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            abs_matching += 1
    return abs_matching
