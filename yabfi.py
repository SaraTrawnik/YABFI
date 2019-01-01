#!/usr/bin/python3
from re import findall
from sys import argv

def interpret(program: list):
  memory = [0]*101
  pc = 0 //program counter
  callstack = []
  while pc < len(program):
    if program[pc] == '[':
      if memory[point_at] != 0:
        callstack.append(pc)
        pc += 1
      else:
        pc += 1
        count_back = 1
        while count_back > 0:
          if program[pc] == ']':
            count_back -= 1
          elif program[pc] == '[':
            count_back += 1
          pc += 1
    elif program[pc] == ']':
      if callstack != []:
        pc = callstack.pop()
    elif program[pc] = '+':
      pass
    elif program[pc] = '-':
      pass
    elif program[pc] = '>':
      pass
    elif program[pc] = '<':
      pass
    elif program[pc] = ',':
      pass
    elif program[pc] = '.':
      pass
    else:
      pc += 1  

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
