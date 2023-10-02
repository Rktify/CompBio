def translate_codon(cod):
    tc = {
        "UUU": "Phe (F)", "UUC": "Phe (F)", "UUA": "Leu (L)", "UUG": "Leu (L)",
        "UCU": "Ser (S)", "UCC": "Ser (S)", "UCA": "Ser (S)", "UCG": "Ser (S)",
        "UAU": "Tyr (Y)", "UAC": "Tyr (Y)", "UAA": "_", "UAG": "_",
        "UGU": "Cys (C)", "UGC": "Cys (C)", "UGA": "_", "UGG": "Trp (W)",
        "CUU": "Leu (L)", "CUC": "Leu (L)", "CUA": "Leu (L)", "CUG": "Leu (L)",
        "CCU": "Pro (P)", "CCC": "Pro (P)", "CCA": "Pro (P)", "CCG": "Pro (P)",
        "CAU": "His (H)", "CAC": "His (H)", "CAA": "Gln (Q)", "CAG": "Gln (Q)",
        "CGU": "Arg (R)", "CGC": "Arg (R)", "CGA": "Arg (R)", "CGG": "Arg (R)",
        "AUU": "Ile (I)", "AUC": "Ile (I)", "AUA": "Ile (I)", "AUG": "Met (M)",
        "ACU": "Thr (T)", "ACC": "Thr (T)", "ACA": "Thr (T)", "ACG": "Thr (T)",
        "AAU": "Asn (N)", "AAC": "Asn (N)", "AAA": "Lys (K)", "AAG": "Lys (K)",
        "AGU": "Ser (S)", "AGC": "Ser (S)", "AGA": "Arg (R)", "AGG": "Arg (R)",
        "GUU": "Val (V)", "GUC": "Val (V)", "GUA": "Val (V)", "GUG": "Val (V)",
        "GCU": "Ala (A)", "GCC": "Ala (A)", "GCA": "Ala (A)", "GCG": "Ala (A)",
        "GAU": "Asp (D)", "GAC": "Asp (D)", "GAA": "Glu (E)", "GAG": "Glu (E)",
        "GGU": "Gly (G)", "GGC": "Gly (G)", "GGA": "Gly (G)", "GGG": "Gly (G)",
    }

    if cod in tc:
        return tc[cod]
    else:
        return None

def complement_dna(dna):
    complementDict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement = ""
    for i in dna:
        complement += complementDict[i]
    return complement

def transcribe_dna_mrna(dna):
    return dna.replace('T', 'U')

def translate_mrna_acid(mrna):
    aminoAcids = []

    for i in range(0, len(mrna), 3):
        codon = mrna[i:i + 3]
        aminoAcid = translate_codon(codon)
        if aminoAcid:
            aminoAcids.append(aminoAcid)

    return aminoAcids


input_dna = input("Input DNA: ")

complement = complement_dna(input_dna)
mrna = transcribe_dna_mrna(complement)
amino_acids = translate_mrna_acid(mrna)

print("")
print(f"Complement = {complement}")
print(f"mRNA = {mrna}")
print(f"Amino Acid = {' - '.join(amino_acids)}")

