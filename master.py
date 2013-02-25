#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# imported libs
import Libraries.Muta as MUTA
import Libraries.Attributes as ATTRIBUTES
import Libraries.Folders as PATHS
import Strings.Build as BUILD
import Strings.Attributes as ATTRSTR

# system libs
import logging
import os

logging.basicConfig(level=BUILD.LOGGER)

class Master:
	def __init__(self):
		self.writefile = BUILD.MASTER_META_FILE
		PATHS.clear_file(self.writefile)
		self.filelist = PATHS.search_valid_files(BUILD.TEST_DIRECTORY_MASTER, BUILD.VALID_FILE_EXTENSIONS)
		self.generate_meta_master()

	def generate_meta_master(self):
		for filename in self.filelist:
			audio_file = MUTA.Audio(filename, BUILD.TEST_DIRECTORY_MASTER)
			logging.info("Reading file: "+audio_file.file_path)
			with open(self.writefile,'a') as mpy:
				logging.info("Writing attributes ...")
				mpy.write(ATTRSTR.FNAME.format(audio_file.file_path))
				for attr in ATTRIBUTES.attributes_list:
					mpy.write(ATTRSTR.ATTRIBUTE.format(ATTRIBUTES.write_attributes_ID3_map[attr],getattr(audio_file,attr)))


if __name__ == "__main__":
	Master()
