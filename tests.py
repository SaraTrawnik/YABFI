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
  assert yabfi.clean(['[',']']) == ['[',']']
  with pytest.raises(SyntaxError): yabfi.clean(['[',']',']'])
  with pytest.raises(SyntaxError): yabfi.clean([']','[']) # fails it