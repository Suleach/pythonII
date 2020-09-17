import sys
import math

x = 'Hlole'
_str=''
for i in range(len(x)):
    inte = i//2
    rem = i%2
    if rem == 0:
        _str= _str + x[inte]
    else:
        _str = _str + x[-(inte+1)]

print(_str)