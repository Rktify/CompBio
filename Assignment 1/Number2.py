def translate_amino_acid(aminoAcid, table):
    codons = []
    for i in aminoAcid:
        found = False
        for codon, j in table.items():
            if i == j:
                codons.append(codon)
                found = True
                break
        if not found:
            break
    return ''.join(codons)

def count(mrna):
    sets = {}
    for i in range(0, len(mrna), 3):
        codon = mrna[i:i + 3]
        if codon in sets:
            sets[codon] += 1
        else:
            sets[codon] = 1
    return sets

table = {
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
    'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
    'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
    'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
    'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_',
    'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W',
}

aminoAcid = input("Input Aminoacid: ")
mrna = translate_amino_acid(aminoAcid, table)
codon_sets = count(mrna)

print(f"mRNA = {mrna}")
for codon, i in codon_sets.items():
    print(f"{codon} = {i}")
