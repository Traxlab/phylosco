from urllib import request
protein = 'A0A069K5A3_9ACTN'
link = 'http://www.uniprot.org/uniprot/' + protein
site = str(request.urlopen(link).read())
print("Actino" in site)