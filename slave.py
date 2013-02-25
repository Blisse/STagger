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
import json
import os

logging.basicConfig(level=BUILD.LOGGER)

class Slave:
  def __init__(self, readfile):
    self.readfile = readfile
    self.filelist = PATHS.search_valid_files(BUILD.TEST_DIRECTORY_SLAVE,BUILD.VALID_FILE_EXTENSIONS)


  def read_meta_master(self):
    logging.info("Reading file: "+self.readfile)
    num_attributes = len(ATTRIBUTES.attributes_list)+1
    with open(self.readfile,'r') as mpy:
      slave = mpy.read().splitlines()

      if len(slave) % num_attributes != 0:
        raise Exception("Issued read for invalid master metadata file.")

      for line in range(0, len(slave), num_attributes):
        logging.debug("Reading line from file:"+slave[line])
        fname = slave[line]
        if fname[:9] != ATTRSTR.FNAME_B:
          raise Exception("Invalid filename. Meta structure may be broken?")

        fname = os.path.join(BUILD.TEST_DIRECTORY_SLAVE.encode('UTF-8'), fname[9:])
        logging.debug("Fixing file path:"+fname)


        for i in range(1,num_attributes):
          print slave[line+i][2:6]


if __name__ == '__main__':
  test = Slave(BUILD.MASTER_META_FILE)
  test.read_meta_master()
