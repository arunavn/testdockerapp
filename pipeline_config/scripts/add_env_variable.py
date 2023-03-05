import json
import os
with open('./pipeline_config/configs/pipeline_config.json', 'r') as f:
	CONFIG_DICT = json.load(f)

def set_all_variables(env_dict):
	for k,v in env_dict:
		os.environ[k] = str(v)	

def main():
	global CONFIG_DICT
	print(f"cwd: {os.getcwd()}")
	print(CONFIG_DICT)
	env_dict = CONFIG_DICT['test']['env_dict']
	set_all_variables(env_dict)  

if __name__ == '__main__':
	main()
