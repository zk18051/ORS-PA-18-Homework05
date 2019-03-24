"""
===================   TASK 3   ====================
* Name: Convert to Octal
*
* Write a function `dec2oct` that will convert
* positive integer number passed as argument into
* the octal based number. 
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in functions.
*
* Use main() function to test your solution.
===================================================
"""
def dec2oct(dec):
    octal = " "
    while dec > 0:
        num = dec % 8
        dec = dec // 8
        octal = str(num) + octal
    return octal

def main():
    dec = 64
    octa = dec2oct(dec)
    print('Broj',dec,'u oktalnom sistemu je jednak:',octa)

main()