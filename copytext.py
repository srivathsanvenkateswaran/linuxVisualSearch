import pyperclip

with open('{INSERT THE FULL PATH OF FINAL.TXT HERE}', 'r') as f:
	text = f.read()
	pyperclip.copy(text)

