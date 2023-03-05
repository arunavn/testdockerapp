import re
import json
import os
with open('./pipeline_config/configs/pipeline_config.json', 'r') as f:
	CONFIG_DICT = json.load(f)

def replacetext(s_regex, file_path):
	global CONFIG_DICT
	# Opening the file in read and write mode
	with open('SampleFile.txt','r+') as f:
		file = f.read()
		# Replacing the pattern with the string in the file data
		file = s_regex.sub(lambda m: tokens[m.group(0)], file)
		f.seek(0)
		f.write(file)
		f.truncate()

def main():
	global CONFIG_DICT
	print(f"cwd: {os.getcwd()}")
	print(CONFIG_DICT)
	tokens = CONFIG_DICT['test']['config_dict']
	s_regex=re.compile("|".join([r"#<{}>#".format(t) for t in tokens]))
	for f_path in CONFIG_DICT['replaceFileList']:
		replacetext(s_regex= s_regex, file_path= f_path)
	  

if __name__ == '__main__':
	main()
 
