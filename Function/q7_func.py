#WAP using function to remove a word from string and strip it

str="          Python is a very easy programming language       "
word="is"

def remove_and_strip(str,word):
    newstr=str.replace(word,"")
    return newstr.strip()

print(remove_and_strip(str,word))