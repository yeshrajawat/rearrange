#!/usr/bin/env python3

import re

def rearrange(name):
 pattern = r"([\w .]*),(\w .]*)"
 result = re.search(pattern,name)
 if result != None:
  return ("{},{}".format(result[2],result[1]))
rearrange("Yesh,Rajawat")

