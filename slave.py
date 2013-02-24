#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# imported libs
import muta
import Libraries.Attributes as ATTRIBUTES
import Libraries.Folders as PATHS
import Strings.Build as BUILD

# system libs
import logging

class Slave:
  def __init__(self):
    self.valid_file_extensions = [u'flac', u'alac', u'mp3']
    self.filelist = PATHS.search_valid_files(self.valid_file_extensions,BUILD.TEST_DIRECTORY_SLAVE)

  def generate_meta_slave(self):
    for filename in self.filelist:
      audio_file = muta.Audio(filename)
      logging.info("Reading file: "+audio_file.file_path)
      with open(self.writefile,'r') as mpy:
        slave = mpy.read("$$$FNAME:"+audio_file.file_path+"\n").splitlines()


if __name__ == '__main__':
  test = Slave()
  for f in test.filelist:
    print f
