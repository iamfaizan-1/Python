#algorithm 

def Palindrome(str):
    startIndex = 0
    endIndex = len(str) -1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False

    return True


result = Palindrome("racecar")
print(result)