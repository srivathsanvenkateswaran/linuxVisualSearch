import pyperclip

with open('final.txt', 'r') as f:
	text = f.read()
	pyperclip.copy(text)

