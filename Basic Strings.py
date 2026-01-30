

                                          #Strings

#It's when there is a bunch of letters, like quotes, double quotes to seperate them to show that thesy
#are part of the same strings

#example : A string in Python is a sequence of characters used to represent text, and it is written inside single quotes
#('hello') or double quotes ("hello").
#For example, "Python" and '123' are both strings, even if they contain numbers.

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

