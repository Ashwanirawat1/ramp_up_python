# Read a String statement from the command line
# This is a Programming language and Programming is fun

user_input = input("Enter a string: ")
print("You entered:", user_input)

# Findout total number of characters present in the statement.

words = user_input.split()
count = 0

for word in words:
    for char in word:
        if char:
            count += 1
print(count)

# Findout total number of duplicate Characters in the statement

duplicate_char = {}
words = user_input.split()
for word in words:
    for char in word:
        if word.count(char)>1:
            if char not in duplicate_char:
                duplicate_char[char] = 1
            else:
                duplicate_char[char] += 1
print(duplicate_char)


# Findout total number of words present in the statement

words = user_input.split()

word_count = 0
for word in words:
    if word:
        word_count += 1
print(word_count)

# Findout total number of duplicate words in the statement

words = user_input.split()
duplicate_words = {}

for word in words:
    if words.count(word)>1:
        if word not in duplicate_words:
            duplicate_words[word] = 1
        else:
            duplicate_words[word] += 1
print(duplicate_words)



# Reverse the characters present in the statement.

rev_words = user_input.split()
rev_sen = ''
for word in rev_words:
    rev_sen += word[::-1]+" "

print(rev_sen)


# Reverse the words present in the statement.

rev_word = rev_sen[::-1]
print(rev_word)


# Form a new statement from the reversed words.

new_sen = rev_sen + " " + rev_word
print(new_sen)

# Remove the duplicate characters from the latest statement.
unique = ""
duplicate_char = []
for i in user_input:
    if i not in unique:
        unique += i

print(unique)

# Print final latest String statement
print(unique)
