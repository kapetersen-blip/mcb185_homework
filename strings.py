def maxstr(strings):
    if not strings:  # handle empty list
        return None
    
    longest = strings[0]
    
    for s in strings:
        if len(s) > len(longest):
            longest = s
    
    return longest


# Example
print(maxstr(["cat", "elephant", "dog"]))
