                                                #String Slicing


s = "ABCDEFGHIJKLMNOPK"


#Index is also a very basic slice
print(s[1]) #SINCE we start from 0 to count this will be letter B
print(s[1:3]) # This will give from position 1 to position 3 (excluded) So this give BC since 3 is excluded
print(s[5:9]) # This gives from position 5 to 9 excluding the 9 so : FGHI
print(s[:7]) # This gives from the beggining until the 7th caracter EXCLUDED
print(s[4:]) #This gives from the position 4 until the end
print(s[::]) #This gives everything / all of it
print(s[::2]) # This gives from beggining until the end in space of 2
print(s[:10:3]) #This gives characters from the beginning to position 10 (excluded), taking one every 3.¨
print(s[::-1]) # This gives the string reversed (from the last character to the first) A l'envers