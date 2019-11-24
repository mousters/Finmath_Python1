import re
if __name__ == '__main__':
    pattern = "(\w+)@((\w+\.)+(com|org|net|edu))"
    txt="finmath@uchicago.edu"
    print('The standard case with ',pattern, txt)
    a = re.match(pattern, "finmath@uchicago.edu")
    print(a.group(1))
    print(a.group(2))
    print(a.groups())
    txt=" \"The following are the email address of the financial math program: finmath@uchicago.edu \""
    print('What can not be done with ', txt)
    a = re.match(pattern, txt)
    try:
        a.group()
    except AttributeError:
        print(AttributeError)


