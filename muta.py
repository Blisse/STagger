#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import mutagen

from mutagen.id3 import ID3
from mutagen.id3 import TIT2, TALB, TPE1, TPE2, COMM, TCON, TDRC, TRCK, TPOS


import os.path as Path

import logging

read_attributes_ID3_map = {
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
write_attributes_ID3_map = {
	"album":"TALB",
	"albumartist":"TPE2",
	"artist":"TPE1",
	"date":"TDRC",
	"discnumber":"TPOS",
	"genre":"TCON",
	"title":"TIT2",
	"tracknumber":"TRCK",
	"comment":"COMM"
}
call_ID3_map = {
	"TALB":TALB,
	"TPE2":TPE2,
	"TPE1":TPE1,
	"TDRC":TDRC,
	"TPOS":TPOS,
	"TCON":TCON,
	"TIT2":TIT2,
	"TRCK":TRCK,
	"COMM":COMM
}

class audio:
	def __init__(self, filepath):
		filepath = Path.realpath(filepath)
		self.attributes = ["album","albumartist","artist","tracknumber","title","genre","date","comment"]
		self.file_path = Path.relpath(filepath)
		self.file_type = self._find_file_type(self.file_path)
		self.container = self._create_mutagen()

		logging.debug("Mapping file attributes to audio object")
		for attr in self.attributes:
			setattr(self, attr, self.get_attribute(attr))
		logging.debug("Audio object created successfully")
		return

	def get_attribute(self, attr):
		call = attr
		if self.file_type in ['mp3']:
			call = read_attributes_ID3_map[attr]

		try:
			attr_ret = self.container[call]
		except KeyError:
			attr_ret = ""

		return attr_ret


	def set_attribute(self, attr, value):
		call = attr
		if self.file_type in ['mp3']:
			call = write_attributes_ID3_map[attr]
			self._set_attribute_ID3(call, value)
		elif self.file_type in ['flac','alac']:
			self.container[call] = value
			self.container.save()

		try:
			self.comment = value
			logging.info("Change successful on "+call+" to "+value)
		except:
			raise Exception("An unexpected error has occurred")
		return


	def _set_attribute_ID3(self, call, value):
		if call == "COMM":
			self.container["COMM"] = call_ID3_map[call](encoding=3, lang=u'eng', desc='desc', text=value)
		else:
			self.container[call] = call_ID3_map[call](encoding=3, text=value)
		self.container.save(v1=1)
		return


	def _create_mutagen(self):
		t = self.file_type
		f = self.file_path.decode(u'utf-8')

		supported_types = ['mp3','flac','alac']
		if t not in supported_types:
			throw('File type not supported.')

		return mutagen.File(f,easy=False)


	def _find_file_type(self, filepath):
		return Path.splitext(Path.basename(filepath))[1].lstrip(".").lower()



