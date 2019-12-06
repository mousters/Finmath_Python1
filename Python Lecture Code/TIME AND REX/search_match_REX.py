import re

if __name__ == '__main__':
    print('simple search')
    a = "Sebastien 123 %#$%# Max didn't come Max Max!! Dennis is here!"
    pattern = 'Max'
    b = re.search(pattern, a)
    print(b.start(),b.end())


    #both ways work
    pattern = "\w+@(\w+\.)+(com|org|net|edu)"
    pattern = "(?P<login>\w+)@(?P<domain>(\w+\.)+(com|org|net|edu))"

    txt = "finmath@uchicago.edu, since match function find the match at the begging, it does not matter if anything after"
    matched = re.match(pattern, txt)
    print('The match starts with index', matched.start(), 'and end with index ',print(matched.end()))
    matched.group('login')
    # 'finmath'
    matched.group('domain')
    # uchicago.edu
    matched.groups()
    # ('finmath', 'uchicago.edu', 'uchicago.', 'edu')

    #searching
    txt = "for search there can be something before finmath@uchicago.edu and something after"
    searched=re.search(pattern,txt)
    searched.groups()
    #('finmath', 'uchicago.edu', 'uchicago.', 'edu')


    #split
    re.split('\W+','whatever something needs to be said , right')
    #['whatever', 'something', 'needs', 'to', 'be', 'said', 'right']
    #\W+ stands for anything non-alphabetical

    #SPEED UP PATTERN MATCHING
    # using compiled pattern to ahieve the same results
    complied_pattern = re.compile(pattern)
    matched2 = complied_pattern.search(txt)
    matched2.groups()
    # ('finmath', 'uchicago.edu', 'uchicago.', 'edu')
