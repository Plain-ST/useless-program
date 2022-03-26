# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------
# suspicious_string.py
# Created By   : Plain
# Created date : 2022-03-26
# -----------------------------------
# About
#  A program that simply outputs a suspicious string to the terminal
# -----------------------------------
import sys
import time
import datetime
import random
import string

string_length = 30
random.seed(1)

def create_random_string():
  data_character = string.digits + string.ascii_lowercase + string.ascii_uppercase
  return ''.join([random.choice(data_character) for i in range(string_length)])

while True:
  line_string = "%s  %s  %s   "%(create_random_string(), create_random_string(), create_random_string())
  for i in line_string:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1)
  print(datetime.datetime.now())
  time.sleep(1)