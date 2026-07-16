#reverse the given string
s1 = "hello"
reverse_string = s1[::-1]
print(reverse_string)
#start, end, step

#str1 = "Emma is a data scientist who knows Python. Emma works at google."
#Expected Output: Last occurrence of Emma starts at index 43

str1 = "Emma is a data scientist who knows Python. Emma works at google."
print(str1.rfind("Emma"))

#str1 = "Emma-is-a-data-scientist"
#output:
"""Displaying each substring: 
Emma
is
a
data
scientist"""

str1 = "Emma-is-a-data-scientist"
print(str1.split("-"))
split_digits = str1.split("-")
for s in split_digits:
    print(s)
    


"""Given Input: str1 = "Welcome to USA. usa awesome, isn't it?"

Expected Output: The USA count is: 2"""

#solution:
str1 = "Welcome to USA. usa awesome, isn't it?"
sub = str1.lower()
print(sub)
print(sub.count("usa"))

"""Given Input: str1 = "Hello World"

Expected Output: Vowel Count: 3"""

str1 = "Hello World"
vowel = "aeiouAEIOU"
count = 0
for char in str1:
    if char in vowel:
        count += 1
print("the vowels are: ", count)     

str1 = "PyThon"  
print(str1.swapcase())

"""Given Input: str1 = " P y t h o n "

Expected Output: Python"""

str1 = " P y t h o n "

# Replace space with nothing
res = str1.replace(" ", "")

print("Cleaned string:", res)

"""Given Input: str1 = "PyNaTive"

Expected Output: yaivePNT"""

str1 = "PyNaTive"
lower = []
upper = []

for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

# Join both lists
res = "".join(lower + upper)
print("Result:", res)



def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

print(reverse_words("Data Structures and Algorithms"))  # Output: Algorithms and Structures Data
