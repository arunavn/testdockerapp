import re
import json
import os
import sys
with open('./pipeline_config/configs/pipeline_config.json', 'r') as f:
	CONFIG_DICT = json.load(f)

def replacetext(s_regex, file_path, replace_dicts):
	# Opening the file in read and write mode
	with open(file_path,'r+') as f:
		file = f.read()
		# Replacing the pattern with the string in the file data
		file = s_regex.sub(lambda m: replace_dicts[m.group(0)], file)
		f.seek(0)
		f.write(file)
		f.truncate()

def main():
	global CONFIG_DICT
	env = sys.argv[0]
	tokens = CONFIG_DICT[env]['config_dict']
	token_updated = {}
	for k, v in tokens.items():
		token_updated[f"#<{k}>#"] = v
	s_regex=re.compile("|".join([r"{}".format(t) for t in token_updated]))
	for f_path in CONFIG_DICT['replaceFileList']:
		replacetext(s_regex= s_regex, file_path= f_path, replace_dicts= token_updated)
	  

if __name__ == '__main__':
	main()
 
