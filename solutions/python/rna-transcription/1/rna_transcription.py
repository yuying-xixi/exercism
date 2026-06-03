"""
实现核苷酸配对
"""
def to_rna(dna_strand):
    """
    :param dna_strand(str) -给定的核苷酸
    :return :str -配对的核苷酸
    """

    dna_strand_collection = {"G":"C", "C":"G", "T":"A", "":"", "A":"U"}
    match_dna_strand = ""

    if dna_strand:
        for dna in dna_strand:
            match_dna_strand += dna_strand_collection.get(dna, "")

    return match_dna_strand