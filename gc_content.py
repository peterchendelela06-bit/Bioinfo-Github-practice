gc_content.py
def calculate_gc_content(sequence):sequence=sequence.upper()
gc_count=sequence.count("G")+sequence.count("C")
gc_percentage=(gc_count/len(sequence))*100
return gc_percentage
dna_sequence="ATGCGTACCGTAATGCGTACCGTA"
gc=calculate_gc_content(dna_sequence)
print(DNA sequence:",dna_sequence)
print("GC content:", round(gc,2),"%"
