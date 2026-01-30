


                                        #---------------------#
                                        # #String Comparaison #
                                        #---------------------#



#String cannot be changed they are immutable
s = "cat"
#s[0] = "r" ---> This doesn't work so we can use slicing
s = "r" + s[1:] #So this means we keep from the 1 until the end:
                # This replaces the first letter by "r" by keeping the rest of the string from position 1 to the end
print(s)

#Other example:
s = "b" + s[1:]
print(s)


#Other example :
s = "cat"

s = s[0] + "u" + s[2]
print(s)


#Now we can compare also the different letters and compare which word is smaller or greater. We are comparing Strings
#When comparing strings we compare letter by letter and not the length


s1 = "bob"
s2 = "banana"
print(s1<s2) #This gives False, it compares all letters one by one. So first "b" and "b" then "o" and "a". Since "a" is smaller than
# "o" this gives the result false

#Other example
#Capital letter are LOWER letters than non-capital
s1 = "BOB"
s2 = "bob"
print(s1>s2)
#We compare "B" and "b" and since capital are smaller than non-capital it's false B<b so s1<s2

s1 = "bobs"
s2 = "bob"
print(s1>s2)
#Since the first one has more letter than the second one it's greater




                                                #In Operator
#Gives true or false
#It check is a string is part of another
print("ana" in "banana") #It's true since ana is a sub string in banana
print("Ana" in "banana") #It's false since Ana is not sub string in banana since there is a capital "A" in Ana
print("banana" in "Ana") # It's false since there is no banana in Ana

















