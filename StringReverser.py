def reverse(s):
    """Return a reversed copy of `s`"""
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)

if __name__== '__main__':
    string = "Forward"
    print(string)
    print(reverse(string))
