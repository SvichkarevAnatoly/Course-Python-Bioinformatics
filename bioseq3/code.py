def consensus(seqs, percent_threshold=25):
    no_consensus = 'X'
    length = max(len(seq) for seq in seqs)
    result = ""
    for i in range(length):
        frequencies = {}
        for j in range(len(seqs)):
            if i < len(seqs[j]):
                symbol = seqs[j][i]
                if symbol in frequencies:
                    frequencies[symbol] += 1
                else:
                    frequencies[symbol] = 1
        most_frequent_symbol = max(frequencies, key=frequencies.get)
        sum_frequencies = sum(frequencies.values())
        symbol_percent = frequencies[most_frequent_symbol] * 100 / float(sum_frequencies)
        if symbol_percent > percent_threshold:
            result += most_frequent_symbol
        else:
            result += no_consensus
    return result
