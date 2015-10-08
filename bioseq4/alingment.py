# coding=utf-8
import sys

# BLOSUM62
penalty = 5
blosum62 = \
    {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2,
           'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2},
     'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3,
           'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2},
     'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0,
           'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2},
     'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1,
           'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3},
     'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0,
           'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3},
     'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3,
           'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3},
     'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3,
           'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1},
     'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1,
           'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2},
     'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0,
           'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2},
     'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2,
           'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1},
     'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3,
           'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1},
     'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0,
           'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2},
     'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5,
           'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1},
     'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2,
           'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3},
     'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0,
           'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2},
     'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0,
           'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2},
     'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0,
           'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2},
     'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4,
           'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2},
     'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3,
           'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1},
     'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2,
           'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}


# LCSBACKTRACK(v, w)
#     for i ← 0 to |v|
#         si, 0 ← 0
#     for j ← 0 to |w|
#         s0, j ← 0
#     for i ← 1 to |v|
#         for j ← 1 to |w|
#             si, j ← max{si-1, j, si,j-1, si-1, j-1 + 1 (if vi = wj)}
#             if si,j = si-1,j
#                 Backtracki, j ← "↓"
#             else if si, j = si, j-1
#                 Backtracki, j ← "→"
#             else if si, j = si-1, j-1 + 1 and vi = wj
#                 Backtracki, j ← "↘"
#     return Backtrack
def lcs_backtrack(v, w):
    v_len = len(v)
    w_len = len(w)
    s = [[0] * (w_len + 1) for _ in range(v_len + 1)]
    backtrack = [[0] * w_len for _ in range(v_len)]

    for i in range(1, v_len + 1):
        for j in range(1, w_len + 1):
            s[i][j] = max(
                s[i - 1][j] - penalty,
                s[i][j - 1] - penalty,
                s[i - 1][j - 1] + blosum62[v[i - 1]][w[j - 1]])

            if s[i][j] == s[i - 1][j] - penalty:
                backtrack[i - 1][j - 1] = "↓"
            elif s[i][j] == s[i][j - 1] - penalty:
                backtrack[i - 1][j - 1] = "→"
            elif s[i][j] == s[i - 1][j - 1] + blosum62[v[i - 1]][w[j - 1]]:
                backtrack[i - 1][j - 1] = "↘"
            pass
    return backtrack, s[v_len][w_len]


# OUTPUTLCS(backtrack, v, i, j)
#     if i = 0 or j = 0
#         return
#     if backtracki, j = "↓"
#         OUTPUTLCS(backtrack, v, i - 1, j)
#     else if backtracki, j = "→"
#         OUTPUTLCS(backtrack, v, i, j - 1)
#     else
#         OUTPUTLCS(backtrack, v, i - 1, j - 1)
#         output vi
def output_lcs(backtrack, v, w, i, j, alignment):
    while i >= 0 and j >= 0:
        if backtrack[i][j] == "↘":
            alignment[v].append(v[i])
            alignment[w].append(w[j])
            i -= 1
            j -= 1
        elif backtrack[i][j] == "↓":
            alignment[v].append(v[i])
            alignment[w].append('-')
            i -= 1
        else:
            alignment[v].append('-')
            alignment[w].append(w[j])
            j -= 1
    while j < 0 <= i:
        alignment[v].append(v[i])
        alignment[w].append('-')
        i -= 1
    while i < 0 <= j:
        alignment[v].append('-')
        alignment[w].append(w[j])
        j -= 1
    alignment[v].reverse()
    alignment[w].reverse()


def parse_input_txt(file_name):
    with open(file_name) as f:
        v = f.readline().strip()
        w = f.readline().strip()
    return v, w


def main():
    v, w = sys.argv[1], sys.argv[2]
    backtrack, score = lcs_backtrack(v, w)
    alignment = {v: [], w: []}
    v_last, w_last = len(v) - 1, len(w) - 1
    output_lcs(backtrack, v, w, v_last, w_last, alignment)
    alignment_text = "".join(alignment[v]) + '\n' + "".join(alignment[w])
    print alignment_text


if __name__ == "__main__":
    main()
