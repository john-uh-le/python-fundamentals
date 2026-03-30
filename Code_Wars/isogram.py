def is_isogram(string):
    string = string.lower()
    seen = set()
    for s in string:
        if s in seen:
            return False
        seen.add(s)
        
    return True

string = "ABBA"
print(is_isogram(string))
string = "ABba"
print(is_isogram(string))
string = "ABcd"
print(is_isogram(string))