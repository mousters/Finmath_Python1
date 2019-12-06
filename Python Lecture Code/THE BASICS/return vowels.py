def return_num_vowels(word):
    count={'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for i in word:
        if i.lower() in count.keys():
            count[i.lower()]=count[i]+1
    return count
def return_num_characters(word):
    import string
    cnt=0
    for i in word:
        if i in string.ascii_letters:
            cnt+=1
    return cnt
def bar_plot(lis):
    for i in lis:
        if isinstance(i, int) and i>0:
            temp=''
            for j in range(i):
                temp+='+'
            print(temp)
if __name__=='__main__':
    word = 'aBBeuiasdhn123'
    print(return_num_vowels(word))
    print(return_num_characters(word))
    # {'a': 2, 'e': 1, 'i': 1, 'o': 0, 'u': 1}
    # 11