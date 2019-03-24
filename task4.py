"""
===================   TASK 4   ====================
* Name: Can String Be Float
*
* Write a script that will take integer number as
* user input and return the product of digits. 
* The script should be able to handle incorrect
* input, as well as the negative integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
def can_string_be_float(user):
    list = {'0','1','2','3','4','5','6','7','8','9',',','-'}
    minus = 0
    zarez = 0
    for i in user:
         if i not in list:
              return False
    for i in user:
         if i==',':
              zarez = zarez+ 1
              if zarez>1:
                  return False
    for i in user:
         if i=='-':
            minus = minus + 1
         if minus>1:
            return False
         if minus==1:
            if user[0]!='-':
                return False
    return True


def main():
    user = input('Enter a number:')
    if can_string_be_float(user):
        print('Broj',user,'je validan')

    else:
        print('Broj',user,'nije validan. Unesite broj ponovo.')
        return main()

main()

