#!/usr/bin/env python
import os
import string

src_dir = os.getcwd()
for file_name in os.listdir(src_dir):
	if '.jpg' in file_name:
		new_file_name = ''.join(c for c in file_name if c in string.printable)
		os.rename(os.path.join(src_dir,file_name),os.path.join(src_dir, new_file_name))




