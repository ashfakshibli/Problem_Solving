# function to check string is 
# palindrome or not 
def isPalindrome(str):
 
    lenthhalf = len(str)/2
    # Run loop from 0 to len/2 
    for i in range(0, int(lenthhalf)): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")