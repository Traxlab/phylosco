from urllib import request
from Bio import SeqIO
#protein = 'A0A069K5A3_9ACTN'

def filter_sequences(fasta_file, filter_word):

	record = SeqIO.parse(fasta_file, "fasta")
	new_fasta_file_name = fasta_file.split(".")[0] + "_filtered.fasta"
	with open(new_fasta_file_name, "w") as new_file: 
		for sequence in record:
			temp_seq_name = sequence.id.split("/")[0]
			link = 'http://www.uniprot.org/uniprot/' + temp_seq_name
			site = str(request.urlopen(link).read())
			if filter_word not in site:
				temp_seq_sequence = str(sequence.seq)
				new_file.write(">"+temp_seq_name)
				new_file.write(temp_seq_sequence)

filter_sequences("PF00616_full.txt", "Actino")
