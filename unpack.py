import py7zr
import os

#	Iterate over items in directory
#		If file is 7z archive, unpack
#		If dir, call this on it
def unpack(target_dir, password):
	for x in os.listdir(target_dir):
		new_path = os.path.join(target_dir, x)
		if os.path.isdir(new_path):
			print('\n/*****	Looking at: {}	*****/\n'.format(new_path))
			unpack(new_path, password)
		elif new_path.endswith('.7z'):
			print('Extracting:', new_path)
			with py7zr.SevenZipFile(new_path, 'r', password=password) as archive:
				archive.extractall()
			os.remove(new_path)
			print('Done.')