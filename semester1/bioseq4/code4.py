import alingment as al

seqs = [
    'QPVHPFSRPAPVVIILIILCVMAGVIGTILLISYGIRLLIK',  # s0
    'QLVHRFTVPAPVVIILIILCVMAGIIGTILLISYTIRRLIK',  # s1
    'QLAHHFSEPEITLIIFGVMAGVIGTILLISYGIRRLIKKSPSDVKPLPSPD',  # s2
    'QLVHEFSELVIALIIFGVMAGVIGTILFISYGSRRLIKKSESDVQPLPPPD',  # s3
    'MLEHEFSAPVAILIILGVMAGIIGIILLISYSIGQIIKKRSVDIQPPEDED',  # s4
    'PIQHDFPALVMILIILGVMAGIIGTILLISYCISRMTKKSSVDIQSPEGGD',  # s5
    'QLVHIFSEPVIIGIIYAVMLGIIITILSIAFCIGQLTKKSSLPAQVASPED',  # s6
    'LAHDFSQPVITVIILGVMAGIIGIILLLAYVSRRLRKRPPADVP',  # s7
    'SYHQDFSHAEITGIIFAVMAGLLLIIFLIAYLIRRMIKKPLPVPKPQDSPD'  # s8
]


def seq_id(index):
    return 's' + str(index)


def distance_matrix(seqs_list):
    seqs_len = len(seqs_list)
    dm = {seq_id(i): {} for i, _ in enumerate(seqs_list)}

    for i in range(seqs_len):
        for j in range(i + 1, seqs_len):
            dm[seq_id(i)][seq_id(j)] = dm[seq_id(j)][seq_id(i)] = al.alignment_score(seqs_list[i], seqs_list[j])

    return dm


def q(dm, n1, n2):
    n = len(dm)
    sum1 = sum2 = 0
    for k in dm.iterkeys():
        if k != n1:
            sum1 += dm[n1][k]
        if k != n2:
            sum2 += dm[n2][k]
    result_q = (n - 2) * dm[n1][n2] - sum1 - sum2
    return result_q


def distance_matrix_to_q_matrix(dm):
    import copy
    qm = copy.deepcopy(dm)

    for i in dm.iterkeys():
        for j in dm[i].iterkeys():
            qm[i][j] = qm[j][i] = q(dm, i, j)
    return qm


def select_min_nodes(qm):
    n1 = qm.keys()[0]
    n2 = qm.keys()[1]
    min_val = qm[n1][n2]
    for i in qm.iterkeys():
        for j in qm[i].iterkeys():
            if qm[i][j] < min_val:
                n1 = i
                n2 = j
                min_val = qm[i][j]
    return n1, n2


def delta1(dm, n1, n2):
    n = len(dm)
    sum1 = sum2 = 0
    for k in dm.iterkeys():
        if k != n1:
            sum1 += dm[n1][k]
        if k != n2:
            sum2 += dm[n2][k]
    delta_result = float(dm[n1][n2]) / 2 + float(sum1 - sum2) / (2 * (n - 2))
    return delta_result


def delta2(dm, n1, n2, d1):
    return dm[n1][n2] - d1


def d_u_k(dm, k, n1, n2):
    return float(dm[n1][k] + dm[n2][k] - dm[n1][n2]) / 2


def new_dm(dm, n1, n2):
    new_node = '(' + n1 + '+' + n2 + ')'
    remain_nodes = (set(dm.keys()) - {n1, n2})
    remain_nodes = list(remain_nodes)
    dm2 = {k: {} for k in remain_nodes}

    for i in remain_nodes:
        for j in remain_nodes:
            if i != j:
                dm2[i][j] = dm2[j][i] = dm[i][j]

    dm2[new_node] = {}
    for i in remain_nodes:
        dm2[new_node][i] = dm2[i][new_node] = d_u_k(dm, i, n1, n2)

    return dm2


def construct_tree(dist_matrix):
    for i in range(len(dist_matrix) - 1):
        qm = distance_matrix_to_q_matrix(dist_matrix)
        n1, n2 = select_min_nodes(qm)
        dist_matrix = new_dm(dist_matrix, n1, n2)
    return dist_matrix.keys()[0]


def prepare_distance_matrix(dist_matrix):
    size_dm = len(dist_matrix)
    pdm = {}
    import string
    alphabet = list(string.ascii_lowercase)
    for i in range(size_dm):
        pdm_line = {}
        for j in range(size_dm):
            if j != i:
                pdm_line[alphabet[j]] = dist_matrix[i][j]
        pdm[alphabet[i]] = pdm_line
    return pdm
