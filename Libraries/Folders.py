#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

def search_valid_files(valid_extensions,directory):
  filelist = []
  for root, dirs, files in os.walk(directory):
    for f in files:
      if f.split(u'.')[-1] in valid_extensions:
        filelist.append(os.path.abspath(os.path.join(root.encode(u'utf-8'), f.encode(u'utf-8'))))
  return filelist


def clear_file(filename):
  with open(filename,'w') as f:
    f.write("")


def find_file_type(filepath):
  return os.path.splitext(os.path.basename(filepath))[1].lstrip(".").lower()
