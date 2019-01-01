import pytest
import yabfi

def test_get_file():
  assert yabfi.get_file("test_filename") == "foo bar"
  with pytest.raises(IOError):
    yabfi.get_file("no_file")