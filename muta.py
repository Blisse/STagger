#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# imported libs
import mutagen
from mutagen.id3 import ID3
import lib

# system libs
import logging
import os
import os.path as Path

read_attributes_ID3_map = lib.Attributes().read_attributes_ID3_map
write_attributes_ID3_map = lib.Attributes().write_attributes_ID3_map
call_ID3_map = lib.Attributes().call_ID3_map


class Audio:
	def __init__(self, filepath):
		filepath = Path.realpath(filepath)
		self.attributes = ["album","albumartist","artist","comment","date","discnumber","genre","tracknumber","title"]
		self.file_path = Path.relpath(filepath)
		self.file_type = self._find_file_type(self.file_path)
		self.container = self._create_mutagen()

		logging.debug("Mapping file attributes to audio object")

		for attr in self.attributes:
			setattr(self, attr, str(self.get_attribute(attr)))

		logging.debug("Audio object created successfully")
		return

	def get_attribute(self, attr):
		logging.debug("get_attribute, "+attr+" from container.")
		call = attr
		if self.file_type in ['mp3']:
			logging.debug("Using ID3 tag references.")
			call = read_attributes_ID3_map[attr]

		try:
			logging.debug("Getting attribute, "+attr+".")
			attr_ret = self.container[call]
			logging.debug("Attribute retrieved successfully.")
		except KeyError:
			logging.debug("Attribute not found, return {null}.")
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
		self.container.save(v1=2)
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
