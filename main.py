#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys, logging
import muta


logging.basicConfig(level=logging.INFO)
TEST_DIRECTORY = u'..\\Test Music\\'

def search_valid_files(valid_extensions):
	filelist = []
	for root, dirs, files in os.walk(TEST_DIRECTORY):
		for f in files:
			if f.split(u'.')[-1] in valid_extensions:
				filelist.append(os.path.abspath(os.path.join(root.encode(u'utf-8'), f.encode(u'utf-8'))))
	return filelist


if __name__ == "__main__":
	pass

valid_file_extensions = [u'flac', u'alac' ,u'mp3']

filelist = search_valid_files(valid_file_extensions)


for f in filelist:
	logging.info("##FILE## "+f)
	c = muta.audio(f)
	logging.info("comment:"+str(c.comment))

	# if isinstance(c, (list,tuple)):
	# 	for cc in c:
	# 		print cc
	# else:
	# 	print c
	#print muta.audio(f).container.pprint().encode(u'utf-8')

def generate_meta_master():
	pass


def generate_meta_slave():
	pass
