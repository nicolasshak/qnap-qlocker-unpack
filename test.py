import os
import shutil
import py7zr
from unpack import unpack

def test_unpack():

	current_dir = os.path.curdir
	shutil.rmtree(os.path.join(current_dir, 'test'))
	test_dir = create_dir(current_dir, 'test')

	# 1. Multiple folder levels
	test_dir_1 = create_dir(test_dir, 'test1')
	sub_1 = create_dir(test_dir_1, 'sub1')

	sub_11 = create_dir(sub_1, 'sub1:1')
	create_archive_files(sub_11, 'archive', 2)

	sub_12 = create_dir(sub_1, 'sub1:2')
	create_archive_files(sub_12, 'archive', 1)
	create_files(sub_12, 'file', 1)
	sub_121 = create_dir(sub_12, 'sub1:2:1')
	create_archive_files(sub_121, 'archive', 2)

	sub_2 = create_dir(test_dir_1, 'sub2')

	# 2. All sub folders
	test_dir_2 = create_dir(test_dir, 'test2')
	for x in range(0, 3):
		test_2_subdir = create_dir(test_dir_2, 'subfolder{}'.format(x))
		create_archive_files(test_2_subdir, 'archive', 3)


	# 3. Mix of archives and sub folders
	test_dir_3 = create_dir(test_dir, 'test3')
	for x in range(0, 3):
		test_3_subdir = create_dir(test_dir_3, 'subfolder{}'.format(x))
		create_archive_files(test_3_subdir, 'archive', 3)
	create_archive_files(test_dir_3, 'archive', 2)

	# 4. All archives
	test_dir_4 = create_dir(test_dir, 'test4')
	create_archive_files(test_dir_4, 'archive', 4)

	# 5. Mix of archives and files
	test_dir_5 = create_dir(test_dir, 'test5')
	create_archive_files(test_dir_5, 'archive', 3)
	create_files(test_dir_5, 'file', 2)


	unpack(os.path.join(os.path.curdir, 'test'), 'test')


def create_files(path, name, num):
	for x in range(0, num):
		file_name = '{}{}.txt'.format(name, x)
		file_path = os.path.join(path, file_name)
		with open(file_path, 'w') as file:
			file.write('This is file number {} from: {}'.format(x, path))
			file.close()

def create_dir(path, name):
	dir_path = os.path.join(path, name)
	os.mkdir(dir_path)
	return dir_path

def archive_file(path, password):
	archive_path = path.replace('.txt', '.7z')
	with py7zr.SevenZipFile(archive_path, 'w', password=password) as archive:
		archive.write(path, path.split()[-1])
	os.remove(path)

def create_archive_files(path, name, num):
	create_files(path, name, num)
	for x in range(0, num):
		archive_file(os.path.join(path, '{}{}.txt'.format(name, x)), 'test')
	

if __name__ == "__main__":
	#create_folders()
	test_unpack()