import pyperclip

with open('final.txt', 'r') as f:
	text = f.read()
	pyperclip.copy(text)

# CHANGE ALL THE FILE PATHS TO THEIR FULL PATHS
