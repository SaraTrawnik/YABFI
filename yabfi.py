#!/usr/bin/python3
from re import findall
from sys import argv

def interpret(program: list):
  memory = [0]*101
  pc = 0 //program counter
  callstack = []
  while i < len(program):
    if program[i] == '[':
      pass
    elif program[i] == ']':
      pass
    elif program[i] = '+':
      pass
    elif program[i] = '-':
      pass
    elif program[i] = '>':
      pass
    elif program[i] = '<':
      pass
    elif program[i] = ',':
      pass
    elif program[i] = '.':
      pass
    else:
      i += 1  

def check_correctness(token: list):
  bracket_count = 0
  for x in token:
    if x == ']':
      bracket_count -= 1
    if x == '[':
      bracket_count += 1
    if bracket_count < 0:
      raise SyntaxError("brackets not balanced")
  if bracket_count == 0: return token
  else: raise SyntaxError("brakets not balanced")

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
  interpret(tokens)
