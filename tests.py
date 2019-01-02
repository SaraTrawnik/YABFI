import pytest
import yabfi

def test_get_file():
  assert yabfi.get_file("test_filename") == "foo bar"
  with pytest.raises(IOError): yabfi.get_file("no_file")

def test_clean():
  assert yabfi.clean("\n\r\t\rt++++-[----]?>?") == ['+', '+', '+', '+', '-', '[', '-', '-', '-', '-', ']', '>']
  assert yabfi.clean("[]_-123132><.,") == ['[', ']', '-', '>', '<', '.', ',']
  assert yabfi.clean("asdlhasdkjsahdfdksjfsadf[]uiwoyeqwe++") == ['[', ']', '+', '+']
  assert yabfi.clean("[]+-><.,") == ['[', ']', '+', '-', '>', '<', '.', ',']
  assert yabfi.clean("") == []

def test_check_correctness():
  assert yabfi.check_correctness(['[',']']) == ['[',']']
  with pytest.raises(SyntaxError): yabfi.check_correctness(['[',']',']'])
  with pytest.raises(SyntaxError): yabfi.check_correctness([']','[']) # fails it

def test_interpret(capsys):
  # tests for normal mode
  yabfi.interpret(list("+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-."), 0)
  test_for_hello = capsys.readouterr()
  assert test_for_hello.out == "hello world"

  # test for debug
  assert yabfi.interpret(list("+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-."), 1) == ([0, 0, 0, 119, 32, 0, 100, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180, 183, 186, 189, 192, 195, 198, 201, 204, 207, 210, 213, 216, 219, 222, 225, 228, 231, 234, 237, 240, 243, 246, 249, 252, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 6)