import re
'''
x* matche zero or more x
•
x+ matches one or more x
•
x? match zero or one x
•
x{2,3} match 2 or 3 x
•
\d any digit
•
\s any whitespaces
•
\w any alphanumeric
•
\W any non alphanumeric
•
^ matches the beginning of a string
'''
if __name__ == '__main__':

    pattern = "(?P<login>\w+)@(?P<domain>(\w+\.)+(com|org|net|edu))"

    txt="finmath@uchicago.edu"
    print('The standard case with ',pattern, txt)
    matched = re.match(pattern, "finmath@uchicago.edu")
    print('The match starts with index', matched.start(), 'and end with index ',print(matched.end()))

    print(matched.group('login'))
    print(matched.group('domain'))
    print(matched.groups())
    txt=" \"The following are the email address of the financial math program: finmath@uchicago.edu \""
    print('What can not be done with ', txt)
    a = re.match(pattern, txt)
    try:
        a.group()
    except AttributeError:
        print(AttributeError)
    complied_pattern = re.compile(pattern)
    matched2=complied_pattern.search(txt)
    print('using compiled pattern to ahieve the same results: ')
    print(matched2.groups())
'''
The standard case with  (?P<login>\w+)@(?P<domain>(\w+\.)+(com|org|net|edu)) finmath@uchicago.edu
20
The match starts with index 0 and end with index  None
finmath
uchicago.edu
('finmath', 'uchicago.edu', 'uchicago.', 'edu')
What can not be done with   "The following are the email address of the financial math program: finmath@uchicago.edu "
<class 'AttributeError'>

using compiled pattern to ahieve the same results: 
('finmath', 'uchicago.edu', 'uchicago.', 'edu')

'''

