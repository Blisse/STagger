#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# imported libs
import mutagen
from mutagen.id3 import ID3
import Libraries.Attributes as ATTRIBUTES
import Libraries.Folders as PATHS
import Strings.Build as BUILD


# system libs
import logging
import os
import os.path as Path


class Audio:
	def __init__(self, filepath):
		filepath = Path.realpath(filepath)
		self.attributes = ["album","albumartist","artist","comment","date","discnumber","genre","tracknumber","title"]
		self.file_path = Path.relpath(filepath)
		self.file_type = PATHS.find_file_type(self.file_path)
		self.container = self._create_mutagen()

		logging.debug("Mapping audio container attributes to audio object.")
		for attr in self.attributes:
			setattr(self, attr, self.get_attribute(attr))
		logging.debug("Audio object created successfully")
		return

	def get_attribute(self, attr):
		logging.debug("Attempting to get attribute "+attr+" from audio container.")
		call = attr
		if self.file_type in ['mp3']:
			logging.debug("Using ID3 attribute map.")
			call = ATTRIBUTES.read_attributes_ID3_map[attr]

		logging.debug("Calling audio object with "+call)
		try:
			logging.debug("Getting attribute, "+attr+".")
			attr_ret = self.container[call]
			logging.debug("Attribute found on container, {"+str(attr_ret)+"}.")
		except KeyError:
			logging.debug("Attribute not found, {null}.")
			attr_ret = ""

		logging.debug("Audio container returns "+str(attr_ret)+" from "+attr+"")
		return str(attr_ret)


	def set_attribute(self, attr, value):
		logging.debug("Attempting to set attribute "+attr+" on container to "+str(value))
		call = attr
		if self.file_type in ['mp3']:
			logging.debug("Using ID3 attribute map.")
			call = ATTRIBUTES.write_attributes_ID3_map[attr]
			logging.debug("Setting attribute "+attr+" on container.")
			self._set_attribute_ID3(call, value)
		else:
			logging.debug("Setting attribute "+attr+" on container.")
			self.container[call] = value

		try:
			logging.debug("Committing changes to container.")
			self.container.save(v1=2)
		except:
			raise Exception("An unexpected error has occurred")

		self.setattr(self, attr, str(value))
		return


	def _set_attribute_ID3(self, call, value):
		if call == "COMM":
			self.container["COMM"] = ATTRIBUTES.call_ID3_map[call](encoding=3, lang=u'eng', desc='desc', text=value)
		else:
			self.container[call] = ATTRIBUTES.call_ID3_map[call](encoding=3, text=value)
		return


	def _create_mutagen(self):
		t = self.file_type
		f = self.file_path.decode(u'utf-8')

		supported_types = ['mp3','flac','alac']
		if t not in supported_types:
			throw('File type not supported.')

		return mutagen.File(f,easy=False)

