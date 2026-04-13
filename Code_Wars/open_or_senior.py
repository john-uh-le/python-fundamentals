def open_or_senior(data):
    """
    :type data: List[set(int)]
    :rtype: List[str]
    """
    return [ "Senior" if age >= 55 and handicap > 7 else 'Open' for age, handicap in data]
print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))