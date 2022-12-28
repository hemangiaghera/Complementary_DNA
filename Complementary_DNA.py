dna_seq= "ATGCATCGATCGATCGACAGCT"
print("DNA sequence: " + dna_seq)
dna_seq1= dna_seq.replace("A","-")
dna_seq2= dna_seq1.replace("T","A")
dna_seq3= dna_seq2.replace("G","+")
dna_seq4= dna_seq3.replace("C","G")
dna_seq5= dna_seq4.replace("+","C")
dna_seq6= dna_seq5.replace("-","T")
print("Complementary sequence: " + dna_seq6)
