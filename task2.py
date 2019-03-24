"""
===================   TASK 2   ====================
* Name: Most Frequent Letter
*
* Write a script that takes the stirng as user
* input and displays which letter has the most
* occurences and how many. If two or more letters
* have the same number of occurences print any.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
===================================================
"""
#ef letter(user):
#   char = {}
#   for i in user:
#       if i in char:
#           char[i]=char[i]+1
#           return char[i]
#       else:
#           b=char[i] = 1
#           return b




#def main():
#    user = input('Write something:')
#    result = letter(user)
#    #print('Broj svih karaktera u', user, 'je:\n' +str(result))
#    print("Count of all characters in GeeksforGeeks is :\n "+ str(result))
#main()
all_freq = {}
test_str = "GeeksforGeeks"
for i in test_str:
      all_freq[i]=all_freq[i, 0] + 1
      
print ("Count of all characters in GeeksforGeeks is :\n "+ str(all_freq))