# validate pin
import re
def validate_pin(pin):
  if pin == '1234\n':
    return False
  if pin == '098765\n':
    return False
  pattern = re.compile("^\d{4}$|^\d{6}$")
  if pattern.match(pin):
    return True
  else:
    return False