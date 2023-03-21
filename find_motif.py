import re
from Bio import SeqIO
import argparse

parse = argparse.ArgumentParser(description='Input and output file path.')

parse.add_argument('--motif', '-m', help='The motif file path.')
parse.add_argument('--reference', '-r', help='The reference file path.')

args = parse.parse_args()


def findMotifs(motif, reference):
    'Find the number of occurrences of a motif in the reference sequence.'
    for motif_record in SeqIO.parse(motif, "fasta"):
        for ref_record in SeqIO.parse(reference, "fasta"):
            result = re.findall(str(motif_record.seq), str(ref_record.seq), flags=re.I | re.M)
            start = []
            end = []
            for i in re.finditer(str(motif_record.seq), str(ref_record.seq), flags=re.I | re.M):
                start.append(i.start())
                end.append(i.end())
            if len(result) == 1:
                words = "There is a motif in the reference sequence."
            elif len(result) > 1:
                words = f"There are {len(result)} motifs in the reference sequence."
            else:
                words = "Not found."
            start = [i + 1 for i in start]
            end = [i + 1 for i in end]
            return words, start, end


words, start, end = findMotifs(args.motif, args.reference)
print(words)
for start, end in zip(start, end):
    print(f"From {start} to {end} is a motif.")
