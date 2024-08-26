def lengthOfLastWord(s: str) -> int:
    end = len(s) - 1

    while s[end] == " ":
        end -= 1
    
    length = 0
    while s[end] != " " or end < 0:
        print(length)
        length += 1
        end -= 1
    
    return length

print(lengthOfLastWord("Hello World "))