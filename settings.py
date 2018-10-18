def init():
	global return_value
	return_value = ""
	global data
	data = None
	global never_quit_filename_loop
	never_quit_filename_loop = True
	global choices
	choices = ["(a) Mettre a jour la carte.","(b) Determiner le plus court chemin securitaire.","(c) Extraire un sous-graphe.","(d) Quitter."]
