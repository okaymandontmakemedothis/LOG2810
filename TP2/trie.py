#https://stackoverflow.com/questions/5169702/how-do-i-list-the-current-line-in-python-pdb
import asyncio
import sys

global terminal_character
terminal_character = "$"

count = 0

global TrieNode_Queue
TrieNode_Queue = []

class TrieNode:

	def __init__(self, character, previous): #, next=None
		self.child = []
		self.character = character
		self.previous = previous #should be an integer for index
		self.wordcount = 0

	# def returnQueue(self):
	# 	return self.TrieNode_Queue


def insertWord(root, word):
	previousNode = root
	for index, character in enumerate(word):
		if character not in childToString(previousNode.child):
			previousNode = insertNode(previousNode, character)
		else:
			if index+1 < len(word):
				try:
					previousNode = previousNode.child[findCharacterIndex(previousNode,character)]
				except Exception as e:
					#if character does not exist in previousNode.child
					previousNode = insertNode(previousNode, character)
					pass
			else:
				return
	previousNode.child.append(TrieNode(terminal_character, previousNode))
	root.wordcount+=1

def findWord(root, word):
	global TrieNode_Queue
	l = list();
	stack = list();
	# currentNode = root
	tipNode = travelToCurrentInput(root, word)

	#So basically the 0-indexed element is the oldest element and the 4-indexed element is the newest one
	global count
	if terminal_character in childToString(tipNode):
		if count == 5:
			TrieNode_Queue.pop(0)
			TrieNode_Queue.push(tipNode)
		elif count < 5:
			TrieNode_Queue.push(tipNode)
			count+=1

	stack.append(tipNode)
	#TUPLE SHAPE : (word, wordcount)
	while stack:
		a = stack.pop()

		if terminal_character in childToString(a.child):
			if len(a.child) == 1:
				l.append((wordifyNode(a.child[findCharacterIndex(a, terminal_character)])[::-1], a.wordcount))
			else:
				l.append( ( wordifyNode(a.child[findCharacterIndex(a, terminal_character)])[::-1], a.wordcount ) )
				for n in reversed(a.child):
					if n.character != terminal_character:
						stack.append(n)
		else:
			for n in reversed(a.child):
				stack.append(n)
	return l

#UTILITY FUNCTIONS


def travelToCurrentInput(currentNode, word):
	for index, character in enumerate(word, 1):
		if character in childToString(currentNode.child):
			currentNode = currentNode.child[findCharacterIndex(currentNode, character)]
		else:
			# Return the position of the character and the length of the word
			raise ValueError(len(word) - index, "take that character away it doesn't exist")
	if terminal_character in childToString(currentNode.child):
		currentNode.wordcount += 1
	return currentNode

def childToString(child):
	string = ""
	for node in child:
		string+=node.character
	return string

def findCharacterIndex(node, character):
	for n in node.child:
		if n.character == character:
			return node.child.index(n)
	return -1

def insertNode(previousNode, character):
	currentNode = TrieNode(character, previousNode)
	previousNode.child.append(currentNode)
	return currentNode

def wordifyNode(leaf):
	word = ""
	while leaf.previous != None :
		leaf = leaf.previous
		word+=leaf.character
	return word

# global l

# async def countPrint():
#     global l
#     for w in l:
#         a,b = w
#         if b == 0 :
#             pass
#         else:
#             print()
#             print(a," (",b,")")

#MAIN

# async def main():
# 	global l
# 	print("booted up main") ##########

# 	root = TrieNode("", None)
# 	#DOUBLE INSERT WORDS DO NOT WORK
# 	insertWord(root, "damn")
# 	# # import pdb; pdb.set_trace()
# 	insertWord(root, "damn")
# 	insertWord(root, "damnish")
# 	insertWord(root, "damniadhaskshad")
# 	insertWord(root, "damnit")
# 	insertWord(root, "damnithhfjkhek")

# 	l = list();
# 	try:
# 		l = findWord(root, "damn")
# 		await countPrint()
# 	except Exception as e:
# 		#implement how to backspace
# 		print(e.args)
# 	for w in l:
# 		# print("at least got smthing")
# 		print(w)

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()