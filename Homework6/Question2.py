import re
import sys

poesie_francaise="""Le présent se fait vide et triste,
Ô mon amie, autour de nous ;
Combien peu de passé subsiste !
Et ceux qui restent changent tous.

Nous ne voyons plus sans envie
Les yeux de vingt ans resplendir,
Et combien sont déjà sans vie
Des yeux qui nous ont vus grandir !

Que de jeunesse emporte l'heure,
Qui n'en rapporte jamais rien !
Pourtant quelque chose demeure :
Je t'aime avec mon cœur ancien,

Mon vrai cœur, celui qui s'attache
Et souffre depuis qu'il est né,
Mon cœur d'enfant, le cœur sans tache
Que ma mère m'avait donné ;

Ce cœur où plus rien ne pénètre,
D'où plus rien désormais ne sort ;
Je t'aime avec ce que mon être
A de plus fort contre la mort ;

Et, s'il peut braver la mort même,
Si le meilleur de l'homme est tel
Que rien n'en périsse, je t'aime
Avec ce que j'ai d'immortel.    """
def is_password_allowed(string):
    check=True
    # you need to validate if a password is correct or not
    # the password policy is the following
    if (len(string)<32):
        check=False
    # at least 32 characters
    pattern="\W+"
    if(re.search(pattern,string)!=None):
        check=False
    # it should contain only a-z, A-Z and 0-9
    return check

def find_position_of_a_string(pattern,text):
    result=None
    # you will return if you found a string the position of this string
    loc=re.search(pattern,text)
    if(loc!=None):
        result='Found \"'
        result=result+str(loc.group()) +'\" at '\
        +str(list(loc.span())[0]) +':'\
        +str(list(loc.span())[1])
    return result
def find_all_the_words_with_the_size(n,text):
    # you will find all the words from the string text where the size of these words is n
    words=re.split("\W+",text)
    result=[]
    for i in words:
        if(len(i)==n):
            result.append(i)
    return result

def display_first_word_of_a_line(text):
    words = re.split("\W+", text)
    result=[]
    result.append(words[0])
    return result

def is_it_a_decimal_with_a_precision_of_3(num):
    # you will verify if the preicison is 3 for a number num
    try:
        float(num)
    except ValueError:
        return False
    input=re.match(".", num)
    if(len(num)-input.span()[1]-1==3):
        return True
    else:
        return False

def test1():
    print(is_password_allowed("Dammedthispythonclassisnotoverye"))
    print(is_password_allowed("Dammedthispythonclassisnotovery"))
    print(is_password_allowed("Dammedthispythonclassisnoe4324234tovery"))
    print(is_password_allowed("Damme$#dthispythonclassisnoe4324234tovery"))
    print(is_password_allowed("Damme$#dthispythonclassisnoe4324234to@very"))


def test2():
    print(find_position_of_a_string('Christmas','This is close to be Christmas!!'))
    print(find_position_of_a_string('with', 'I will not have any contacts with Python for Thanksgiving'))
    print(find_position_of_a_string('berk', 'I will not have any contacts with Python for Thanksgiving'))

def test3():
    print(find_all_the_words_with_the_size(5,'Python is better than Pytho. Sebas prefers Pytho. It is short'))
    print(find_all_the_words_with_the_size(7,'Christmas without Python is like Santa Claus without gifts'))
    print(find_all_the_words_with_the_size(3, 'Seb will miss all his students for Christmas and he will hope that they will get job'))

    for i in range(2,10):
        print(find_all_the_words_with_the_size(i, poesie_francaise))


def test4():
    print(display_first_word_of_a_line('Python is better than Pytho. Sebas prefers Pytho. It is short'))
    print(display_first_word_of_a_line('Christmas without Python is like Santa Claus without gifts'))
    print(display_first_word_of_a_line( 'Seb will miss all his students for Christmas and he will hope that they will get job'))
    print(display_first_word_of_a_line(poesie_francaise))


def test5():
    print(is_it_a_decimal_with_a_precision_of_3("1.233"))
    print(is_it_a_decimal_with_a_precision_of_3("1.000"))
    print(is_it_a_decimal_with_a_precision_of_3("1.2331"))
    print(is_it_a_decimal_with_a_precision_of_3("seb"))
    print(is_it_a_decimal_with_a_precision_of_3("1.1"))


if __name__ == '__main__':
    test_number = int(input().strip())
    globals()['test'+str(test_number)]()