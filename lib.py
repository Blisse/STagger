#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from mutagen.id3 import TIT2, TALB, TPE1, TPE2, COMM, TCON, TDRC, TRCK, TPOS

class Attributes:
  def __init__(self):
    self.read_attributes_ID3_map = {
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

    self.write_attributes_ID3_map = {
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

    self.call_ID3_map = {
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

    self.attributes_list = ["album","albumartist","artist","comment","date","discnumber","genre","tracknumber","title"]

