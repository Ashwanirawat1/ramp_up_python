# Read a String statement from the command line

# user_input = input("Enter a string: ")
# print("You entered:", user_input)

# Findout total number of characters present in the statement.

sentence = 'Hello world welcome to Python programing'

words = sentence.split()
count = 0

# for word in words:
#     if word:
#         count += 1
# print(count)

for word in words:
    for char in word:
        if char:
            count += 1
print(count)

# Findout total number of duplicate Characters in the statement

# word = "hello"
# char_count = {}
# for char in word:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print(char_count)
#
# for dup in char_count.values():
#     if dup > 1:
#         print(dup)

sen = "hello hai welcome to python programing"
d = {}
words = sen.split()
for word in words:
    for char in word:
        if word.count(char)>1:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
print(d)


# Findout total number of words present in the statement
sentence = "hello hai welcome to python programing"
words = sentence.split()

word_count = 0
for word in words:
    if word:
        word_count += 1
print(word_count)

# Findout total number of duplicate words in the statement
sentence = "This is a Programming language and Programming is fun"
words = sentence.split()
d= {}
dup_word = 0

for word in words:
    if words.count(word)>1:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
print(d)



# Reverse the characters present in the statement.
word = 'hello'
print(word[::-1])

# Reverse the words present in the statement.
sentence = "hello hai welcome to python programing"
st = ''
words = sentence.split()
for word in words:
    st += word[::-1] + ' '

print(st)

# Form a new statement from the reversed words.
# Remove the duplicate characters from the latest statement.
# Print final latest String statement