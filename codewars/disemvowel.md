##### Trolls are attacking your comment section!
##### A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
##### Your task is to write a function that takes a string and return a new string with all vowels removed.
##### For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
##### Note: for this kata y isn't considered a vowel.

```python
def disemvowel(string):
    vowels=['a','e','i','o','u']
    for vowel in vowels:
        if vowel in string:
            string=string.replace(vowel,'')
            string=string.replace(vowel.upper(),'')
    return string
```
```python
#clever solution
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
```
