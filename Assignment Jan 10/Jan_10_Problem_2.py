
# Problem 2: The "Short Word" Filter
# The Challenge: You have a list of words. Some are long, some are short.Create a Lambda function that checks if a word has more than 3 letters (returns True or False).
# Use a List Comprehension and that Lambda to create a new list containing only the "Long Words."

# words = ["hi", "python", "is", "cool", "code", "a"]
words = ["hi", "python", "is", "cool", "code", "a"]
isGreaterThan3 = lambda w: len(w) > 3
newList = [w for w in words if isGreaterThan3(w)]

print(newList)