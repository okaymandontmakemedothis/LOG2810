# import pdb; pdb.set_trace()
with open("./lexique1.txt", 'rU', encoding='latin-1') as f:
	for line in f.readlines():
		a = line.split()
		print(a[0])