#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import mutagen
# from mutagen.mp3 import MP3
# from mutagen.id3 import ID3, TIT2
# from mutagen.flac import FLAC
# from mutagen.m4a import M4A

import os.path as Path




class audio:
	def __init__(self, filepath):
		filepath = Path.realpath(filepath)
		self.attributes = ["album","albumartist","artist","tracknumber","title","genre","date","comment"]
		self.attributes_ID3_map = {
			"album":"TALB",
			"albumartist":"TPE2",
			"artist":"TPE1",
			"date":"TDRC",
			"discnumber":"TPOS",
			"genre":"TCON",
			"title":"TIT2",
			"tracknumber":"TRCK",
			"comment":"COMM::'eng'"
		}
		self.file_path = Path.relpath(filepath)
		self.file_type = self._find_file_type(self.file_path)
		self.container = self._create_mutagen()

		for attr in self.attributes:
			setattr(self, attr, self.get_attribute(attr))

	def get_attribute(self, attr):
		call = attr
		if self.file_type in ['mp3']:
			call = self.attributes_ID3_map[attr]

		try:
			attr_ret = self.container[call]
		except KeyError:
			print "Could not find attribute."
			attr_ret = ""

		return attr_ret

	def set_attribute(self, attr, value):
		call = attr
		if self.file_type in ['mp3']:
			print


	def _create_mutagen(self):
		t = self.file_type
		f = self.file_path.decode(u'utf-8')

		supported_types = ['mp3','flac','alac']
		if t not in supported_types:
			throw('File type not supported.')

		return mutagen.File(f,easy=False)

	def _find_file_type(self, filepath):
		return Path.splitext(Path.basename(filepath))[1].lstrip(".").lower()



