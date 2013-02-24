#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# imported libs
import muta
import Libraries.Attributes as ATTRIBUTES
import Libraries.Folders as PATHS
import Strings.Build as BUILD

# system libs
import logging

logging.basicConfig(level=BUILD.LOGGER)

class Master:
	def __init__(self, writefile):
		self.writefile = writefile
		self.valid_file_extensions = [u'flac', u'alac', u'mp3']
		PATHS.clear_file(self.writefile)
		self.filelist = PATHS.search_valid_files(self.valid_file_extensions,BUILD.TEST_DIRECTORY_MASTER)
		self.generate_meta_master()

	def generate_meta_master(self):
		for filename in self.filelist:
			audio_file = muta.Audio(filename)
			logging.info("Reading file: "+audio_file.file_path)
			with open(self.writefile,'a') as mpy:
				logging.info("Writing attributes to: "+self.writefile)
				mpy.write("$$$FNAME:"+audio_file.file_path+"\n")
				for attr in ATTRIBUTES.attributes_list:
					mpy.write("$["+ATTRIBUTES.write_attributes_ID3_map[attr]+"]::"+getattr(audio_file,attr)+"\n")


if __name__ == "__main__":
	Master(BUILD.MASTER_META_FILE)
