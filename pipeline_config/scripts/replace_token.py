import re
import json
import os
CONFIG_DICT = {}

def replacetext(s_regex, file_path):
	global CONFIG_DICT
	# Opening the file in read and write mode
	with open('SampleFile.txt','r+') as f:
		file = f.read()
		# Replacing the pattern with the string in the file data
		file = re.sub(search_text, replace_text, file)
		f.seek(0)
		f.write(file)
		f.truncate()

def main():
	print(f"cwd: {os.getcwd()}")
	tokens = {'hello': 'world'}
	s_regex=re.compile("|".join([r"#<{}>".format(t) for t in tokens]))
  
  

if __name__ == '__main__':
	main()
 
