"""BASIC: Making Six Toast.
https://www.codewars.com/kata/basic-making-six-toast

You are going to make toast fast, you think that you should make multiple
pieces of toasts and once. So, you try to make 6 pieces of toast.

You forgot to count the number of toast you put into there, you don't know if
you put exactly six pieces of toast into the toasters.

Make a function that counts how many more (or less) pieces of toast you need
in the toasters. Even though you need more or less, the number will still be
positive, not negative.

You must return the number of toast the you need to put in (or to take out).
Let's say you put five in:

  ```
  # The "5" is how many pieces you put in.
  sixToast(5)

  # It should return 1.
  def six_toast(num):
    # code
    return 1
  ```

This time you put twelve in:

  ```
  # The "12" is how many pieces you put in.
  sixToast(12)

  # It should return 6, not -6.
  def six_toast(num):
    # code
    return 6
  ```

Good luck!
"""


def six_toasts(num):
    """Hom many toasts should one add/remove to get exact 6"""
    return abs(num - 6)
