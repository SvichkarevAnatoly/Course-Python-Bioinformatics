from Bio import AlignIO


def read_alignment(align_file_name):
    file_obj = open(align_file_name)
    result = AlignIO.read(file_obj, "clustal")
    return result


alignment = read_alignment("out.aln")

print("Alignment length %i" % alignment.get_alignment_length())
for record in alignment:
    print record.seq, record.id


def write_phylip(align, phylip_file_name):
    file_obj = open(phylip_file_name, "w")
    AlignIO.write(align, file_obj, "phylip")


write_phylip(alignment, "out.phylip")
