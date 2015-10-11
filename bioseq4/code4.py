import alingment as al

seqs = [
    'QPVHPFSRPAPVVIILIILCVMAGVIGTILLISYGIRLLIK',
    'QLVHRFTVPAPVVIILIILCVMAGIIGTILLISYTIRRLIK',
    'QLAHHFSEPEITLIIFGVMAGVIGTILLISYGIRRLIKKSPSDVKPLPSPD',
    'QLVHEFSELVIALIIFGVMAGVIGTILFISYGSRRLIKKSESDVQPLPPPD',
    'MLEHEFSAPVAILIILGVMAGIIGIILLISYSIGQIIKKRSVDIQPPEDED',
    'PIQHDFPALVMILIILGVMAGIIGTILLISYCISRMTKKSSVDIQSPEGGD',
    'QLVHIFSEPVIIGIIYAVMLGIIITILSIAFCIGQLTKKSSLPAQVASPED',
    'LAHDFSQPVITVIILGVMAGIIGIILLLAYVSRRLRKRPPADVP',
    'SYHQDFSHAEITGIIFAVMAGLLLIIFLIAYLIRRMIKKPLPVPKPQDSPD'
]


def distance_matrix(seqs_list):
    seqs_len = len(seqs_list)
    dm = [[0] * seqs_len for _ in range(seqs_len)]

    for i in range(seqs_len):
        for j in range(i + 1, seqs_len):
            dm[i][j] = dm[j][i] = al.alignment_score(seqs_list[i], seqs_list[j])

    return dm


def q(dm, i, j):
    n = len(dm)
    sum1 = sum2 = 0
    for k in range(n):
        sum1 += dm[i][k]
        sum2 += dm[j][k]
    result_q = (n - 2) * dm[i][j] - sum1 - sum2
    return result_q


def distance_matrix_to_q_matrix(dm):
    dm_size = len(dm)
    qm = [[0] * dm_size for _ in range(dm_size)]

    for i in range(dm_size):
        for j in range(i + 1, dm_size):
            qm[i][j] = qm[j][i] = q(dm, i, j)
    return qm


def select_min_nodes(qm):
    qm_size = len(qm)
    ind1 = 0
    ind2 = 1
    min_val = qm[ind1][ind2]
    for i in range(qm_size):
        for j in range(i + 1, qm_size):
            if qm[i][j] < min_val:
                ind1 = i
                ind2 = j
                min_val = qm[i][j]
    return ind1, ind2


def delta1(dm, ind1, ind2):
    n = len(dm)
    sum1 = sum2 = 0
    for k in range(n):
        sum1 += dm[ind1][k]
        sum2 += dm[ind2][k]
    delta_result = float(dm[ind1][ind2]) / 2 + float(sum1 - sum2) / (2 * (n - 2))
    return delta_result


def delta2(dm, a_index, b_index, delta1_value):
    return dm[a_index][b_index] - delta1_value
