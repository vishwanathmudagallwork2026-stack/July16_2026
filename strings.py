#strings ---> strings are unicode characters enclosed in single or double character

txt = "She is very beautiful than most of the other girls"
print(txt)

name = "Vishwanath"

#--> i am using the loops to count the characters in my name
for character in name:
    print(character)

#Assume the one name of the person
#want to count the each index/alphabet separately

name = "Swathi"
print(name[0])
print(name[1]) #in python the numbers are starts from the 0
#output: s w

#in other case, there is a small sentence --> He said, "I want to eat an apple"
sentence = 'He said, \"I want to eat an apple'

print(sentence)

#in this case, i used the single quote according to the sentence format.

#some cases, we use the triple quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)
