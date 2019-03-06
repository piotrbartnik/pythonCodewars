#replace in string and firts use of regexp in python
def DNAtoRNA(dna):
  return dna.replace(r'T', 'U')

DNAtoRNA("GCATT")