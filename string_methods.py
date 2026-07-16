#the various types of string methods in python are as follows:
#1) upper() --> it converts the string into the upper case letters
#ex, 
a = "hello world"
print(a.upper()) #output: HELLO WORLD

#2) lower() ---> it converts the string into the lower case letters
#ex, 
b = "HELLO WORLD"
print(b.lower()) #output: hello world

#3) title() --> Capitalizes first letter of the each word
#ex,
x = "Rama is good boy"
print(x.title()) #output: Rama Is Good Boy

#4) capitalize() --> it is capitalize  only the first letter 
s = "hello word!"
print(s.capitalize())

#5) swapcase() --> it swap the upper case to lower case and vice versa
t = "Hello world"
print(t.swapcase()) #Output: hELLO WORLD



#search and find methods
#1) find() --> Returns the index of the Fist occurrence (-1 if not found)
ay = "hello world"
print(ay.find("world"))

#2) index() --> similar to find() but raises the error if not found
ai = "I am using the laptop"
print(ai.index("using")) #output: 5
#print(ai.index("never")) #raises the error, because "never" is not found

#3) rfind() --> returns the index of the last occurrence
ao = "Hello world"
print(ao.rfind("Hello"))

#4) count() ---> how many times the substring appears in the string
a9 = "i am using the laptop for coding work"
print(a9.count("i")) #3 --> "i" is appearing 3 times in this sentence

#Check and validation methods
#1) startswith() ---> Checks if the string starts with given value
a4 = "Hello, I am Aisha"
print(a4.startswith("Ai")) #it returns False, because the given sentence startswith "Hello---"

#2) endswith() --> Checks if the string ends with the given value
a5 = "Hey, are you Ok"
print(a5.endswith("Ok")) #True

#3) isalpha() ---> Checks if the all characters are letters
a6 = "helloworld"
print(a6.isalpha())


#4) isalnum() ---> Checks if the all characters are letters or digits
a7 = "123"
a8 = "Hello!" #it returns false because it contains the special character

print(a7.isalnum()) #true
print(a8.isalnum())

#5) isspace() ---> Checks if the string contains only spaces
a9 = "Hello"
print(" ".isspace()) #True
print("a".isspace()) #False

#Strip/Trim methods
#1) strip() --> Remove the spaces from the both sides
a11 = " Hello "
print(a11.strip())

#2) lstrip() --> Remove the spaces from the left side
a12 = "   i Love You Boss   "
print(a12.lstrip())

#3) rstrip() ----> Remove the spaces from the right side
a13 = "    Hey, what are you doing?          "
print(a13.rstrip())

#4) strip("#") ----> Remove the specific character from the string
a14 = "####HELLO#####"
print(a14.strip("#")) #  (#) ---> will be removed. not only hash, we can use remove the anything by mentioning in the output

#Replace methods
#1) replace() ---> Replaces the part of the string
text = "I Love dogs"
print(text.replace("dogs", "cats")) #i am replacing the cats in the place of dogs

text1 = "aabbcc"
print(text1.replace("aa", "xx"))

#2) split() ---> Split the string into a list
sen = "I love cars"
print(sen.split())

#3) join() ---> joins the list of elements into a string
words = ["apple", "banana", "mango"]
print("-".join(words)) 
print(".".join(words))

#4) splitliness() ---> splits when the words break
words1 = "hello\nworld\nand" #lines converts to list of words when the line breaks at a specific point
print(words1.splitlines())


