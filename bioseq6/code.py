from matplotlib import pyplot
from numpy import array, empty, identity, dot, ones, zeros, log


class HMM(object):
    @staticmethod
    def show_plot(sm):
        buried_list = []
        expose_list = []
        for values in sm:
            expose_list.append(sum(values[:20]))
            buried_list.append(sum(values[20:]))

        # Sequence positions
        x_axis_values = range(len(expose_list))

        pyplot.plot(x_axis_values, expose_list, c='#A0A0A0')
        pyplot.plot(x_axis_values, buried_list, c='#000000')
        pyplot.show()

    def __init__(self):
        self.exposure_types = ['-', '*']
        self.amino_acid_types = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                                 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
        self.exposure_size = len(self.exposure_types)  # Number of exposure categories
        self.amino_size = len(self.amino_acid_types)  # Number of amino acid types
        self.state_size = self.exposure_size * self.amino_size  # Number of HMM states

        self.p_emit = zeros((self.state_size, self.amino_size), float)  # Emission probabilities
        self.p_trans = zeros((self.state_size, self.state_size), float)  # Transition probabilities
        self.p_start = zeros(self.state_size, float)  # Starting probabilities

        self.state_dict = {}
        self.index_dict = {}

        self.initialisation()

    def initialisation(self):
        index = 0
        for exposure in self.exposure_types:
            for amino_acid in self.amino_acid_types:
                state_key = (exposure, amino_acid)
                self.index_dict[state_key] = index
                self.state_dict[index] = state_key
                index += 1

    def read(self, db):
        seq = db.readline()
        exposure = db.readline()
        while seq and exposure:
            index2 = 0
            for i in range(len(seq) - 2):
                aa1, aa2 = seq[i:i + 2]
                exp1, exp2 = exposure[i:i + 2]
                state_key1 = (exp1, aa1)
                state_key2 = (exp2, aa2)
                index1 = self.index_dict.get(state_key1)
                index2 = self.index_dict.get(state_key2)

                if index1 is None or index2 is None:
                    continue
                self.p_start[index1] += 1.0
                self.p_trans[index1, index2] += 1.0

            self.p_start[index2] += 1.0
            seq = db.readline().strip()
            exposure = db.readline().strip()

        self.p_start /= sum(self.p_start)
        for i in range(self.state_size):
            self.p_trans[i] /= sum(self.p_trans[i])

        # Setup trivial emission probabilities
        for exposure in self.exposure_types:
            for amino_index, amino_acid in enumerate(self.amino_acid_types):
                state_index = self.index_dict[(exposure, amino_acid)]
                self.p_emit[state_index, amino_index] = 1.0

    def best_route(self, seq):
        obs = [self.amino_acid_types.index(aa) for aa in seq]
        adj = 1e-99
        log_start = log(self.p_start + adj)
        log_trans = log(self.p_trans + adj)
        log_emit = log(self.p_emit + adj)

        # Best route - Viterbi
        _, path = viterbi(obs, log_start, log_trans, log_emit)
        best_exp_codes = ''.join([self.state_dict[i][0] for i in path])
        return best_exp_codes

    def pos_state_prob(self, seq):
        obs = [self.amino_acid_types.index(aa) for aa in seq]
        # Positional state probabilities - Forward-backward
        return forward_backward(obs, self.p_start, self.p_trans, self.p_emit)


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
    sm = empty([n + 1, n_states])
    sm[-1] = fwd[-1]

    for i in range(n - 1, -1, -1):
        bwd = dot(p_trans, dot(p_emit[:, obs[i]] * ident, bwd))
        bwd /= bwd.sum()
        prob = fwd[i] * bwd
        sm[i] = prob / prob.sum()
    return sm


if __name__ == '__main__':
    # HMM test example - protein burried/exposed states
    hmm = HMM()

    # Estimate transition probabilities from database counts
    database = open('PDBCategories.txt', 'r')
    hmm.read(database)

    # HMM test data
    sequence = "MYGKIIFVLLLSEIVSISASSTTGVAMHTSTSSSVTKSYISSQTNDTHKRDTYAATPRAH" \
               "EVSEISVRTVYPPEEETGERVQLAHHFSEPEITLIIFGVMAGVIGTILLISYGIRRLIKK" \
               "SPSDVKPLPSPDTDVPLSSVEIENPETSDQ"
    route = hmm.best_route(sequence)

    print(sequence)
    print(route)

    smooth = hmm.pos_state_prob(sequence)
    hmm.show_plot(smooth)
