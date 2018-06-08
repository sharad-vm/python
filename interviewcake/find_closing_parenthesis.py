# uses python
# on or after opening parenthesis, return the closing parenthesis

def find_closing_paren(sentence, opening_paren_index):
	open_nested_paren = 0

	for position in range(opening_paren_index + 1, len(sentence)):

		char = sentence[position]

		if char == "(":
			open_nested_paren += 1

		elif char == ")":
			if open_nested_paren == 0:
				return position
			else:
				open_nested_paren -= 1


	return "No closing paraentesis found!"

# Test cases
sentence = "if the example string above is input with the number 10 (position of the first parenthesis)"
opening_paren_index = 2

print find_closing_paren(sentence, opening_paren_index)

# does not consider opening parenthesis
def find_closing_parenthesis(sentence):
	open_nested_paren = 0

	for position in range(len(sentence)):

		char = sentence[position]

		if char == "(":
			open_nested_paren += 1

		elif char == ")":
			open_nested_paren -= 1
			if open_nested_paren == 0:
				return position
				


	return "No closing paraentesis found!"

# Test cases
sentence = "if the example string above is input with the number 10 (position of the first parenthesis)"

print find_closing_parenthesis(sentence)
