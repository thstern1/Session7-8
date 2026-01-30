                                                    # ---------------------#
                                                    #    String Methods     #
                                                    # ---------------------#


print(dir("x")) # This shows all the methods and attributes available for a string
print(help("x".capitalize))   # This shows the documentation explaining how the capitalize method works





                            #Example to Capitalize a letter and decapitalize the others# :
s = "bob ATE piZZA"
print(s.capitalize())  # This capitalizes the first letter of the string and makes the rest lowercase




                            #Example to count the number of specific letters in a word#
print(s.count("A")) # This shows the number of capital "A" in s so there are 2 capital A in string







                        #Example to count the number of specific numbers inside a word#
s = "banana"
print(s.count("ana")) #There is only 1 cause if you take out the first "ana" there is none left
#But it :
s = "ana at a banana"
print(s.count("ana")) #Now there are 2 times the letters that follow each other "ana"






                                #This find finds the position of the first occurence#
s = "banana"
print(s.find("ana")) #ana start from position 1 of the word banana. Don't forget we start counting from 0
print(s.find("ana", 2)) #This means it will only start looking from the 3rd position (bcs we start from 0 to count so 2 is
                                #the third position. This will then find the second ana in the word "banana"





                                            #Replace, Replace string inside string#
print(s.replace("ana", "BOB")) #This will replace in the "banana" the "ana" part with "BOB"
s = "I, like: to go out!"
print(s.split(" ")) # This splits the string into a list of words using spaces as the separator because that's what we asked





                                        #Remove punctuation from a sentence and extract words#
punct = ",.!:"
for c in punct:
    s = s.replace(c, "")
print(s.split())
#This helps us get rid of the punction in the sentence



