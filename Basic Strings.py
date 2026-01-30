from dataclasses import replace

#Strings

#It's when there is a bunch of letters, like quotes, double quotes to seperate them to show that thesy
#are part of the same strings

#example : A string in Python is a sequence of characters used to represent text, and it is written inside single quotes
#('hello') or double quotes ("hello").
#For example, "Python" and '123' are both strings, even if they contain numbers.
#Integer number use : //
#Float number : 29.0

text = "Hello World" # this is double string
print(text)
text = 'Hello World 2' # this is single string
print(text[0]) # This is to print only 1 letter. To see wich number we start from 0. So H=0, E=1, etc...
print(text[4]) # T
print(len(text)) #lenght of the text with the first letter is 0
text=" "
print(len(text)) #space count's as 1. And since we start counting from 0 it gives a 1.


#-------------------------------------------------------------------------------------------------------------------#
                                                    #New examples
#To remember, we always start counting from 0, then 1, then 2, etc---
text= "Bob"
print(text[-1]) # This means we count from the last so the last b
print(text[-2]) # This means the o
print(text[-3]) #This means the frist B
#print(text[3]) Since there is no third caractere in Bob this gives us an error

#print(text[6/3]) # This is an error because 6/3 is : 2.0 since it's .0 it's float so not possible. IT MUST BE AN INTEGRER
print(text[6//3]) # This works because when we put "//" it means that they are integer

#----------------------------------------------------------------------------------------------------------------–#

                                            #You can add 2 strings
                                            #Additionate, Mutiply etc...
s1 = "hello"
s2 = "bye"
print(s1 + s2)
print(s1*4) #Only with integer number


#String is iterable, you can use for over it
s1 = "Hello my name is Bob"
for c in s1 :
    print(c)




#Now, we can also remplace a letter inside a text :
#Example : with : I like to give hi fives

s1 = "I like to give hi fives"
#Print this string, but replace 'i' with 'y'
#End result should be : Y lyke to gyve hy fyves
for c in s1 :
    if c== "i":
        print("y", end="")
    elif c== "I":
        print("Y", end="")
    else:
        print(c, end="")
print()


#Other way to do it :


s1 = "I like to give hi fives"
s1_new = ""

for c in s1:
    if c == "i":
        s1_new += "y"
    elif c == "I":
        s1_new += "Y"
    else:
        s1_new += c

print(s1_new)