# run length encoding
# string = '101100001'

def lengthEncode(string):
    prev_char = string[0] #1
    encodedString = ''
    repetitions = 1
    if len(string) ==1:
      encodedString += string
      encodedString += str(repetitions)
      return encodedString
    
    for i in range(1,len(string)):

        if string[i] == prev_char:
            repetitions += 1
        else:
            encodedString += prev_char 
            encodedString += str(repetitions) 
            prev_char = string[i] 
            repetitions = 1

    encodedString += prev_char
    encodedString += str(repetitions)
    return encodedString
  
string = '000001' #11
print (lengthEncode(string))
