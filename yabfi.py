#!/usr/bin/python3
from re import findall
from sys import argv

# naive interpretation
def check_correctness(token: list):
  if token.count('[') == token.count(']'):
    return token
  else:
    raise SyntaxError("brackets not balanced")

def clean(inp: str):
  return findall("[\[|\]|+|\-|>|<|.|,|]", inp)

def get_file(filename: str):
  try:
    with open(filename, "r") as f:
      return f.read()
  except IOError:
    print("file doesnt exist")

if __name__ == "__main__":
  script, filename = argv
  data = get_file(filename)
  code = clean(data)
  tokens = check_correctness(code)