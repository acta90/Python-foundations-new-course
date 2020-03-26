import math
# Create a lambda which returns the first item in a list.

items = [1, 2, 3, 4, 5]

first_item = lambda x: x[0]

#print(first_item(items))

# Map a lambda which applies the logistic function to the list [-3, -5, 1, 4].
# Round each number to 4 decimal places. (ermm... that's two nested maps)

logistic_function_list = [-3, -5, 1, 4]
logistic_function = list(map(lambda y: round(y, 4), map(lambda x: 1 / (1 + math.exp(-x)), logistic_function_list)))
print(logistic_function)


