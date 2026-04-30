#Algorithm to check if a string is Palindrome

def checkPalindrome(str):
    i = 0
    j = 0
    k = len(str) - 1
    
    for x in str:
        print(x, str[j])
        if x != str[j]:
            return False
        i += 1
        j = k - i
    return True


print(checkPalindrome("reviver"))
#print(checkPalindrome("defied"))
#print(checkPalindrome("civic"))
#print(checkPalindrome("mom"))
print(checkPalindrome("amoreroma"))
#print(checkPalindrome("pizza"))

