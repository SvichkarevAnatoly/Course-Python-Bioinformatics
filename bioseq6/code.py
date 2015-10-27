from matplotlib import pyplot
from numpy import array, empty, identity, dot, ones, zeros, log


def comb(n, k):
    if (k > n) or (n < 0) or (k < 0):
        return 0L
    nn, kk = map(long, (n, k))
    top = n
    val = 1L
    while top > (nn - kk):
        val *= top
        top -= 1
    nn = 1L
    while nn < kk + 1L:
        val /= n
        n += 1
    return val


def binomial_probability(n, k, p):
    return comb(n, k) * p ** k * (1 - p) ** (n - k)


def get_next_gen_pop(current_pop, rand_var):
    progeny = rand_var.rvs(size=current_pop)
    next_pop = progeny.sum()
    return next_pop


def viterbi(obs, p_start, p_trans, p_emit):
    n_states = len(p_start)
    states = range(n_states)
    scores = empty(n_states)
    scores_prev = p_start + p_emit[:, obs[0]]
    paths_prev = dict([(i, [i]) for i in states])

    paths = {}
    for val in obs[1:]:
        paths = {}

        for i in states:
            options = scores_prev + p_trans[:, i] + p_emit[i, val]
            best_state = options.argmax()
            scores[i] = options.max()
            paths[i] = paths_prev[best_state] + [i]

        paths_prev = paths
        scores_prev = array(scores)

    end_state = scores.argmax()
    log_prob = scores.max()

    return log_prob, paths[end_state]


def forward_backward(obs, p_start, p_trans, p_emit):
    n = len(obs)
    n_states = len(p_start)
    ident = identity(n_states)

    fwd = empty([n + 1, n_states])
    fwd[0] = p_start

    for i, val in enumerate(obs):
        f_prob = dot(p_emit[:, val] * ident, dot(p_trans, fwd[i]))
        fwd[i + 1] = f_prob / f_prob.sum()

    bwd = ones(n_states)
    smooth = empty([n + 1, n_states])
    smooth[-1] = fwd[-1]

    for i in range(n - 1, -1, -1):
        bwd = dot(p_trans, dot(p_emit[:, obs[i]] * ident, bwd))
        bwd /= bwd.sum()
        prob = fwd[i] * bwd
        smooth[i] = prob / prob.sum()

    return smooth


if __name__ == '__main__':
    # HMM test example - protein burried/exposed states
    exposure_types = ['-', '*']
    amino_acid_types = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                        'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

    # Initialisation
    exposure_size = len(exposure_types)  # Number of exposure categories
    amino_size = len(amino_acid_types)  # Number of amino acid types
    state_size = exposure_size * amino_size  # Number of HMM states

    p_start = zeros(state_size, float)  # Starting probabilities
    p_trans = zeros((state_size, state_size), float)  # Transition probabilities
    p_emit = zeros((state_size, amino_size), float)  # Emission probabilities

    index_dict = {}
    state_dict = {}
    index = 0
    for exposure in exposure_types:
        for amino_acid in amino_acid_types:
            state_key = (exposure, amino_acid)
            index_dict[state_key] = index
            state_dict[index] = state_key
            index += 1

    # Estimate transition probabilities from database counts
    database = open('PDBCategories.txt', 'r')

    sequence = database.readline()
    exposure = database.readline()
    while sequence and exposure:
        index2 = 0
        for i in range(len(sequence) - 2):
            aa1, aa2 = sequence[i:i + 2]
            exp1, exp2 = exposure[i:i + 2]
            state_key1 = (exp1, aa1)
            state_key2 = (exp2, aa2)
            index1 = index_dict.get(state_key1)
            index2 = index_dict.get(state_key2)

            if index1 is None or index2 is None:
                continue

            p_start[index1] += 1.0
            p_trans[index1, index2] += 1.0

        p_start[index2] += 1.0
        sequence = database.readline().strip()
        exposure = database.readline().strip()

    p_start /= sum(p_start)
    for i in range(state_size):
        p_trans[i] /= sum(p_trans[i])

    # Setup trivial emission probabilities
    for exposure in exposure_types:
        for amino_index, amino_acid in enumerate(amino_acid_types):
            state_index = index_dict[(exposure, amino_acid)]
            p_emit[state_index, amino_index] = 1.0

    # HMM test data
    seq = "MYGKIIFVLLLSEIVSISASSTTGVAMHTSTSSSVTKSYISSQTNDTHKRDTYAATPRAH" \
          "EVSEISVRTVYPPEEETGERVQLAHHFSEPEITLIIFGVMAGVIGTILLISYGIRRLIKK" \
          "SPSDVKPLPSPDTDVPLSSVEIENPETSDQ"

    obs = [amino_acid_types.index(aa) for aa in seq]
    adj = 1e-99
    log_start = log(p_start + adj)
    log_trans = log(p_trans + adj)
    log_emit = log(p_emit + adj)

    # Best route - Viterbi
    _, path = viterbi(obs, log_start, log_trans, log_emit)
    best_exp_codes = ''.join([state_dict[i][0] for i in path])

    print(seq)
    print(best_exp_codes)

    # Positional state probabilities - Forward-backward
    smooth = forward_backward(obs, p_start, p_trans, p_emit)

    buried_list = []
    expose_list = []
    for values in smooth:
        expose_list.append(sum(values[:20]))
        buried_list.append(sum(values[20:]))

    # Sequence positions
    x_axis_values = range(len(expose_list))

    pyplot.plot(x_axis_values, expose_list, c='#A0A0A0')
    pyplot.plot(x_axis_values, buried_list, c='#000000')
    pyplot.show()
