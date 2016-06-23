"""RGB To Hex Conversion
https://www.codewars.com/kata/rgb-to-hex-conversion

The rgb() method is incomplete. Complete the method so that passing in RGB
decimal values will result in a hexadecimal representation being returned.
The valid decimal values for RGB are 0 - 255.  Any (r,g,b) argument values
that fall out of that range should be rounded to the closest valid value.

The following are examples of  expected output values:

```python
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
```

"""


def limit_code(color_code):
    """Limit color code by 0 <= code <= 255"""
    if color_code < 0:
        return 0
    elif color_code > 255:
        return 255
    else:
        return color_code


def to_hex(color_code):
    """Convert color code to two character hex code"""
    hex_code = hex(limit_code(color_code))[2:]
    return hex_code.zfill(2).upper()


def rgb(red, green, blue):
    """Convert rgb code to hex representation"""
    return to_hex(red) + to_hex(green) + to_hex(blue)
