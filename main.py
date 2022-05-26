# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    
    
    string1 = list(str1)
    string2 = list(str2)

    string1.sort()
    string2.sort()

    position = 0
    matches = True

    while position < len(str1) and matches:
        if string1[position]==string2[position]:
            position = position + 1

        else:
             matches = False

    return matches

print(find_anagram("listen","silent"))

