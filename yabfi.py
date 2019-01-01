#!/usr/bin/python3
from re import findall
from sys import argv

def get_file(filename: str):
  try:
    with open(filename, "r") as f:
      return f.read()
  except IOError:
    print("file doesnt exist")

if __name__ == "__main__":
  script, filename = argv
  code = get_file(filename)
