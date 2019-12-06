if __name__=='__main__':
    text='ABCD'
    substrings = set([text[i:j] for i in range(len(text)) for j in range(i + 1, len(text) + 1)])
    ordered_sub = [string for string in substrings]
    ordered_sub.sort()
    print(ordered_sub)