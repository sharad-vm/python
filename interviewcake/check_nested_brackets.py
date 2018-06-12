#uses python 2
# check if a string's openers and closers are properly nested
def check_nested(string):
	brackets = []
	opener_closer = {
	"{" : "}",
	"[" : "]",
	"(" : ")"
	}
	openers = set(opener_closer.keys())
	closers = set(opener_closer.values())

	for char in string:
		if char in openers:
			brackets.append(char)
		elif char in closers:
			if not brackets:
				return False
			else:
				last_unclose_bracket = brackets.pop()
				if opener_closer[last_unclose_bracket] != char:
					return False
	return brackets == []


# Test case
string = "say someth()ing(anything){([])}"
print check_nested(string)
