global terminal_character
terminal_character = "$"

class TrieNode:
	def __init__(self, character, previous):
		self.child = []
		self.character = character
		self.previous = previous





def insertWord(root, word):
	currentNode = root
	previousNode = None
	for character in word:
		newNode = TrieNode(character, previousNode)
		currentNode.child.append(newNode)
		previousNode = currentNode
		currentNode = newNode
	currentNode.child.append(TrieNode(terminal_character, previousNode))
    


def findWord(root, word):
	currentNode = root
	child = currentNode.child

	l = list();

	print(word) ##########
	for character in word:
		print("char#:",word.find(character)) ########## 
		if terminal_character in currentNode.child:
			print("term char enter!") ##########
			l.append(wordifyNode(child[child.index(terminal_character)]))
		if character in child :
			currentNode = child[child.index(character)]

	return l

def wordifyNode(leaf):
	word = ""
	while leaf.previous != None :
		currentNode = leaf.previous
		word.append(currentNode.character)
	return word



if __name__ == '__main__':
	print("booted up main") ##########

	root = TrieNode("", None)
	insertWord(root, "damn")
	insertWord(root, "damnit")
	l = findWord(root, "damniteery")
	for w in l:
		print("at least got smthing")
		print(w)
