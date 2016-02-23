from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio import SeqIO

example_seqs = [
    'SRPAPVVLIILCVMAGVIGTILLISYGIRLLIK',
    'TVPAPVVIILIILCVMAGIIGTILLLIISYTIRRLIK',
    'HHFSEPEITLIIFGVMAGVIGTILLLIISYGIRLIK',
    'HFSELVIALIIFGVMAGVIGTILFISYGSRLIK'
]


def save_fasta_protein(seqs, fasta_file_name):
    records = []
    for i, seq in enumerate(seqs):
        seq_obj = Seq(seq, IUPAC.protein)
        name = 'test%d' % i
        record_obj = SeqRecord(seq_obj, id=name, description='demo only')
        records.append(record_obj)

    with open(fasta_file_name, "w") as out_file_obj:
        SeqIO.write(records, out_file_obj, "fasta")

save_fasta_protein(example_seqs, "example_seqs.fasta")
