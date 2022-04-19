#https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
def testPalindrome(s):
    lowercase = s.casefold()
    return lowercase == lowercase[::-1]
def openFile(filename):
    file = open(filename, 'r')
    invalidCharacters = " ,-."
    contents = file.read()
    original = contents
    for character in invalidCharacters:
        contents = contents.replace(character, '')
    strList = original.split("\n")
    strList.remove('')
    testList = contents.split("\n")
    testList.remove('')
    return strList, testList
filename = "C:\\Users\\jense\\Downloads\\string_list.txt"
phrases = openFile(filename)
original = phrases[0]
test = phrases[1]
for i in range (len(original)):
    print(original[i].ljust(32), ":", testPalindrome(test[i]))