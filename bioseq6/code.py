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
    expTypes = ['-', '*', ]
    aaTypes = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
               'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

    # Initialisation
    nExp = len(expTypes)  # Number of exposure categories
    nAmino = len(aaTypes)  # Number of amino acid types
    nStates = nExp * nAmino  # Number of HMM states

    pStart = zeros(nStates, float)  # Starting probabilities
    pTrans = zeros((nStates, nStates), float)  # Transition probabilities
    pEmit = zeros((nStates, nAmino), float)  # Emission probabilities

    indexDict = {}
    stateDict = {}
    index = 0
    for exposure in expTypes:
        for aminoAcid in aaTypes:
            stateKey = (exposure, aminoAcid)
            indexDict[stateKey] = index
            stateDict[index] = stateKey
            index += 1

    # Estimate transition probabilities from database counts

    # fileName = 'examples/PdbSeqExposureCategories.txt'
    fileName = 'PDBCategories.txt'
    fileObj = open(fileName, 'r')

    line1 = fileObj.readline()
    line2 = fileObj.readline()

    while line1 and line2:
        sequence = line1.strip()
        exposure = line2.strip()

        n = len(sequence)
        index2 = 0
        for i in range(n - 2):
            aa1, aa2 = sequence[i:i + 2]
            exp1, exp2 = exposure[i:i + 2]
            stateKey1 = (exp1, aa1)
            stateKey2 = (exp2, aa2)
            index1 = indexDict.get(stateKey1)
            index2 = indexDict.get(stateKey2)

            if index1 is None or index2 is None:
                continue

            pStart[index1] += 1.0
            pTrans[index1, index2] += 1.0

        pStart[index2] += 1
        line1 = fileObj.readline()
        line2 = fileObj.readline()

    pStart /= pStart.sum()
    for i in range(nStates):
        pTrans[i] /= pTrans[i].sum()

    # Setup trivial emission probabilities

    for exposure in expTypes:
        for aminoIndex, aminoAcid in enumerate(aaTypes):
            stateIndex = indexDict[(exposure, aminoAcid)]
            pEmit[stateIndex, aminoIndex] = 1.0
            print ("Emit:", aminoAcid, stateIndex, aminoIndex, pEmit[stateIndex, aminoIndex])

    # HMM test data
    seq = "MYGKIIFVLLLSEIVSISASSTTGVAMHTSTSSSVTKSYISSQTNDTHKRDTYAATPRAH" \
          "EVSEISVRTVYPPEEETGERVQLAHHFSEPEITLIIFGVMAGVIGTILLISYGIRRLIKK" \
          "SPSDVKPLPSPDTDVPLSSVEIENPETSDQ"

    obs = [aaTypes.index(aa) for aa in seq]

    adj = 1e-99
    logStart = log(pStart + adj)
    logTrans = log(pTrans + adj)
    logEmit = log(pEmit + adj)

    # Best route - Viterbi
    logProbScore, path = viterbi(obs, logStart, logTrans, logEmit)

    bestExpCodes = ''.join([stateDict[i][0] for i in path])

    print(seq)
    print(bestExpCodes)

    # Positional state probabilitied - Forward-backward
    smooth = forward_backward(obs, pStart, pTrans, pEmit)

    buriedList = []
    exposeList = []

    for values in smooth:
        exposeList.append(sum(values[:20]))
        buriedList.append(sum(values[20:]))

    xAxisValues = list(range(len(exposeList)))  # Sequence positions

    pyplot.plot(xAxisValues, exposeList, c='#A0A0A0')
    pyplot.plot(xAxisValues, buriedList, c='#000000')
    pyplot.show()
