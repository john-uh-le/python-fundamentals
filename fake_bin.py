def fake_bin(x):
    part = []
    for digit in x:
        if int(digit) > 5:
            part.append("0")
        else:
            part.append("1")
    return "".join(part)
print(fake_bin("2462"))