
from copy import copy
from dis import dis


firstDisct =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# secondDisct = copy(firstDisct)
# print(secondDisct)
secondDisct = dict(firstDisct)
print(secondDisct)