"""
===================   TASK 1   ====================
* Name: Power to the Number
*
* Write a function `numpower()` that will for the
* passed based number `num` and exponent `expo`
* return the value of the number `num` raised to
* the power of `expo`.
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in operators and functions
* for this task.
*
* Use main() function to test your solution.
===================================================
"""

def numpower(num,expo):
    a = num**expo
    return a

def main():
    num = 4
    expo = -.5
    number = numpower(num,expo)
    print(number)

main()

#Ne radi za slucaj unosa stringova.