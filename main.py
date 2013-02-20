#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# imported libs
import muta
import lib

# system libs
import logging
import os
import os.path as Path


logging.basicConfig(level=logging.INFO)

TEST_DIRECTORY = u'..\\Test Music\\'

write_attributes_ID3_map = lib.Attributes().write_attributes_ID3_map


class Meta:
	def __init__(self, writefile):
		self.writefile = writefile
		self.valid_file_extensions = [u'flac', u'alac', u'mp3']
		self.filelist = self._search_valid_files(self.valid_file_extensions)
		self.generate_meta_master()


	def generate_meta_master(self):
		for filename in self.filelist:
			audio_file = muta.Audio(filename)
			with open(self.writefile,'a') as mpy:
				mpy.write("$$$FNAME:"+audio_file.file_path+"\n")
				for attr in lib.Attributes().attributes_list:
					mpy.write("$["+write_attributes_ID3_map[attr]+"]::"+getattr(audio_file,attr)+"\n")

	def _search_valid_files(self,valid_extensions):
		filelist = []
		for root, dirs, files in os.walk(TEST_DIRECTORY):
			for f in files:
				if f.split(u'.')[-1] in valid_extensions:
					filelist.append(os.path.abspath(os.path.join(root.encode(u'utf-8'), f.encode(u'utf-8'))))
		return filelist



def generate_meta_slave():
	pass




if __name__ == "__main__":
	Meta("random.txt")
