from subprocess import call


def run_clustalw(fasta_file_name, align_file_name):
    cmd_args = [
        'clustalw2',
        '-INFILE=' + fasta_file_name,
        '-OUTFILE=' + align_file_name
    ]
    call(cmd_args)

run_clustalw("example_seqs.fasta", "out.aln")
